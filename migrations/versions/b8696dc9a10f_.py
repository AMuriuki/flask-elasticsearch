"""empty message

Revision ID: b8696dc9a10f
Revises: 1b7c266cebb1
Create Date: 2022-12-22 10:27:38.987740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8696dc9a10f'
down_revision = '1b7c266cebb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('product_collection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['product_category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('product_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['product_category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_category', sa.Integer(), nullable=True),
    sa.Column('product_type', sa.Integer(), nullable=True),
    sa.Column('product_collection', sa.Integer(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('published_on', sa.DateTime(), nullable=True),
    sa.Column('rating', sa.String(length=120), nullable=True),
    sa.Column('is_draft', sa.Boolean(), nullable=True),
    sa.Column('is_published', sa.Boolean(), nullable=True),
    sa.Column('in_stock', sa.String(length=120), nullable=True),
    sa.Column('slug', sa.Text(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('original_price', sa.Float(), nullable=True),
    sa.Column('discount', sa.Float(), nullable=True),
    sa.Column('brand', sa.String(length=120), nullable=True),
    sa.Column('store', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['product_category'], ['product_category.id'], ),
    sa.ForeignKeyConstraint(['product_collection'], ['product_collection.id'], ),
    sa.ForeignKeyConstraint(['product_type'], ['product_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('product_type')
    op.drop_table('product_collection')
    op.drop_table('product_category')
    # ### end Alembic commands ###
