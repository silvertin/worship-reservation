"""empty message

Revision ID: 80d5f0788559
Revises: 7a007f351252
Create Date: 2021-01-11 12:07:09.049969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80d5f0788559'
down_revision = '7a007f351252'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('seat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user', sa.String(length=50), nullable=True))
        batch_op.drop_constraint('fk_seat_user_id_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('seat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_seat_user_id_user', 'user', ['user_id'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('user')

    # ### end Alembic commands ###
