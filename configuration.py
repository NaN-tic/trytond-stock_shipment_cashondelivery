# This file is part of the stock_shipment_cashondelivery module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields, ModelSQL, ModelView
from trytond.pool import PoolMeta
from trytond import backend

__all__ = ['ConfigurationSalePaymentType', 'Configuration']


class ConfigurationSalePaymentType(ModelSQL, ModelView):
    'Configuration - Sale Payment Type'
    __name__ = 'sale.configuration-sale.payment.type'
    _table = 'sale_configuration_sale_payment_type'
    sale_configuration = fields.Many2One('sale.configuration',
        'Sale Configuration', ondelete='CASCADE', select=True)
    payment_type = fields.Many2One('account.payment.type', 'Payment Type',
        ondelete='RESTRICT', select=True, required=True)

    @classmethod
    def __register__(cls, module_name):
        # Migration from 3.6: rename table
        old_table = 'sale_configuration_sale_payment_type_rel'
        new_table = 'sale_configuration_sale_payment_type'
        if backend.TableHandler.table_exist(old_table):
            backend.TableHandler.table_rename(old_table, new_table)

        super(ConfigurationSalePaymentType, cls).__register__(module_name)


class Configuration(metaclass=PoolMeta):
    __name__ = 'sale.configuration'
    cashondelivery_payments = fields.Many2Many(
        'sale.configuration-sale.payment.type', 'sale_configuration',
        'payment_type', 'Cash on Delivery Payment Types',
        domain=[('kind', '=', 'receivable')],
        )
