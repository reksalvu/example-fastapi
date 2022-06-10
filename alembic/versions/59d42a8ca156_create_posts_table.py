"""create posts table

Revision ID: 59d42a8ca156
Revises: 
Create Date: 2022-06-10 09:38:52.680383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59d42a8ca156'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(),nullable=False,primary_key=True), 
                    sa.Column('title', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
