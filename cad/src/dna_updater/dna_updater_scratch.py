
    # find directional bond chains (or rings) covering our atoms

    def func( atom1, dir1): # wrong, see below
        if atom1.killed(): ###k
            return ### best place to do this?
        for b in atom1.bonds:
            if b.is_directional():
                a1, a2 = b.atom1, b.atom2
                dir1[a1.key] = a1
                dir1[a2.key] = a2
        return
    all_atoms = transclose( initial_atoms, func )

    # wait, that only found all atoms, not their partition... ###

    # does transclose know when it has to go back to an initial atom to find more? probably not.
    # it does not even assume equiv relation, but on one-way relation this partition is not defined.

    # also when we do find these partitions, we probably want their chain lists, not just their sets.
    # so make new finding code to just grab the chains, then see which initial_atoms can be dropped (efficiently).
    # probably mark the atoms or store them in dicts, as well as making chains.
    # An easy way: grow_bond_chain, and a custom next function for it. It can remove from initial_atoms too, as it runs past.

    return

# ==

def _pop_arbitrary_atom_with_qualifying_bond(atoms_dict, bond_ok_func):
    """
    Return (atom, bond) (and pop atom from atoms_dict) where atom has bond
    and bond_ok_func(bond) is true, or return (None, None) if no remaining
    atoms have qualifying bonds.

    Also pop all atoms returned, and all atoms skipped since they have no
    qualifying bonds. This means that atoms_dict will be empty when we
    return (None, None). It also means any atom is returned at most once,
    during repeated calls using the same atoms_dict, even if it has more
    than one qualifying bond.

    Warning: there is no atom_ok_func, and we consider all atoms or bondpoints
    with no checks at all, not even of atom.killed().
    
    In typical usage, the caller might add atoms to or remove atoms from
    atoms_dict between repeated calls, terminating a loop when we return
    (None, None) and/or when atoms_dict becomes empty.
    """
    while atoms_dict:
        key_unused, atom = pop_arbitrary_item(atoms_dict)
        # Assume any atom with a qualifying bond is ok
        # (i.e. caller must exclude non-ok atoms).
        # [Someday we might need to add an atom_ok_func,
        #  or a func that looks at both atom and bond,
        #  if of two atoms on an ok bond, only one might be ok.
        #  But it's probably still easier to do it in a helper function
        #  (like this one) than directly in a caller loop, due to our
        #  desire to pop atom as soon as we return it with any bond,
        #  even if it qualifies with other bonds too.]
        for bond in atom.bonds:
            if bond_ok_func(bond):
                return atom, bond
        # REVIEW: should we return (atom, None) here?
    return None, None

def find_chains_or_rings(unprocessed_atoms, atom_ok_func): # needs rewrite as in TODO @@@ ; REVIEW: discard lone atoms ok??
        # TODO: also needs a function to find one bond or test one bond;
        # if that func just returns the special bonds from an atom, up to 2, open bonds ok??,
        # then maybe it's enough and we can use it to make the next_bond_in_chain function too.
        # (Or the special func could just be an atom test...)
    # ...
    def bond_ok_func(bond):
        return atom_ok_func(bond.atom1) and \
               atom_ok_func(bond.atom2)
    def next_bond_in_chain(...):
        pass...
    while True:
        atom, bond = _pop_arbitrary_atom_with_qualifying_bond(unprocessed_atoms, bond_ok_func)
        if atom is None:
            assert not unprocessed_atoms
            break
        (ringQ, listb, lista) = res_element = grow_bond_chain(bond, atom, next_bond_in_chain)
        
        ### BUG: only grows in one direction!
        # see some caller
        #   of grow_bond_chain
        #   or grow_directional_bond_chain
        # which calls it twice...
        # ... hmm, make_pi_bond_obj calls twice grow_pi_sp_chain
        
        for atom in lista:
            unprocessed_atoms.pop(atom.key, None)
        res.append( res_element)
        continue
    

    return ksddskj


def pop_arbitrary_item(dict1):
    """
    If dict1 is not empty, efficiently pop and return
    an arbitrary item (key, value pair) from it.
    Otherwise return None.
    """
    if not dict1:
        return None
    key, val_unused = item = arbitrary_item(dict1)
    del dict1[key]
    return item

def arbitrary_item(dict1):
    """
    If dict1 is not empty, efficiently return an arbitrary item
    (key, value pair) from it. Otherwise return None.
    """
    for item in dict1.iteritems():
        return item
    return None


# a lot of atom methods about directional bonds would also apply to axis bonds... almost unchanged, isomorphic
# but i guess i'll dup/revise the code
# also is it time to move these into subclasses of atom? i could introduce primitive updater that just keeps atom
# classes right... it might help with open bonds marked as directional... have to review all code that creates them.
# (and what about mmp reading? have to assume correct structure; for bare strand ends use geom or be arb if it is)


