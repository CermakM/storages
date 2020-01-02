"""Optimize marker evaluation result query for adviser

Revision ID: fd7771734460
Revises: f00fc22d1589
Create Date: 2020-01-02 06:18:52.279747+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd7771734460'
down_revision = 'f00fc22d1589'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('depends_on', 'marker_evaluation_result',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('depends_on', 'marker_evaluation_result',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
