"""'added'

Revision ID: fa2bd0ad2eac
Revises: 872eed2e47c5
Create Date: 2020-06-05 14:04:36.240283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa2bd0ad2eac'
down_revision = '872eed2e47c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admins', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dp_fname', sa.String(length=180), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admins', schema=None) as batch_op:
        batch_op.drop_column('dp_fname')

    # ### end Alembic commands ###