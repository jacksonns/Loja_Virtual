"""Initial database

Revision ID: 8847cca1ad27
Revises: 9a6b551b0ff1
Create Date: 2022-06-25 15:18:49.625594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8847cca1ad27'
down_revision = '9a6b551b0ff1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('budget_reais', sa.Integer(), nullable=False),
    sa.Column('budget_cents', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('seller_id', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('price_reais', sa.Integer(), nullable=False),
    sa.Column('price_cents', sa.Integer(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('sale', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item_list',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('item_id', sa.String(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.PrimaryKeyConstraint('id', 'item_id')
    )
    op.create_table('cart',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('item_list', sa.String(), nullable=True),
    sa.Column('expiration_date', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['item_list'], ['item_list.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('session',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('expiration_date', sa.String(), nullable=True),
    sa.Column('cart_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('session')
    op.drop_table('cart')
    op.drop_table('item_list')
    op.drop_table('item')
    op.drop_table('user')
    # ### end Alembic commands ###