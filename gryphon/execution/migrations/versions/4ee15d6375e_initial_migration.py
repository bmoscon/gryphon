"""Initial Migration

Revision ID: 4ee15d6375e
Revises: None
Create Date: 2019-03-18 15:38:42.643916

"""

# revision identifiers, used by Alembic.
revision = '4ee15d6375e'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

from gryphon.lib.models.exchange import JSONEncodedMoneyDict
sa.JSONEncodedMoneyDict = JSONEncodedMoneyDict

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('unique_id', sa.Unicode(length=64), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('time_created', sa.DateTime(), nullable=False),
    sa.Column('exchange_name', sa.Unicode(length=256), nullable=False),
    sa.Column('event_type', sa.Unicode(length=256), nullable=False),
    sa.Column('data', sa.UnicodeText(length=2147483648), nullable=True),
    sa.PrimaryKeyConstraint('event_id')
    )
    op.create_table('exchange',
    sa.Column('exchange_id', sa.Integer(), nullable=False),
    sa.Column('unique_id', sa.Unicode(length=64), nullable=False),
    sa.Column('name', sa.Unicode(length=64), nullable=False),
    sa.Column('position', sa.JSONEncodedMoneyDict(), nullable=True),
    sa.Column('target', sa.JSONEncodedMoneyDict(), nullable=True),
    sa.Column('balance', sa.JSONEncodedMoneyDict(), nullable=True),
    sa.Column('multi_position_cache', sa.Numeric(precision=24, scale=14), nullable=True),
    sa.PrimaryKeyConstraint('exchange_id')
    )
    op.create_table('flag',
    sa.Column('key', sa.Unicode(length=64), nullable=False),
    sa.Column('value', sa.UnicodeText(length=2147483648), nullable=True),
    sa.PrimaryKeyConstraint('key')
    )
    op.create_table('liability',
    sa.Column('liability_id', sa.Integer(), nullable=False),
    sa.Column('unique_id', sa.Unicode(length=64), nullable=False),
    sa.Column('time_created', sa.DateTime(), nullable=False),
    sa.Column('amount', sa.Numeric(precision=24, scale=14), nullable=True),
    sa.Column('amount_currency', sa.Unicode(length=3), nullable=True),
    sa.Column('liability_type', sa.Unicode(length=64), nullable=True),
    sa.Column('entity_name', sa.Unicode(length=128), nullable=False),
    sa.Column('time_started', sa.DateTime(), nullable=True),
    sa.Column('time_repayed', sa.DateTime(), nullable=True),
    sa.Column('details', sa.UnicodeText(length=2147483648), nullable=True),
    sa.PrimaryKeyConstraint('liability_id')
    )
    op.create_table('order',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Unicode(length=32), nullable=False),
    sa.Column('order_type', sa.Unicode(length=64), nullable=True),
    sa.Column('unique_id', sa.Unicode(length=64), nullable=False),
    sa.Column('exchange_order_id', sa.Unicode(length=64), nullable=True),
    sa.Column('actor', sa.Unicode(length=64), nullable=True),
    sa.Column('exchange_rate', sa.Numeric(precision=20, scale=10), nullable=True),
    sa.Column('time_created', sa.DateTime(), nullable=False),
    sa.Column('time_executed', sa.DateTime(), nullable=True),
    sa.Column('exchange_name', sa.Unicode(length=64), nullable=True),
    sa.Column('price', sa.Numeric(precision=20, scale=10), nullable=True),
    sa.Column('price_currency', sa.Unicode(length=64), nullable=True),
    sa.Column('volume', sa.Numeric(precision=20, scale=10), nullable=True),
    sa.Column('volume_currency', sa.Unicode(length=64), nullable=True),
    sa.Column('fundamental_value', sa.Numeric(precision=20, scale=10), nullable=True),
    sa.Column('fundamental_value_currency', sa.Unicode(length=3), nullable=True),
    sa.Column('competitiveness', sa.Numeric(precision=20, scale=10), nullable=True),
    sa.Column('competitiveness_currency', sa.Unicode(length=3), nullable=True),
    sa.Column('spread', sa.Numeric(precision=20, scale=10), nullable=True),
    sa.Column('spread_currency', sa.Unicode(length=3), nullable=True),
    sa.PrimaryKeyConstraint('order_id')
    )
    op.create_table('result',
    sa.Column('result_id', sa.Integer(), nullable=False),
    sa.Column('ticks', sa.Integer(), nullable=False),
    sa.Column('unique_id', sa.Unicode(length=64), nullable=False),
    sa.Column('algorithm', sa.Unicode(length=64), nullable=False),
    sa.Column('batch', sa.Unicode(length=64), nullable=False),
    sa.Column('trading_volume', sa.Numeric(precision=20, scale=10), nullable=True),
    sa.Column('usd', sa.Numeric(precision=20, scale=10), nullable=True),
    sa.Column('btc', sa.Numeric(precision=20, scale=10), nullable=True),
    sa.Column('time_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('result_id')
    )
    op.create_table('datum',
    sa.Column('unique_id', sa.Unicode(length=64), nullable=False),
    sa.Column('datum_id', sa.Integer(), nullable=False),
    sa.Column('time_created', sa.DateTime(), nullable=False),
    sa.Column('datum_type', sa.Unicode(length=256), nullable=False),
    sa.Column('numeric_value', sa.Numeric(precision=20, scale=10), nullable=True),
    sa.Column('string_value', sa.Unicode(length=256), nullable=True),
    sa.Column('meta_data', sa.UnicodeText(length=2147483648), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.order_id'], ),
    sa.PrimaryKeyConstraint('datum_id')
    )
    op.create_table('result_trade',
    sa.Column('trade_id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Numeric(precision=20, scale=10), nullable=True),
    sa.Column('price_currency', sa.Unicode(length=3), nullable=True),
    sa.Column('volume', sa.Numeric(precision=20, scale=10), nullable=True),
    sa.Column('volume_currency', sa.Unicode(length=3), nullable=True),
    sa.Column('tick', sa.Integer(), nullable=True),
    sa.Column('user_trade', sa.Unicode(length=64), nullable=True),
    sa.Column('result_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['result_id'], ['result.result_id'], ),
    sa.PrimaryKeyConstraint('trade_id')
    )
    op.create_table('transaction',
    sa.Column('transaction_id', sa.Integer(), nullable=False),
    sa.Column('transaction_type', sa.Unicode(length=64), nullable=True),
    sa.Column('transaction_status', sa.Unicode(length=64), nullable=True),
    sa.Column('unique_id', sa.Unicode(length=64), nullable=False),
    sa.Column('time_created', sa.DateTime(), nullable=False),
    sa.Column('time_completed', sa.DateTime(), nullable=True),
    sa.Column('amount', sa.Numeric(precision=24, scale=14), nullable=True),
    sa.Column('amount_currency', sa.Unicode(length=3), nullable=True),
    sa.Column('fee', sa.Numeric(precision=24, scale=14), nullable=True),
    sa.Column('fee_currency', sa.Unicode(length=3), nullable=True),
    sa.Column('transaction_details', sa.UnicodeText(length=2147483648), nullable=True),
    sa.Column('exchange_id', sa.Integer(), nullable=True),
    sa.Column('fee_buyback_transaction_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['exchange_id'], ['exchange.exchange_id'], ),
    sa.ForeignKeyConstraint(['fee_buyback_transaction_id'], ['transaction.transaction_id'], ),
    sa.PrimaryKeyConstraint('transaction_id')
    )
    op.create_table('trade',
    sa.Column('trade_id', sa.Integer(), nullable=False),
    sa.Column('trade_type', sa.Unicode(length=64), nullable=True),
    sa.Column('unique_id', sa.Unicode(length=64), nullable=False),
    sa.Column('exchange_trade_id', sa.Unicode(length=64), nullable=True),
    sa.Column('time_created', sa.DateTime(), nullable=False),
    sa.Column('fee', sa.Numeric(precision=24, scale=14), nullable=True),
    sa.Column('fee_currency', sa.Unicode(length=3), nullable=True),
    sa.Column('price', sa.Numeric(precision=24, scale=14), nullable=True),
    sa.Column('price_currency', sa.Unicode(length=3), nullable=True),
    sa.Column('volume', sa.Numeric(precision=24, scale=14), nullable=True),
    sa.Column('volume_currency', sa.Unicode(length=3), nullable=True),
    sa.Column('meta_data', sa.UnicodeText(length=2147483648), nullable=True),
    sa.Column('fee_buyback_transaction_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fee_buyback_transaction_id'], ['transaction.transaction_id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.order_id'], ),
    sa.PrimaryKeyConstraint('trade_id')
    )

    # Indices.
    op.create_index('idx_exchange_order_id_exchange_name', 'order', ['exchange_order_id', 'exchange_name'])
    op.create_index('idx_status', 'order', ['status'])
    op.create_index('time_created', 'order', ['time_created'])
    op.create_index('exchange_name', 'order', ['exchange_name'])

    op.create_index('time_created', 'datum', ['time_created'])

    op.create_index('time_created', 'event', ['time_created'])

    op.create_index('time_created', 'trade', ['time_created'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trade')
    op.drop_table('transaction')
    op.drop_table('result_trade')
    op.drop_table('datum')
    op.drop_table('result')
    op.drop_table('order')
    op.drop_table('liability')
    op.drop_table('flag')
    op.drop_table('exchange')
    op.drop_table('event')
    ### end Alembic commands ###