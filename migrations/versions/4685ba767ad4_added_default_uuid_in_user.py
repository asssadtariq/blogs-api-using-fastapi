
from typing import Union, Sequence
from alembic import op
import sqlalchemy as sa
import uuid  # Import uuid for generating defaults

# revision identifiers, used by Alembic.
revision: str = "4685ba767ad4"
down_revision: Union[str, None] = "2144b82daad8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Set a default value for the user_id column
    op.alter_column(
        table_name="user",
        column_name="user_id",
        server_default=sa.text(
            "gen_random_uuid()"
        ),  # PostgreSQL-specific function for UUIDs
    )


def downgrade() -> None:
    # Remove the default value for the user_id column
    op.alter_column(table_name="user", column_name="user_id", server_default=None)
