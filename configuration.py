# This file is part of the stock_shipment_cashondelivery module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields, ModelSQL, ModelView
from trytond.pool import PoolMeta

__all__ = ['ConfigurationSalePaymentType', 'Configuration']
__metaclass__ = PoolMeta


class ConfigurationSalePaymentType(ModelSQL, ModelView):
    'Configuration - Sale Payment Type'
    __name__ = 'sale.configuration-account.payment.type'
    _table = 'sale_configuration_account_payment_type_rel'
    sale_configuration = fields.Many2One('sale.configuration',
        'Sale Configuration', ondelete='CASCADE', select=True)
    payment_type = fields.Many2One('account.payment.type', 'Payment Type',
        ondelete='RESTRICT', select=True, required=True)


class Configuration:
    __name__ = 'sale.configuration'
    cashondelivery_payments = fields.Many2Many(
        'sale.configuration-account.payment.type', 'sale_configuration',
        'payment_type', 'Cash on Delivery Payment Types',
        domain=[('kind', '=', 'receivable')],
        )
