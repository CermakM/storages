"""Add InspectionRun inspection_batch_order attribute.

Revision ID: 5969d4fee836
Revises: b330ba2154f4
Create Date: 2020-02-19 09:58:46.286226+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5969d4fee836"
down_revision = "b330ba2154f4"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "inspection_run",
        sa.Column("inspection_batch_order", sa.Integer(), nullable=False, server_default="1")
    )
    op.alter_column(
        "inspection_run",
        sa.Column("inspection_batch_order", sa.Integer(), server_default=None)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("inspection_run", "inspection_batch_order")
    # ### end Alembic commands ###