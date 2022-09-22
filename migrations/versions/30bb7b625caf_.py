"""empty message

Revision ID: 30bb7b625caf
Revises: 3ff7b215d687
Create Date: 2022-09-22 10:52:20.324025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "30bb7b625caf"
down_revision = "3ff7b215d687"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("is_admin", sa.Boolean(), nullable=True))

    from database import db
    from models import User

    u = User.query.filter(User.netid == "ntyp").first()
    u.is_admin = True
    db.commit()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "is_admin")
    # ### end Alembic commands ###
