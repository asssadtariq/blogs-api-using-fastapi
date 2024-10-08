"""Initial migration

Revision ID: bd145487e8a1
Revises: 
Create Date: 2024-09-16 15:50:09.428350

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd145487e8a1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=False),
    sa.Column('email', sa.VARCHAR(length=64), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('password', sa.VARCHAR(length=32), nullable=True),
    sa.Column('dob', sa.DATE(), nullable=False),
    sa.Column('ver_key', sa.Text(), nullable=True),
    sa.Column('is_verified', sa.BOOLEAN(), nullable=True),
    sa.Column('is_active', sa.VARCHAR(length=32), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('last_modified', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('profile_img_path', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_user_id'), 'user', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
