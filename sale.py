# This file is part of the stock_shipment_cashondelivery module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'

    def create_shipment(self, shipment_type):
        shipments = super(Sale, self).create_shipment(shipment_type)
        Config = Pool().get('sale.configuration')
        config = Config(1)
        if shipment_type == 'out' and shipments:
            for payment_type in config.cashondelivery_payments:
                if self.payment_type == payment_type:
                    for shipment in shipments:
                        shipment.carrier_cashondelivery = True
                        shipment.save()
                    break
        return shipments
