"""empty message

Revision ID: 6180e1a3dea2
Revises: 28f696c0ef88
Create Date: 2022-06-22 20:58:25.767258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6180e1a3dea2'
down_revision = '28f696c0ef88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.ARRAY(sa.String()), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###
