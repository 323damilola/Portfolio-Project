"""empty message

Revision ID: 34f0fddcd77f
Revises: fa46aa8ebf45
Create Date: 2023-12-28 15:19:36.776841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34f0fddcd77f'
down_revision = 'fa46aa8ebf45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointments',
    sa.Column('appointment_id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('which_customer', sa.Integer(), nullable=False),
    sa.Column('which_service', sa.Integer(), nullable=False),
    sa.Column('appointment_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['which_customer'], ['customers.customer_id'], ),
    sa.ForeignKeyConstraint(['which_service'], ['services.service_id'], ),
    sa.PrimaryKeyConstraint('appointment_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appointments')
    # ### end Alembic commands ###