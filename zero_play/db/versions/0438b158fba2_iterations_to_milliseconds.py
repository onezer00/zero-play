"""iterations to milliseconds

Revision ID: 0438b158fba2
Revises: 62b4dd973a0f
Create Date: 2023-05-16 20:43:30.218334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0438b158fba2'
down_revision = '62b4dd973a0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('players', sa.Column('milliseconds', sa.Integer(), nullable=True))
    # Dropping iterations didn't work, so we'll leave it unused.
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('players', 'milliseconds')
    # ### end Alembic commands ###