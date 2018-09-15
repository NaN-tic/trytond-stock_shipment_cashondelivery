# This file is part of the stock_shipment_cashondelivery module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import configuration
from . import shipment
from . import sale


def register():
    Pool.register(
        configuration.ConfigurationSalePaymentType,
        configuration.Configuration,
        shipment.ShipmentOut,
        sale.Sale,
        module='stock_shipment_cashondelivery', type_='model')
