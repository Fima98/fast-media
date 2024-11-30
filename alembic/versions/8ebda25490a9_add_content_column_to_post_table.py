"""add content column to post table

Revision ID: 8ebda25490a9
Revises: 17c3d87aa74b
Create Date: 2024-11-17 12:34:25.336345

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ebda25490a9'
down_revision: Union[str, None] = '17c3d87aa74b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
