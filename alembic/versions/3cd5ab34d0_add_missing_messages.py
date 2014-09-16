"""add missing messages

Revision ID: 3cd5ab34d0
Revises: 25450d45211
Create Date: 2014-09-14 22:01:10.695008

"""

# revision identifiers, used by Alembic.
revision = '3cd5ab34d0'
down_revision = '25450d45211'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('misses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_name', sa.String(), nullable=True),
    sa.Column('message', sa.BigInteger(), nullable=True),
    sa.Column('attempts', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_misses_group_name'), 'misses', ['group_name'], unique=False)
    op.create_index(op.f('ix_misses_message'), 'misses', ['message'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_misses_message'), table_name='misses')
    op.drop_index(op.f('ix_misses_group_name'), table_name='misses')
    op.drop_table('misses')
    ### end Alembic commands ###
