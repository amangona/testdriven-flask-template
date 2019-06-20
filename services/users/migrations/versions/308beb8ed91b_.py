"""empty message

Revision ID: 308beb8ed91b
Revises: a82652a753b1
Create Date: 2019-06-19 20:29:08.210129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '308beb8ed91b'
down_revision = 'a82652a753b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
