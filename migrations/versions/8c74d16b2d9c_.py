"""empty message

Revision ID: 8c74d16b2d9c
Revises: 
Create Date: 2020-10-10 20:28:52.433838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c74d16b2d9c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('infocontacto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('state', sa.Boolean(), nullable=True),
    sa.Column('plan', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('planes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('frecuencia', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rol', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rol')
    )
    op.create_table('edificios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_edificio', sa.String(length=120), nullable=False),
    sa.Column('direccion', sa.String(length=120), nullable=False),
    sa.Column('telefono', sa.String(length=12), nullable=False),
    sa.Column('correo', sa.String(length=120), nullable=False),
    sa.Column('numero_pisos', sa.Integer(), nullable=False),
    sa.Column('numero_departamentos', sa.Integer(), nullable=False),
    sa.Column('total_bodegas', sa.Integer(), nullable=False),
    sa.Column('total_estacionamientos', sa.Integer(), nullable=False),
    sa.Column('inicio_contratacion', sa.String(length=120), nullable=False),
    sa.Column('termino_contrato', sa.String(length=120), nullable=False),
    sa.Column('dia_vencimiento', sa.String(length=120), nullable=False),
    sa.Column('plan_id', sa.Integer(), nullable=False),
    sa.Column('archivoCSV', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['plan_id'], ['planes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bodegas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('total_superficie', sa.Integer(), nullable=False),
    sa.Column('cantidad_total', sa.Integer(), nullable=False),
    sa.Column('edificio_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['edificio_id'], ['edificios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('boletines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('asunto', sa.String(length=120), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('edificio_id', sa.Integer(), nullable=False),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['edificio_id'], ['edificios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('departamentos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('modelo', sa.String(length=120), nullable=False),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('interior', sa.Integer(), nullable=False),
    sa.Column('terraza', sa.Integer(), nullable=False),
    sa.Column('cantidad_total', sa.Integer(), nullable=False),
    sa.Column('edificio_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['edificio_id'], ['edificios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('estacionamientos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('total_superficie', sa.Integer(), nullable=False),
    sa.Column('cantidad_total', sa.Integer(), nullable=False),
    sa.Column('edificio_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['edificio_id'], ['edificios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('rol_id', sa.Integer(), nullable=False),
    sa.Column('edificio_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['edificio_id'], ['edificios.id'], ),
    sa.ForeignKeyConstraint(['rol_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('conserjes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('telefono', sa.String(length=120), nullable=False),
    sa.Column('turno', sa.String(length=120), nullable=False),
    sa.Column('avatar', sa.String(length=100), nullable=True),
    sa.Column('edificio_id', sa.Integer(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('state', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['edificio_id'], ['edificios.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('departamentosusuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero_departamento', sa.String(length=120), nullable=False),
    sa.Column('estado', sa.String(length=120), nullable=False),
    sa.Column('residente', sa.Integer(), nullable=True),
    sa.Column('propietario', sa.Integer(), nullable=True),
    sa.Column('bodega_id', sa.Integer(), nullable=True),
    sa.Column('estacionamiento_id', sa.Integer(), nullable=True),
    sa.Column('piso', sa.Integer(), nullable=True),
    sa.Column('edificio_id', sa.Integer(), nullable=False),
    sa.Column('modelo_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['edificio_id'], ['edificios.id'], ),
    sa.ForeignKeyConstraint(['modelo_id'], ['departamentos.id'], ),
    sa.ForeignKeyConstraint(['propietario'], ['users.id'], ),
    sa.ForeignKeyConstraint(['residente'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bodega_id'),
    sa.UniqueConstraint('estacionamiento_id')
    )
    op.create_table('gastoscomunes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('month', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('monto', sa.Integer(), nullable=False),
    sa.Column('departamento_id', sa.Integer(), nullable=False),
    sa.Column('edificio_id', sa.Integer(), nullable=False),
    sa.Column('estado', sa.String(length=250), nullable=True),
    sa.Column('pago', sa.String(length=250), nullable=True),
    sa.ForeignKeyConstraint(['departamento_id'], ['departamentosusuarios.id'], ),
    sa.ForeignKeyConstraint(['edificio_id'], ['edificios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('montostotales',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('month', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('monto', sa.Integer(), nullable=False),
    sa.Column('comprobante', sa.String(length=250), nullable=False),
    sa.Column('departamento_id', sa.Integer(), nullable=False),
    sa.Column('edificio_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['departamento_id'], ['departamentosusuarios.id'], ),
    sa.ForeignKeyConstraint(['edificio_id'], ['edificios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('paqueteria',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('departamento_id', sa.Integer(), nullable=False),
    sa.Column('edificio_id', sa.Integer(), nullable=False),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['departamento_id'], ['departamentosusuarios.id'], ),
    sa.ForeignKeyConstraint(['edificio_id'], ['edificios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('paqueteria')
    op.drop_table('montostotales')
    op.drop_table('gastoscomunes')
    op.drop_table('departamentosusuarios')
    op.drop_table('conserjes')
    op.drop_table('users')
    op.drop_table('estacionamientos')
    op.drop_table('departamentos')
    op.drop_table('boletines')
    op.drop_table('bodegas')
    op.drop_table('edificios')
    op.drop_table('roles')
    op.drop_table('planes')
    op.drop_table('infocontacto')
    # ### end Alembic commands ###