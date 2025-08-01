"""bringing restaurant's name to product table

Revision ID: 2eebefc193e6
Revises: 1f01f0ade401
Create Date: 2025-07-22 10:45:12.048289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2eebefc193e6'
down_revision = '1f01f0ade401'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orden', schema=None) as batch_op:
        batch_op.alter_column('precio_total',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    with op.batch_alter_table('ordenDetallePersonalizacion', schema=None) as batch_op:
        batch_op.alter_column('ajuste_precio',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    with op.batch_alter_table('productos', schema=None) as batch_op:
        batch_op.alter_column('precio',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    with op.batch_alter_table('subproductos', schema=None) as batch_op:
        batch_op.alter_column('precio',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)
        batch_op.alter_column('valor_adicion',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)
        batch_op.alter_column('valor_remocion',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('subproductos', schema=None) as batch_op:
        batch_op.alter_column('valor_remocion',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('valor_adicion',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('precio',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('productos', schema=None) as batch_op:
        batch_op.alter_column('precio',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('ordenDetallePersonalizacion', schema=None) as batch_op:
        batch_op.alter_column('ajuste_precio',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('orden', schema=None) as batch_op:
        batch_op.alter_column('precio_total',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
