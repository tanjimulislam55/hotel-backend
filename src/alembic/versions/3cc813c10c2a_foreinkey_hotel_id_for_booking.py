"""foreinkey hotel_id for booking

Revision ID: 3cc813c10c2a
Revises: 672c541730d8
Create Date: 2022-06-07 09:16:00.804942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cc813c10c2a'
down_revision = '672c541730d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('booked_by_users', sa.Column('hotel_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'booked_by_users', 'hotels', ['hotel_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'booked_by_users', type_='foreignkey')
    op.drop_column('booked_by_users', 'hotel_id')
    # ### end Alembic commands ###
