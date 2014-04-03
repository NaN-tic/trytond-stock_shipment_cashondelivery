# This file is part of the stock_shipment_cashondelivery module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from configuration import *
from .shipment import *
from .sale import *


def register():
    Pool.register(
        ConfigurationSalePaymentType,
        Configuration,
        ShipmentOut,
        Sale,
        module='stock_shipment_cashondelivery', type_='model')
