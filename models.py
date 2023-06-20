from sqlalchemy import Float, Boolean, Column, Integer, String, DateTime

# from .database import Base
from database import Base

class FullContratoModel(Base):
    __tablename__ = "contratos_full"

    id = Column(Integer, primary_key=True, index=True)
    nit_entidad = Column(Integer)
    nombre_entidad = Column(String)
    departamento = Column(String)
    ciudad = Column(String)
    orden = Column(String)
    sector = Column(String)
    rama = Column(String)
    entidad_centralizada = Column(String)
    estado_contrato = Column(String)
    descripcion_del_proceso = Column(String)
    tipo_de_contrato = Column(String)
    modalidad_de_contratacion = Column(String)
    justificacion_modalidad_de = Column(String)
    fecha_de_firma = Column(DateTime)
    fecha_de_inicio_del_contrato = Column(DateTime)
    fecha_de_fin_del_contrato = Column(DateTime)
    condiciones_de_entrega = Column(String)
    proveedor_adjudicado = Column(String)
    es_pyme = Column(String)
    obligaci_n_ambiental = Column(String)
    valor_del_contrato = Column(Float)
    valor_pendiente_de_pago = Column(Float)
    valor_pagado = Column(Float)
    valor_pendiente_de_ejecucion = Column(Float)
    espostconflicto = Column(String)
    urlproceso = Column(String)
    destino_gasto = Column(String)
    nombre_representante_legal = Column(String)
    identificaci_n_representante_legal = Column(String)
    g_nero_representante_legal = Column(String)
    ultima_actualizacion = Column(DateTime)
    objeto_del_contrato = Column(String)
    fecha_de_inicio_de_ejecucion = Column(DateTime)
    fecha_de_fin_de_ejecucion = Column(DateTime)
    fecha_inicio_liquidacion = Column(DateTime)
    fecha_fin_liquidacion = Column(DateTime)


class Contrato(Base):
    __tablename__ = "contratos"

    index = Column(Integer, primary_key=True, index=True)
    uid = Column(String, unique=True)
    orden_entidad = Column(String)
    nombre_de_la_entidad = Column(String)
    nit_de_la_entidad = Column(String)
    tipo_de_proceso = Column(String)
    regimen_de_contratacion = Column(String)
    detalle_del_objeto_a_contratar = Column(String)
    tipo_de_contrato = Column(String)
    fecha_de_cargue_en_el_secop = Column(DateTime)
    numero_del_contrato = Column(String)
    cuantia_proceso = Column(Float)
    identificacion_del_contratista = Column(String)
    nom_raz_social_contratista = Column(String)
    fecha_de_firma_del_contrato = Column(DateTime)
    fecha_ini_ejec_contrato = Column(DateTime)
    plazo_de_ejec_del_contrato = Column(Float)
    cuantia_contrato = Column(Float)
    espostconflicto = Column(Boolean)
    sexo_replegal_entidad = Column(String)
    fecha_fin_ejec = Column(DateTime)
    fecha_firma_cont = Column(DateTime)






