# This file is part of the stock_shipment_cashondelivery module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from decimal import Decimal
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval, Equal
from trytond.modules.currency.fields import Monetary

__all__ = ['ShipmentOut']


class ShipmentOut(metaclass=PoolMeta):
    __name__ = 'stock.shipment.out'
    carrier_cashondelivery = fields.Boolean('Carrier Cash OnDelivery',
        states={
            'readonly': Equal(Eval('state'), 'done'),
            'invisible': ~Eval('carrier'),
        }, help='Paid package when carrier delivery')
    carrier_cashondelivery_total = Monetary(
        'Carrier Cash OnDelivery Total', currency='currency', digits='currency',
        states={
            'invisible': ~Eval('carrier_cashondelivery'),
            'readonly': ~Eval('state').in_(['draft', 'waiting', 'assigned',
                'packed']),
        }, depends=['state'])
    carrier_cashondelivery_price = fields.Function(Monetary(
        'Carrier Cash OnDelivery Price', currency='currency', digits='currency',
        states={
            'invisible': ~Eval('carrier_cashondelivery'),
            'readonly': ~Eval('state').in_(['draft', 'waiting', 'assigned',
                'packed']),
        }),
        'on_change_with_carrier_cashondelivery_price')
    carrier_sale_price_total = fields.Function(Monetary('Sale Total',
        currency='currency', digits='currency',
        states={
            'invisible': ~Eval('carrier_cashondelivery'),
        }),
        'on_change_with_carrier_sale_price_total')
    carrier_price_total = fields.Function(Monetary('Price Total',
        currency='currency', digits='currency',
        states={
            'invisible': ~Eval('carrier_cashondelivery'),
        }),
        'on_change_with_carrier_price_total')

    @classmethod
    def __setup__(cls):
        super(ShipmentOut, cls).__setup__()
        if hasattr(ShipmentOut, 'origin_cache'):
            cls.on_change_with_carrier_sale_price_total.depends.add('origin_cache')
        if hasattr(ShipmentOut, 'origin'):
            cls.on_change_with_carrier_sale_price_total.depends.add('origin')

    def get_carrier_price_total(self):
        'Return the total price shipment'
        if self.carrier_cashondelivery_total:
            price = self.carrier_cashondelivery_total
        elif self.carrier_sale_price_total:
            price = self.carrier_sale_price_total
        else:
            price = self.total_amount
        return price

    @fields.depends('carrier_cashondelivery_total', 'carrier_sale_price_total',
        'total_amount')
    def on_change_with_carrier_price_total(self, name=None):
        return self.get_carrier_price_total()

    @fields.depends('carrier_cashondelivery')
    def on_change_with_carrier_sale_price_total(self, name=None):
        'Get Sale Total Amount if shipment origin is a sale'
        price = Decimal(0)
        origin = None
        if hasattr(self, 'origin_cache') and self.origin_cache:
            origin = self.origin_cache
        elif hasattr(self, 'origin'):
            origin = self.origin
        if origin and origin.__name__ == 'sale.sale':
            price = origin.total_amount
        return price

    @fields.depends('carrier_cashondelivery', 'carrier_cashondelivery_total',
        'carrier_sale_price_total', 'total_amount')
    def on_change_with_carrier_cashondelivery_price(self, name=None):
        'Get Price Cash on Delivery'
        if not self.carrier_cashondelivery:
            return
        if self.carrier_cashondelivery_total:
            return self.carrier_cashondelivery_total
        elif self.carrier_sale_price_total:
            return self.carrier_sale_price_total
        return self.total_amount

    @classmethod
    def view_attributes(cls):
        return super(ShipmentOut, cls).view_attributes() + [
            ('//page[@id="carrier-delivery"]', 'states', {
                    'invisible': ~Eval('carrier'),
                    })]
