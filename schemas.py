from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any


class GroupableColumns(str, Enum):

    col13 = "nombre_entidad"
    col1 = "departamento"
    col2 = "ciudad"
    col3 = "orden"
    col4 = "sector"
    col5 = "rama"
    col6 = "rama"
    col7 = "estado_contrato"
    col8 = "tipo_de_contrato"
    col9 = "modalidad_de_contratacion"
    col10 = "proveedor_adjudicado"
    col11 = "month"
    col12 = "year"
    col14 = "es_pyme"

class DescribeFull(BaseModel):

    group: Optional[str]
    max_valor: Optional[float]
    min_valor: Optional[float]
    avg_valor: Optional[float]
    cantidad_contratos: Optional[int]

    class Config:
        orm_mode = True


class FullContrato(BaseModel):

    id: int
    nit_entidad: int
    nombre_entidad: str
    departamento: str
    ciudad: str
    orden: Optional[str]
    sector: Optional[str]
    rama: Optional[str]
    entidad_centralizada: Optional[str]
    estado_contrato: Optional[str]
    descripcion_del_proceso: Optional[str]
    tipo_de_contrato: Optional[str]
    modalidad_de_contratacion: Optional[str]
    justificacion_modalidad_de: Optional[str]
    fecha_de_firma: Optional[datetime]
    fecha_de_inicio_del_contrato: Optional[datetime]
    fecha_de_fin_del_contrato: Optional[datetime]
    condiciones_de_entrega: Optional[str]
    proveedor_adjudicado: Optional[str]
    es_pyme: Optional[str]
    obligaci_n_ambiental: Optional[str]
    valor_del_contrato: Optional[float]
    valor_pendiente_de_pago: Optional[float]
    valor_pagado: Optional[float]
    valor_pendiente_de_ejecucion: Optional[float]
    espostconflicto: Optional[str]
    urlproceso: Optional[str]
    destino_gasto: Optional[str]
    nombre_representante_legal: Optional[str]
    identificaci_n_representante_legal: Optional[str]
    g_nero_representante_legal: Optional[str]
    ultima_actualizacion: Optional[datetime]
    objeto_del_contrato: Optional[str]
    fecha_de_inicio_de_ejecucion: Optional[datetime]
    fecha_de_fin_de_ejecucion: Optional[datetime]
    fecha_inicio_liquidacion: Optional[datetime]
    fecha_fin_liquidacion: Optional[datetime]

    class Config:
        orm_mode = True


class KeyWordSearch(BaseModel):
    nombre_entidad: Optional[str]
    departamento: Optional[str]
    ciudad: Optional[str]
    orden: Optional[str]
    sector: Optional[str]
    rama: Optional[str]
    estado_contrato: Optional[str]
    descripcion_del_proceso: Optional[str]
    modalidad_de_contratacion: Optional[str]
    es_pyme: Optional[str]
    valor_del_contrato: Optional[Dict[str, float]] = {"$gt": 1_000_000,
                                                    "$lt": 500_000_000}
    order_by_column: Optional[str] = "id"


