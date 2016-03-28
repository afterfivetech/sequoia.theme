# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from sequoia.theme.testing import SEQUOIA_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that sequoia.theme is properly installed."""

    layer = SEQUOIA_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sequoia.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'sequoia.theme'))

    def test_browserlayer(self):
        """Test that ISequoiaThemeLayer is registered."""
        from sequoia.theme.interfaces import (
            ISequoiaThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(ISequoiaThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SEQUOIA_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['sequoia.theme'])

    def test_product_uninstalled(self):
        """Test if sequoia.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'sequoia.theme'))

    def test_browserlayer_removed(self):
        """Test that ISequoiaThemeLayer is removed."""
        from sequoia.theme.interfaces import ISequoiaThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(ISequoiaThemeLayer, utils.registered_layers())
