"""empty message

Revision ID: 1662b99a587f
Revises: 57f66785aecf
Create Date: 2021-01-02 11:55:45.280004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1662b99a587f'
down_revision = '57f66785aecf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('admin', sa.Integer(), server_default='1', nullable=True))

    with op.batch_alter_table('worship', schema=None) as batch_op:
        batch_op.add_column(sa.Column('limit', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('worship', schema=None) as batch_op:
        batch_op.drop_column('limit')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('admin')

    # ### end Alembic commands ###
