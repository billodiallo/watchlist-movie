"""Add UserMixin to the User class as an argument and add email property

Revision ID: 701bec8863b5
Revises: bf3f542ee9a5
Create Date: 2017-10-23 19:05:20.682139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '701bec8863b5'
down_revision = 'bf3f542ee9a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
