#! /usr/bin/python

# Copyright 2005 Nanorex, Inc.  See LICENSE file for details.
import numpy as np
from VQT import *
from string import *
import re
import os
import sys

keypat = re.compile("(\S+)")
molpat = re.compile("mol \(.*\) (\S\S\S)")
atompat = re.compile("atom (\d+) \((\d+)\) \((-?\d+), (-?\d+), (-?\d+)\)")


def readmmp(fname):
    global atnum, elt, poshape
    pos = []
    elt = []
    atnum = -1
    atnos = {}
    bonds = [(0,0,0)]
    for card in open(fname).readlines():
        key = keypat.match(card).group(1)
        if key == 'atom':
            atnum += 1
            m = atompat.match(card)
            atnos[int(m.group(1))] = atnum
            elt += [int(m.group(2))]
            pos += [[float(m.group(n)) for n in [3,4,5]]]
        if key[:4] == 'bond':
            order = ['1','2','3','a','g'].index(key[4])
            bonds += [(atnum,atnos[int(x)],order)
                      for x in re.findall("\d+",card[5:])]
    pos = np.transpose(array(pos)/1000.0) # gives angstroms
    poshape = np.shape(pos)
    return elt, pos, np.array(bonds)



parmpat = re.compile("([A-Z][a-z]?)([\+=\-@#])([A-Z][a-z]?) +Ks= *([\d\.]+) +R0= *([\d\.]+) +De= *([\d\.]+)")
commpat = re.compile("#")

bendpat = re.compile("([A-Z][a-z]?)([\+=\-@#])([A-Z][a-z]?)([\+=\-@#])([A-Z][a-z]?) +theta0= *([\d\.]+) +Ktheta= *([\d\.]+)")


# masses in 1e-27kg
elmnts=[("H",   1,   1.6737),
        ("He",  2,   6.646),
        ("Li",  3,  11.525),
        ("Be",  4,  14.964),
        ("B",   5,  17.949),
        ("C",   6,  19.925),
        ("N",   7,  23.257),
        ("O",   8,  26.565),
        ("F",   9,  31.545),
        ("Ne", 10,  33.49),

        ("Na", 11,  38.1726),
        ("Mg", 12,  40.356),
        ("Al", 13,  44.7997),
        ("Si", 14,  46.6245),
        ("P",  15,  51.429),
        ("S",  16,  53.233),
        ("Cl", 17,  58.867),
        ("Ar", 18,  66.33),

        ("K",  19,  64.9256),
        ("Ca", 20,  66.5495),
        ("Sc", 21,  74.646),
        ("Ti", 22,  79.534),
        ("V",  23,  84.584),
        ("Cr", 24,  86.335),
        ("Mn", 25,  91.22),
        ("Fe", 26,  92.729),
        ("Co", 27,  97.854),
        ("Ni", 28,  97.483),
        ("Cu", 29, 105.513),
        ("Zn", 30, 108.541),
        ("Ga", 31, 115.764),
        ("Ge", 32, 120.53),
        ("As", 33, 124.401),
        ("Se", 34, 131.106),
        ("Br", 35, 132.674),
        ("Kr", 36, 134.429)]

elmass = np.array([0.0]+[1e-27*x[2] for x in elmnts])

enames = ['X']+[x[0] for x in elmnts]

btypes = ['-', '=', '+','@', '#']

def bondstr(elts,triple):
    return enames[elts[triple[0]]]+btypes[triple[2]]+enames[elts[triple[1]]]

def bendstr(elts,quint):
    return (enames[elts[quint[0]]]+btypes[quint[1]]+enames[elts[quint[2]]]
            +btypes[quint[1]]+enames[elts[quint[2]]])
# ks -- N/m
# R0 -- 1e-10 m
# De -- aJ

stretchtable={}
f=open("stretch.parms")
for lin in f.readlines():
    if commpat.match(lin): continue
    m = parmpat.match(lin)
    which = m.group(1)+m.group(2)+m.group(3)
    which1 = m.group(3)+m.group(2)+m.group(1)

    ks,r0,de = [float(m.group(p)) for p in [4,5,6]]

    bt=np.sqrt(ks/(2.0*de))/10.0
    stretchtable[which] = (ks,r0,de, bt)
    stretchtable[which1] = (ks,r0,de, bt)

# Theta - radians
# Ktheta - aJ/radian^2

bendtable={}
f=open("bending.parms")
for lin in f.readlines():
    if commpat.match(lin): continue
    m = bendpat.match(lin)
    which = m.group(1)+m.group(2)+m.group(3)+m.group(4)+m.group(5)
    which1 = m.group(5)+m.group(4)+m.group(3)+m.group(2)+m.group(1)

    th0, kth = [float(m.group(p)) for p in [6,7]]
    kth *= 100.0
    bendtable[which] = (th0, kth)
    bendtable[which1] = (th0, kth)

