#!/usr/bin/env python
# This file is part of the stock_shipment_cashondelivery module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.tests.test_tryton import test_depends, test_view
import os
import sys
import trytond.tests.test_tryton
import unittest
DIR = os.path.abspath(os.path.normpath(os.path.join(__file__,
    '..', '..', '..', '..', '..', 'trytond')))
if os.path.isdir(DIR):
    sys.path.insert(0, os.path.dirname(DIR))


class StockShipmentCashondeliveryTestCase(unittest.TestCase):
    '''
    Test Stock Shipment Cashondelivery module.
    '''

    def setUp(self):
        trytond.tests.test_tryton.install_module(
            'stock_shipment_cashondelivery')

    def test0005views(self):
        '''
        Test views.
        '''
        test_view('stock_shipment_cashondelivery')

    def test0006depends(self):
        '''
        Test depends.
        '''
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockShipmentCashondeliveryTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
