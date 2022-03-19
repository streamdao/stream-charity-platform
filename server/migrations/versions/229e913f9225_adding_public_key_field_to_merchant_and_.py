"""Adding public_key field to Merchant and Recipient

Revision ID: 229e913f9225
Revises: 78f183308c16
Create Date: 2022-02-26 14:44:55.779802

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '229e913f9225'
down_revision = '78f183308c16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('merchant', schema=None) as batch_op:
        batch_op.add_column(sa.Column('public_key', sa.String(length=64), nullable=True))
        batch_op.drop_constraint('merchant_merchant_id_key', type_='unique')
        batch_op.drop_column('merchant_id')

    with op.batch_alter_table('recipient', schema=None) as batch_op:
        batch_op.add_column(sa.Column('public_key', sa.String(length=64), nullable=True))
        batch_op.drop_constraint('recipient_recipient_id_key', type_='unique')
        batch_op.drop_column('recipient_id')
        batch_op.drop_column('spl_wallet_address')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipient', schema=None) as batch_op:
        batch_op.add_column(sa.Column('spl_wallet_address', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('recipient_id', postgresql.UUID(), autoincrement=False, nullable=True))
        batch_op.create_unique_constraint('recipient_recipient_id_key', ['recipient_id'])
        batch_op.drop_column('public_key')

    with op.batch_alter_table('merchant', schema=None) as batch_op:
        batch_op.add_column(sa.Column('merchant_id', postgresql.UUID(), autoincrement=False, nullable=True))
        batch_op.create_unique_constraint('merchant_merchant_id_key', ['merchant_id'])
        batch_op.drop_column('public_key')

    # ### end Alembic commands ###
