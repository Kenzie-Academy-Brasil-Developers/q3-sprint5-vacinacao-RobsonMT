"""create module VaccineCard

Revision ID: 057adbd86aeb
Revises: 
Create Date: 2022-04-09 15:30:37.132110

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "057adbd86aeb"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "vaccine_cards",
        sa.Column("cpf", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("first_shot_date", sa.DateTime(), nullable=False),
        sa.Column("second_shot_date", sa.DateTime(), nullable=False),
        sa.Column("vaccine_name", sa.String(), nullable=False),
        sa.Column("health_unit_name", sa.String(), nullable=True),
        sa.CheckConstraint('length("cpf") = 11', name="check_cpf"),
        sa.PrimaryKeyConstraint("cpf"),
        sa.UniqueConstraint("cpf"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("vaccine_cards")
    # ### end Alembic commands ###
