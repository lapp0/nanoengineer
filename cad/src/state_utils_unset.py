
class _UNSET_class:
    "[private class for _UNSET_, which sometimes represents unset attribute values, and similar things]"
    #e can we add a decl that makes the _s_attr system notice the bug if it ever hits this value in a real attrval? (should we?)
    def __init__(self, name = "_???_"):
        self.name = name
    def __repr__(self):
        return self.name
    pass

try:
    _UNSET_ # ensure only one instance of _UNSET_ itself, even if we reload this module
except:
    _UNSET_ = _UNSET_class("_UNSET_")

try:
    _Bugval
except:
    _Bugval = _UNSET_class("_Bugval")
