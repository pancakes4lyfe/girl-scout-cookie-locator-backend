"""empty message

Revision ID: 4da685e23675
Revises: 5ed03e0c9ab8
Create Date: 2021-08-10 10:22:11.265762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4da685e23675'
down_revision = '5ed03e0c9ab8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pins', sa.Column('pinned_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pins', 'pinned_at')
    # ### end Alembic commands ###