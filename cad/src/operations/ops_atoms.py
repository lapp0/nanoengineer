# Copyright 2004-2009 Nanorex, Inc.  See LICENSE file for details.
"""
ops_atoms.py -- operations on the atoms and/or bonds inside a Part.
These operations generally create or destroy atoms, bondpoints, or real bonds.
Operations specific to single modes (Build, Crystal, Extrude) are not included here.

@version: $Id$
@copyright: 2004-2009 Nanorex, Inc.  See LICENSE file for details.

History:

bruce 050507 made this by collecting appropriate methods (by various authors)
from existing modules, from class Part and class basicMode.
"""

from utilities.Log import greenmsg, redmsg

from utilities.constants import SELWHAT_CHUNKS, SELWHAT_ATOMS
from utilities.constants import gensym

from platform_dependent.PlatformDependent import fix_plurals

from model.elements import Singlet
from model.chem import Atom

import foundation.env as env

class ops_atoms_Mixin:
    """
    Mixin class for providing these methods to class Part
    """

    def make_Atom_and_bondpoints(self,
                                 elem,
                                 pos,
                                 atomtype = None,
                                 Chunk_class = None ):
        """
        Create one unbonded atom, of element elem
        and (if supplied) the given atomtype
        (otherwise the default atomtype for elem),
        at position pos, in its own new chunk,
        with enough bondpoints to have no valence error.

        @param Chunk_class: constructor for the returned atom's new chunk
                            (self.assy.Chunk by default)

        @return: one newly created Atom object, already placed into a new
                 chunk which has been added to the model using addnode
        """
        #bruce 041215 moved this from chunk.py to chem.py, and split part of it
        # into the new atom method make_bondpoints_when_no_bonds, to help fix bug 131.
        #bruce 050510 added atomtype option
        #bruce 080520 added Chunk_class option
        #bruce 090112 renamed oneUnbonded function and turned it into this method
        assy = self.assy
        if Chunk_class is None:
            Chunk_class = assy.Chunk
        chunk = Chunk_class(assy, 'bug') # name is reset below!
        atom = Atom(elem.symbol, pos, chunk)
        # bruce 041124 revised name of new chunk, was gensym('Chunk.');
        # no need for gensym since atom key makes the name unique, e.g. C1.
        atom.set_atomtype_but_dont_revise_singlets(atomtype)
            # ok to pass None, type name, or type object; this verifies no change in elem
            # note, atomtype might well already be the value we're setting;
            # if it is, this should do nothing
        ## chunk.name = "Chunk-%s" % str(atom)
        chunk.name = gensym("Chunk", assy) #bruce 080407 per Mark NFR desire
        atom.make_bondpoints_when_no_bonds() # notices atomtype
        assy.addnode(chunk) # REVIEW: same as self.addnode?
        return atom

    def modifyTransmute(self, elem, force = False, atomType = None):
        """
        This method was originally a method of class mode and selectMode.
        Transmute selected atoms into <elem> and with an optional <atomType>.
        <elem> is an element number that selected atoms will be transmuted to.
        <force>: boolean variable meaning keeping existing bond or not.
        <atomType>: the optional hybrid bond type if the element support hybrid. --Huaicai[9/1/05]
        """
        # now change selected atoms to the specified element
        # [bruce 041215: this should probably be made available for any modes
        #  in which "selected atoms" are permitted, not just Select modes. #e]
        from model.elements import PeriodicTable
        if self.selatoms:
            dstElem = PeriodicTable.getElement(elem)
            for atm in list(self.selatoms.values()):
                atm.Transmute(dstElem, force = force, atomtype=atomType)
                # bruce 041215 fix bug 131 by replacing low-level mvElement call
                # with new higher-level method Transmute. Note that singlets
                # can't be selected, so the fact that Transmute does nothing to
                # them is not (presently) relevant.
            #e status message?
            # (Presently a.Transmute makes one per "error or refusal".)
            self.o.gl_update()

        if self.selmols: #bruce 060720 elif -> if, in case both atoms and chunks can be selected someday
            dstElem = PeriodicTable.getElement(elem) #bruce 060720 fix typo dstElm -> dstElem to fix bug 2149
                # but we have to decide if we want the behavior this now gives us, of transmuting inside selected chunks.
            for mol in self.selmols[:]:
                for atm in list(mol.atoms.values()):
                    atm.Transmute(dstElem, force = force, atomtype=atomType)
                        # this might run on some killed singlets; should be ok
            self.o.gl_update()

        return

    def modifyDeleteBonds(self):
        """
        Delete all bonds between selected and unselected atoms or chunks
        """
        cmd = greenmsg("Delete Bonds: ")

        if not self.selatoms and not self.selmols: # optimization, and different status msg
            msg = redmsg("Nothing selected")
            env.history.message(cmd + msg)
            return

        cutbonds = 0

        # Delete bonds between selected atoms and their neighboring atoms that are not selected.
        for a in list(self.selatoms.values()):
            for b in a.bonds[:]:
                neighbor = b.other(a)
                if neighbor.element != Singlet:
                    if not neighbor.picked:
                        b.bust()
                        a.pick() # Probably not needed, but just in case...
                        cutbonds += 1

        # Delete bonds between selected chunks and chunks that are not selected.
        for mol in self.selmols[:]:
            # "externs" contains a list of bonds between this chunk and a different chunk
            for b in mol.externs[:]:
                # atom1 and atom2 are the connect atoms in the bond
                if int(b.atom1.molecule.picked) + int(b.atom2.molecule.picked) == 1:
                    b.bust()
                    cutbonds += 1

        msg = fix_plurals("%d bond(s) deleted" % cutbonds)
        env.history.message(cmd + msg)

        if self.selatoms and cutbonds:
            self.modifySeparate() # Separate the selected atoms into a new chunk
        else:
            self.w.win_update() #e do this in callers instead?
        return

    # change surface atom types to eliminate dangling bonds
    # a kludgey hack
    # bruce 041215 added some comments.
    def modifyPassivate(self):

        cmd = greenmsg("Passivate: ")

        if not self.selatoms and not self.selmols: # optimization, and different status msg
            msg = redmsg("Nothing selected")
            env.history.message(cmd + msg)
            return

        if self.selwhat == SELWHAT_CHUNKS:
            for m in self.selmols:
                m.Passivate(True) # arg True makes it work on all atoms in m
        else:
            assert self.selwhat == SELWHAT_ATOMS
            for m in self.molecules:
                m.Passivate() # lack of arg makes it work on only selected atoms
                # (maybe it could just iterate over selatoms... #e)

        # bruce 050511: remove self.changed (since done as needed in atom.Passivate) to fix bug 376
        ## self.changed() # could be much smarter
        self.o.gl_update()

    # add hydrogen atoms to each dangling bond
    # Changed this method to mirror what modifyDehydrogenate does.
    # It is more informative about the number of chunks modified, etc.
    # Mark 050124
    def modifyHydrogenate(self):
        """
        Add hydrogen atoms to bondpoints on selected chunks/atoms.
        """
        cmd = greenmsg("Hydrogenate: ")

        fixmols = {} # helps count modified mols for statusbar
        if self.selmols:
            counta = countm = 0
            for m in self.selmols:
                changed = m.Hydrogenate()
                if changed:
                    counta += changed
                    countm += 1
                    fixmols[id(m)] = m
            if counta:
                didwhat = "Added %d atom(s) to %d chunk(s)" \
                          % (counta, countm)
                if len(self.selmols) > countm:
                    didwhat += \
                        " (%d selected chunk(s) had no bondpoints)" \
                        % (len(self.selmols) - countm)
                didwhat = fix_plurals(didwhat)
            else:
                didwhat = "Selected chunks contain no bondpoints"

        elif self.selatoms:
            count = 0
            for a in list(self.selatoms.values()):
                ma = a.molecule
                for atm in a.neighbors():
                    matm = atm.molecule
                    changed = atm.Hydrogenate()
                    if changed:
                        count += 1
                        fixmols[id(ma)] = ma
                        fixmols[id(matm)] = matm
            if fixmols:
                didwhat = \
                    "Added %d atom(s) to %d chunk(s)" \
                    % (count, len(fixmols))
                didwhat = fix_plurals(didwhat)
                # Technically, we *should* say ", affected" instead of "from"
                # since the count includes mols of neighbors of
                # atoms we removed, not always only mols of atoms we removed.
                # Since that's rare, we word this assuming it didn't happen.
                # [#e needs low-pri fix to be accurate in that rare case;
                #  might as well deliver that as a warning, since that case is
                #  also "dangerous" in some sense.]
            else:
                didwhat = "No bondpoints on selected atoms"
        else:
            didwhat = redmsg("Nothing selected")

        if fixmols:
            self.changed()
            self.w.win_update()
        env.history.message(cmd + didwhat)
        return

    # Remove hydrogen atoms from each selected atom/chunk
    # (coded by Mark ~10/18/04; bugfixed/optimized/msgd by Bruce same day,
    #  and cleaned up (and perhaps further bugfixed) after shakedown changes
    #  on 041118.)
    def modifyDehydrogenate(self):
        """
        Remove hydrogen atoms from selected chunks/atoms.
        """
        cmd = greenmsg("Dehydrogenate: ")

        fixmols = {} # helps count modified mols for statusbar
        if self.selmols:
            counta = countm = 0
            for m in self.selmols:
                changed = m.Dehydrogenate()
                if changed:
                    counta += changed
                    countm += 1
                    fixmols[id(m)] = m
            if counta:
                didwhat = "Removed %d atom(s) from %d chunk(s)" \
                          % (counta, countm)
                if len(self.selmols) > countm:
                    didwhat += \
                        " (%d selected chunk(s) had no hydrogens)" \
                        % (len(self.selmols) - countm)
                didwhat = fix_plurals(didwhat)
            else:
                didwhat = "Selected chunks contain no hydrogens"
        elif self.selatoms:
            count = 0
            for a in list(self.selatoms.values()):
                ma = a.molecule
                for atm in list(a.neighbors()) + [a]:
                    #bruce 041018 semantic change: added [a] as well
                    matm = atm.molecule
                    changed = atm.Dehydrogenate()
                    if changed:
                        count += 1
                        fixmols[id(ma)] = ma
                        fixmols[id(matm)] = matm
            if fixmols:
                didwhat = \
                    "Removed %d atom(s) from %d chunk(s)" \
                    % (count, len(fixmols))
                didwhat = fix_plurals(didwhat)
                # Technically, we *should* say ", affected" instead of "from"
                # since the count includes mols of neighbors of
                # atoms we removed, not always only mols of atoms we removed.
                # Since that's rare, we word this assuming it didn't happen.
                # [#e needs low-pri fix to be accurate in that rare case;
                #  might as well deliver that as a warning, since that case is
                #  also "dangerous" in some sense.]
            else:
                didwhat = "No hydrogens bonded to selected atoms"
        else:
            didwhat = redmsg("Nothing selected")
        if fixmols:
            self.changed() #e shouldn't we do this in lower-level methods?
            self.w.win_update()
        env.history.message(cmd + didwhat)
        return

    pass # end of class ops_atoms_Mixin

# end
