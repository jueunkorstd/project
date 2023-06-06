"""empty message

Revision ID: 028f31baf022
Revises: 66943afff1bd
Create Date: 2023-06-06 21:03:27.187018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '028f31baf022'
down_revision = '66943afff1bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['alarm.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answer')
    # ### end Alembic commands ###
