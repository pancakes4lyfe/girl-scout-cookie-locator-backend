"""empty message

Revision ID: 91f651fc3cbf
Revises: 
Create Date: 2021-08-18 02:01:47.413950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91f651fc3cbf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pins',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('lat_lon', sa.String(), nullable=True),
    sa.Column('pinned_at', sa.DateTime(), nullable=True),
    sa.Column('hours', sa.String(), nullable=True),
    sa.Column('cookies_available', sa.String(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.Column('upvote_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pins')
    # ### end Alembic commands ###