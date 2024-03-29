"""empty message

Revision ID: 00e3cb0de685
Revises: ae59e30d2d39
Create Date: 2021-10-25 00:19:55.151704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00e3cb0de685'
down_revision = 'ae59e30d2d39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('worshiptype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('detail', sa.String(length=100), nullable=True),
    sa.Column('bgcolor', sa.String(length=7), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_worshiptype'))
    )
    op.drop_table('worship_type')
    with op.batch_alter_table('worship', schema=None) as batch_op:
        batch_op.add_column(sa.Column('worshiptype_id', sa.Integer(), server_default='1', nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_worship_worshiptype_id_worshiptype'), 'worshiptype', ['worshiptype_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('worship', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_worship_worshiptype_id_worshiptype'), type_='foreignkey')
        batch_op.drop_column('worshiptype_id')

    op.create_table('worship_type',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('detail', sa.VARCHAR(length=100), nullable=True),
    sa.Column('bgcolor', sa.VARCHAR(length=7), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_worship_type')
    )
    op.drop_table('worshiptype')
    # ### end Alembic commands ###
