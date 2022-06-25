"""Testing

Revision ID: fca238ba7670
Revises: b01546ccca76
Create Date: 2022-06-25 14:00:57.180342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fca238ba7670'
down_revision = 'b01546ccca76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item', 'stock')
    op.drop_column('item', 'price_reais')
    op.drop_column('item', 'price_cents')
    op.drop_column('item', 'sale')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('sale', sa.INTEGER(), nullable=True))
    op.add_column('item', sa.Column('price_cents', sa.INTEGER(), nullable=False))
    op.add_column('item', sa.Column('price_reais', sa.INTEGER(), nullable=False))
    op.add_column('item', sa.Column('stock', sa.INTEGER(), nullable=False))
    # ### end Alembic commands ###
