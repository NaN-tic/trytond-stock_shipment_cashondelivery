# This file is part of the stock_shipment_cashondelivery module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'

    def _get_shipment_sale(self, Shipment, key):
        config = Pool().get('sale.configuration')(1)

        shipment = super(Sale, self)._get_shipment_sale(Shipment, key)

        if (Shipment.__name__ == 'stock.shipment.out'
                and self.payment_type in config.cashondelivery_payments):
            shipment.carrier_cashondelivery = True
        return shipment
