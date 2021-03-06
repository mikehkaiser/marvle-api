"""empty message

Revision ID: a64ff0053869
Revises: 244d67a4bad3
Create Date: 2021-08-08 22:10:03.078553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a64ff0053869'
down_revision = '244d67a4bad3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'name',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'name',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    # ### end Alembic commands ###
