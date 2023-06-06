"""empty message

Revision ID: 10d6b9630005
Revises: 
Create Date: 2023-06-06 16:40:43.894046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10d6b9630005'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alarm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('alarmName', sa.String(length=200), nullable=False),
    sa.Column('alarmTime', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alarm')
    # ### end Alembic commands ###