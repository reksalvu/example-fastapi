"""add foreign-key to posts table

Revision ID: 094a7a072349
Revises: 65b5d4bbf9e0
Create Date: 2022-06-10 10:07:05.555440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '094a7a072349'
down_revision = '65b5d4bbf9e0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
