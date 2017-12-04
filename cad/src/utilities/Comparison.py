# Copyright 2005-2009 Nanorex, Inc.  See LICENSE file for details.
"""
utilities/Comparison.py - provides same_vals, for correct equality comparison.
See also state_utils.py, which contains the closely related copy_val.

@author: Bruce
@version: $Id$
@copyright: 2005-2009 Nanorex, Inc.  See LICENSE file for details.

History:

same_vals was written as part of state_utils.py [bruce]

moved same_vals into utilities/Comparison.py to break an import cycle
[ericm 071005]

moved SAMEVALS_SPEEDUP and "import samevals" along with it
(but left the associated files in cad/src, namely samevals.c [by wware],
setup2.py [now in outtakes], and part of Makefile) [bruce 071005]
"""


# refactoring - this file seems to only have existed because
# Numeric was improperly implemented. Instead, we will require numpy
# until this is completely refactored out

import numpy

def same_vals(v1, v2): #060303
    return v1 == v2
