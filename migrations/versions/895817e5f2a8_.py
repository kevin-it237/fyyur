"""empty message

Revision ID: 895817e5f2a8
Revises: 655aa0646b1d
Create Date: 2021-03-17 23:25:50.561668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '895817e5f2a8'
down_revision = '655aa0646b1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genres', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'genres')
    # ### end Alembic commands ###
