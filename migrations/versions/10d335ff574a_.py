"""empty message

Revision ID: 10d335ff574a
Revises: 4cae3176daa5
Create Date: 2023-12-26 20:20:01.480565

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '10d335ff574a'
down_revision = '4cae3176daa5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=30),
               type_=sa.String(length=200),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.String(length=200),
               type_=mysql.VARCHAR(collation='utf8mb4_general_ci', length=30),
               existing_nullable=True)

    # ### end Alembic commands ###