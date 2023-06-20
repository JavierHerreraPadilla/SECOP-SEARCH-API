from sys import maxsize
from sqlalchemy import desc, func
from fastapi import FastAPI, Depends, Body, Request
from sqlalchemy.orm import Session
from typing import List, Annotated, Optional
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
# from . import models, schemas
import models, schemas
from database import SessionLocal
# from .database import SessionLocal

app = FastAPI()
templates = Jinja2Templates(directory="./")
# templates = Jinja2Templates(directory="./secop_search/templates")

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    columns = models.FullContratoModel.__table__.c
    return templates.TemplateResponse("home.html", {"request": request, "columns": columns})


@app.get("/all_contracts/", response_model=List[schemas.FullContrato], response_description="""returns first 100 results in the DB: offset 0, limit 100 \n 
        Send {'offset':start, 'limit':num_of_results, "order_by_col":"column_name"} as query params\n
        results default return ordered by id  """)
def all_contracts(offset: int = 0, limit: int = 100, order_by_col: str = "id", db: Session = Depends(get_db)):
    query = db.query(models.FullContratoModel).order_by(getattr(models.FullContratoModel, order_by_col)).offset(offset).limit(limit)
    results = query.all()
    return results


@app.get("/describe_full/{col}", response_model=List[schemas.DescribeFull],
         response_description="""Groups by the {col} parameter (exact name of the column). To group by month or year pass the Path parameter {col} as month or year\n
         returns the max, min average and count from valor_del_contrato_column""")
def describe_full(col: schemas.GroupableColumns, db: Session = Depends(get_db)):
    if col == "month":
        query = db.query(
                func.strftime("%Y-%m", models.FullContratoModel.fecha_de_firma).label("group"),
                func.max(models.FullContratoModel.valor_del_contrato).label("max_valor"),
                func.min(models.FullContratoModel.valor_del_contrato).label("min_valor"),
                func.avg(models.FullContratoModel.valor_del_contrato).label("avg_valor"),
                func.count(models.FullContratoModel.id).label("contract_qtty")
            ).group_by(
                func.strftime("%Y-%m", models.FullContratoModel.fecha_de_firma)
            ).order_by(desc(func.strftime("%Y-%m", models.FullContratoModel.fecha_de_firma)))
        return query.all()
    elif col == "year":
        query = db.query(
            func.strftime("%Y", models.FullContratoModel.fecha_de_firma).label("group"),
            func.max(models.FullContratoModel.valor_del_contrato).label("max_valor"),
            func.min(models.FullContratoModel.valor_del_contrato).label("min_valor"),
            func.avg(models.FullContratoModel.valor_del_contrato).label("avg_valor"),
            func.count(models.FullContratoModel.id).label("cantidad_contratos")
        ).group_by(
            func.strftime("%Y", models.FullContratoModel.fecha_de_firma)
        ).order_by(desc(func.strftime("%Y", models.FullContratoModel.fecha_de_firma)))
        return query.all()
    query = db.query(
        getattr(models.FullContratoModel, col).label("group"),
        func.max(models.FullContratoModel.valor_del_contrato).label("max_valor"),
        func.min(models.FullContratoModel.valor_del_contrato).label("min_valor"),
        func.avg(models.FullContratoModel.valor_del_contrato).label("avg_valor"),
        func.count(models.FullContratoModel.id).label("cantidad_contratos")
    ).group_by(
        getattr(models.FullContratoModel, col)
    )
    return query.all()


@app.post("/filter/", response_model=List[schemas.FullContrato], response_description="""Select any column to filter results. Offset 0, limit = 100. Can change them in request body.\n
                                           Dont' include columns you don't want to filter by """)
def filter(search: Optional[schemas.KeyWordSearch], limit: Annotated[int, Body()] = 100, offset: Annotated[int, Body()] = 0, db: Session = Depends(get_db)):
    nombre_entidad = search.nombre_entidad if search.nombre_entidad else ""
    dep = search.departamento if search.departamento else ""
    ciudad = search.ciudad if search.ciudad else ""
    orden = search.orden if search.orden else ""
    sector = search.sector if search.sector else ""
    rama = search.rama if search.rama else ""
    estado_contrato = search.estado_contrato if search.estado_contrato else ""
    descripcion = search.descripcion_del_proceso if search.descripcion_del_proceso else ""
    modalidad = search.modalidad_de_contratacion if search.modalidad_de_contratacion else ""
    greater_than = search.valor_del_contrato.get("$gt", 0) if search.valor_del_contrato else 0
    less_than = search.valor_del_contrato.get("$lt", maxsize) if search.valor_del_contrato else maxsize
    es_pyme = search.es_pyme if search.es_pyme else ""
    query = db.query(models.FullContratoModel).filter(
        models.FullContratoModel.nombre_entidad.like(f"%{nombre_entidad}%"),
        models.FullContratoModel.departamento.like(f"%{dep}%"),
        models.FullContratoModel.ciudad.like(f"%{ciudad}%"),
        models.FullContratoModel.orden.like(f"%{orden}%"),
        models.FullContratoModel.sector.like(f"%{sector}%"),
        models.FullContratoModel.rama.like(f"%{rama}%"),
        models.FullContratoModel.estado_contrato.like(f"%{estado_contrato}%"),
        models.FullContratoModel.descripcion_del_proceso.like(f"%{descripcion}%"),
        models.FullContratoModel.modalidad_de_contratacion.like(f"%{modalidad}%"),
        models.FullContratoModel.es_pyme.like(f"%{es_pyme}%")
    ).filter(
        models.FullContratoModel.valor_del_contrato > greater_than,
        models.FullContratoModel.valor_del_contrato < less_than
    ).order_by(desc(search.order_by_column)).limit(limit).offset(offset)
    final_query = query
    return final_query.all()
