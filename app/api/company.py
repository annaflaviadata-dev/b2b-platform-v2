from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Linhas de conexão que você confirmou:
from app.db.database import get_db 
from app.models import company as models
from app.schemas import company as schemas

router = APIRouter(prefix="/companies", tags=["Companies"])

# --- Daqui para baixo é a lógica que faz a API funcionar ---

@router.post("/", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    # Verifica se o CNPJ já existe para não duplicar
    db_company = db.query(models.Company).filter(models.Company.cnpj == company.cnpj).first()
    if db_company:
        raise HTTPException(status_code=400, detail="CNPJ já cadastrado")
    
    new_company = models.Company(name=company.name, cnpj=company.cnpj)
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

@router.get("/", response_model=List[schemas.Company])
def list_companies(db: Session = Depends(get_db)):
    return db.query(models.Company).all()

# Rota para ATUALIZAR uma empresa
@router.put("/{company_id}", response_model=schemas.Company)
def update_company(company_id: int, company_update: schemas.CompanyCreate, db: Session = Depends(get_db)):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if not db_company:
        raise HTTPException(status_code=404, detail="Empresa não encontrada para atualizar")
    
    db_company.name = company_update.name
    db_company.cnpj = company_update.cnpj
    
    db.commit()
    db.refresh(db_company)
    return db_company

# Rota para DELETAR uma empresa
@router.delete("/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if not db_company:
        raise HTTPException(status_code=404, detail="Empresa não encontrada para deletar")
    
    db.delete(db_company)
    db.commit()
    return {"message": f"Empresa {company_id} removida com sucesso"}