# given a set of stretch bonds, return the bend quintuples
def bondsetup(bonds):
    global bond0, bond1, KS, R0
    global sort0,mash0,spred0, sort1,mash1,spred1
    global bends, Theta0, Ktheta, bba, bbb, bbc
    global bbsorta, bbmasha, bbputa
    global bbsortb, bbmashb, bbputb
    global bbsortc, bbmashc, bbputc

    n = atnum+1

    bond0 = bonds[:,0]
    bond1 = bonds[:,1]

    sort0 = np.argsort(bond0)
    x0=np.take(bond0,sort0)
    x=x0[1:]!=x0[:-1]
    x[0]=1
    x=np.compress(x,arange(len(x)))
    mash0=np.concatenate((array([0]),x+1))
    spred0=np.zeros(n)
    x=np.take(x0,mash0[1:])
    np.put(spred0,x,1+arange(len(x)))

    sort1 = np.argsort(bond1)
    x1=np.take(bond1,sort1)
    x=x1[1:]!=x1[:-1]
    x[0]=1
    x=np.compress(x,arange(len(x)))
    mash1=np.concatenate((array([0]),x+1))
    spred1=np.zeros(n)
    x=np.take(x1,mash1[1:])
    np.put(spred1,x,1+arange(len(x)))

    btlis = [bondstr(elt,x) for x in bonds]
    KS = np.array([stretchtable[x][0] for x in btlis])
    KS[0]=0.0
    R0 = np.array([stretchtable[x][1] for x in btlis])
    R0[0]=0.0

    bondict = {}
    bends = []
    for (a,b,o) in bonds[1:]:
        bondict[a] = bondict.get(a,[]) + [(o,b)]
        bondict[b] = bondict.get(b,[]) + [(o,a)]
    for (a,lis) in bondict.items():
        for i in range(len(lis)-1):
            (ob,b) = lis[i]
            for (oc,c) in lis[i+1:]:
                bends += [(b,ob,a,oc,c)]
    bends = np.array(bends)
    bba = bends[:,0]
    bbb = bends[:,4]
    bbc = bends[:,2]
    bnlis = [bendstr(elt,x) for x in bends]
    Theta0 = np.array([bendtable[b][0] for b in bnlis])
    Ktheta = np.array([bendtable[b][1] for b in bnlis])

    n=len(elt)

    bbsorta = np.argsort(bba)
    x1=np.take(bba,bbsorta)
    x2=x1[1:]!=x1[:-1]
    x=np.compress(x2,arange(len(x2)))
    bbmasha=np.concatenate((array([0]),x+1))
    bbputa = np.compress(concatenate((array([1]),x2)),x1)
    bbputa = np.concatenate((bbputa, n+bbputa, 2*n+bbputa))

    bbsortb = np.argsort(bbb)
    x1=np.take(bbb,bbsortb)
    x2=x1[1:]!=x1[:-1]
    x=np.compress(x2,arange(len(x2)))
    bbmashb=np.concatenate((array([0]),x+1))
    bbputb = np.compress(concatenate((array([1]),x2)),x1)
    bbputb = np.concatenate((bbputb, n+bbputb, 2*n+bbputb))

    bbsortc = np.argsort(bbc)
    x1=np.take(bbc,bbsortc)
    x2=x1[1:]!=x1[:-1]
    x=np.compress(x2,arange(len(x2)))
    bbmashc=np.concatenate((array([0]),x+1))
    bbputc = np.compress(concatenate((array([1]),x2)),x1)
    bbputc = np.concatenate((bbputc, n+bbputc, 2*n+bbputc))

    return bends


# aa means stretch bond (atom-atom)
# bb means bend (bond-bond)
# bba, bbb, bbc are the three atoms in a bend, bbc the center
#
#globals: bond0, bond1: atom #'s; R0s; KSs
def force(pos):
    aavx = np.take(pos,bond0,1) - take(pos,bond1,1)
    aax = np.sqrt(np.add.reduce(aavx*aavx))
    aax[0]=1.0

    aavu = aavx/aax
    aavf = aavu * KS * (R0 - aax)

    avf0 = np.add.reduceat(take(aavf,sort0,1),mash0)
    avf1 = np.add.reduceat(take(aavf,sort1,1),mash1)
    f = take(avf0,spred0,1) - take(avf1,spred1,1)

    bbva = take(pos,bba,1) - take(pos,bbc,1)
    bbvb = take(pos,bbb,1) - take(pos,bbc,1)
    bbla = np.sqrt(np.add.reduce(bbva*bbva))
    bblb = np.sqrt(np.add.reduce(bbvb*bbvb))
    bbau = bbva/bbla
    bbbu = bbvb/bblb
    bbadb = np.add.reduce(bbau*bbbu)
    angle = np.arccos(bbadb)
    torq = Ktheta*(angle-Theta0)

    bbaf = bbbu-bbadb*bbau
    bbaf = bbaf/np.sqrt(np.add.reduce(bbaf*bbaf))
    bbaf = bbaf*torq/bbla
    bbbf = bbau-bbadb*bbbu
    bbbf = bbbf/np.sqrt(np.add.reduce(bbbf*bbbf))
    bbbf = bbbf*torq/bblb

    fa = np.zeros(poshape,np.float64)
    np.put(fa,bbputa,np.add.reduceat(np.take(bbaf,bbsorta,1),bbmasha))
    fc1 = np.zeros(poshape,np.float64)
    np.put(fc1,bbputc,np.add.reduceat(np.take(bbaf,bbsortc,1),bbmashc))

    fb = np.zeros(poshape,np.float64)
    np.put(fb,bbputb,np.add.reduceat(np.take(bbbf,bbsortb,1),bbmashb))
    fc2 = np.zeros(poshape,Float)
    np.put(fc2,bbputc,np.add.reduceat(np.take(bbbf,bbsortc,1),bbmashc))

    return f+fa+fb-fc1-fc2


