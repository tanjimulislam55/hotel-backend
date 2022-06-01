"""room check_in, check_out, is_booked

Revision ID: 952fcafcf1e1
Revises: 245dc034505e
Create Date: 2022-06-01 12:48:07.399676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '952fcafcf1e1'
down_revision = '245dc034505e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rooms', sa.Column('check_in', sa.DateTime(), nullable=True))
    op.add_column('rooms', sa.Column('check_out', sa.DateTime(), nullable=True))
    op.add_column('rooms', sa.Column('is_booked', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rooms', 'is_booked')
    op.drop_column('rooms', 'check_out')
    op.drop_column('rooms', 'check_in')
    # ### end Alembic commands ###
