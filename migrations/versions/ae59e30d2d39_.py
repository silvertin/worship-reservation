"""empty message

Revision ID: ae59e30d2d39
Revises: 80d5f0788559
Create Date: 2021-10-24 22:57:48.989917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae59e30d2d39'
down_revision = '80d5f0788559'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('worship_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('detail', sa.String(length=100), nullable=True),
    sa.Column('bgcolor', sa.String(length=7), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_worship_type'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('worship_type')
    # ### end Alembic commands ###