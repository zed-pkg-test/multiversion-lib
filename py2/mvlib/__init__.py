# -*- coding: utf-8 -*-
"""Python 2 line of multiversion-lib.

Uses u"" literals and unicode_literals, which is what makes this subtree
2.7-shaped rather than merely 2.7-compatible.
"""
from __future__ import unicode_literals

LANGUAGE = "python"
RUNTIME_LINE = "python2"


def greet(who):
    return "hello {0} from multiversion-lib/python2".format(who)
