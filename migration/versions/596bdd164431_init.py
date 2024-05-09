"""'init'

Revision ID: 596bdd164431
Revises: 
Create Date: 2024-05-08 14:16:01.242393

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '596bdd164431'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
                    sa.Column('todo_id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(), nullable=True),
                    sa.Column('description', sa.Text(), nullable=False),
                    sa.Column('completed', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('todo_id')
                    )
    op.create_index(op.f('ix_todo_todo_id'), 'todo', ['todo_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_todo_todo_id'), table_name='todo')
    op.drop_table('todo')
    # ### end Alembic commands ###