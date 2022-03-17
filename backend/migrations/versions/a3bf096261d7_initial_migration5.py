"""Initial Migration5

Revision ID: a3bf096261d7
Revises: fa28f5ced5b5
Create Date: 2022-03-16 22:24:24.964528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3bf096261d7'
down_revision = 'fa28f5ced5b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'about')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###