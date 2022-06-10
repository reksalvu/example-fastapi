"""add content column to posts table

Revision ID: 18a4eff2c413
Revises: 59d42a8ca156
Create Date: 2022-06-10 09:50:00.203702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18a4eff2c413'
down_revision = '59d42a8ca156'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
