"""create account events table

Revision ID: 0baca0d41eb0
Revises:
Create Date: 2020-03-12 23:35:37.571713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0baca0d41eb0"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "events",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("event", sa.Unicode(200)),
    )


def downgrade():
    op.drop_table("account")
