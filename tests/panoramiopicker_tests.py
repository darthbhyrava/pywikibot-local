# -*- coding: utf-8 -*-
"""Test methods in panoramiopicker script."""
#
# (C) Pywikibot team, 2016
#
# Distributed under the terms of the MIT license.
#
from __future__ import absolute_import, unicode_literals
__version__ = '$Id'

from scripts import panoramiopicker

from tests.aspects import unittest, TestCase


class TestPanoramioMethods(TestCase):

    """Test methods in panoramiopicker."""

    def test_get_license(self):
        """Test getLicense() method."""
        x = panoramiopicker.getPhotos(photoset=u'public', start_id='0', end_id='5')
        for photoinfo in x:
            photoinfo = panoramiopicker.getLicense(photoinfo)
            self.assertIsNotNone(photoinfo['license'])


if __name__ == '__main__':
    unittest.main()
