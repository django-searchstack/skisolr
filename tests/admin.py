# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from skisolr import SolrCoreAdmin


class SolrCoreAdminTestCase(unittest.TestCase):
    def setUp(self):
        super(SolrCoreAdminTestCase, self).setUp()
        self.solr_admin = SolrCoreAdmin('http://localhost:8983/solr/admin/cores')

    def test_status(self):
        self.assertTrue('name="defaultCoreName"' in self.solr_admin.status())
        self.assertTrue('<int name="status">' in self.solr_admin.status(core='core0'))

    def test_reload(self):
        self.assertTrue('<int name="status">0</int>' in self.solr_admin.reload('core0'))

    def test_rename(self):
        self.assertTrue('<int name="status">0</int>' in self.solr_admin.rename('core0', 'coreX'))
        self.assertTrue('<int name="status">0</int>' in self.solr_admin.rename('coreX', 'core0'))

    def test_swap(self):
        self.assertTrue('<int name="status">0</int>' in self.solr_admin.swap('core0', 'core1'))
        self.assertTrue('<int name="status">0</int>' in self.solr_admin.swap('core1', 'core0'))

    def test_unload_create(self):
        # unload core0 without deleting data and then recreate it
        self.assertTrue('<int name="status">0</int>' in self.solr_admin.unload('core0'))
        self.assertTrue('<int name="status">0</int>' in self.solr_admin.create('core0'))

    def test_load(self):
        self.assertRaises(NotImplementedError, self.solr_admin.load, 'wheatley')
