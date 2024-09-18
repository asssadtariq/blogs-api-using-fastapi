"""blog category model added

Revision ID: cdd8494a5f6f
Revises: 3f83e18552a0
Create Date: 2024-09-18 11:40:35.865248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdd8494a5f6f'
down_revision: Union[str, None] = '3f83e18552a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_category',
    sa.Column('blog_catg_id', sa.UUID(), nullable=False),
    sa.Column('blog_catg_name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('created_on', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('last_modified', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('blog_catg_id')
    )
    op.create_index(op.f('ix_blog_category_blog_catg_id'), 'blog_category', ['blog_catg_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_blog_category_blog_catg_id'), table_name='blog_category')
    op.drop_table('blog_category')
    # ### end Alembic commands ###
