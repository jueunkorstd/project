"""empty message

Revision ID: 850991f24ec5
Revises: 028f31baf022
Create Date: 2023-06-06 22:00:07.801151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '850991f24ec5'
down_revision = '028f31baf022'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('alarm_id', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'answer', type_='foreignkey')
    op.create_foreign_key(None, 'answer', 'alarm', ['alarm_id'], ['id'], ondelete='CASCADE')
    op.drop_column('answer', 'question_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('question_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'answer', type_='foreignkey')
    op.create_foreign_key(None, 'answer', 'alarm', ['question_id'], ['id'], ondelete='CASCADE')
    op.drop_column('answer', 'alarm_id')
    # ### end Alembic commands ###
