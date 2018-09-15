# This file is part of the stock_shipment_cashondelivery module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['Sale']


class Sale(metaclass=PoolMeta):
    __name__ = 'sale.sale'

    def create_shipment(self, shipment_type):
        pool = Pool()
        shipments = super(Sale, self).create_shipment(shipment_type)
        if shipment_type != 'out' or not shipments:
            return

        Config = pool.get('sale.configuration')
        ShipmentOut = pool.get('stock.shipment.out')
        config = Config(1)

        if self.payment_type in config.cashondelivery_payments:
            ShipmentOut.write(shipments, {
                'carrier_cashondelivery': True,
                })
        return shipments
