#!/usr/bin/env python

"""
test_zsession
-------------

Tests for the `zsession` module.
"""

import unittest
import zsession

class TestZsession(unittest.TestCase):
    def test_decode(self):
        zsession.decode("world!")
        pass
