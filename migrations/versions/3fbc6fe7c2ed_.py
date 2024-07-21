"""empty message

Revision ID: 3fbc6fe7c2ed
Revises: 0073967f619f
Create Date: 2024-01-02 19:14:38.470690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fbc6fe7c2ed'
down_revision = '0073967f619f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('habit', schema=None) as batch_op:
        batch_op.add_column(sa.Column('completed', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('habit', schema=None) as batch_op:
        batch_op.drop_column('completed')

    # ### end Alembic commands ###
