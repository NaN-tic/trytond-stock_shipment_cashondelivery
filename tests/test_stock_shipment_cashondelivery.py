# This file is part of the stock_shipment_cashondelivery module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockShipmentCashondeliveryTestCase(ModuleTestCase):
    'Test Stock Shipment Cashondelivery module'
    module = 'stock_shipment_cashondelivery'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockShipmentCashondeliveryTestCase))
    return suite