from app.core.security import get_password_hash
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models import company as models
from app.schemas import user as schemas

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 1. Verifica se a empresa existe
    db_company = db.query(models.Company).filter(models.Company.id == user.company_id).first()
    if not db_company:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    
    # 2. Verifica se o email já existe
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    new_user = models.User(
        email=user.email,
        hashed_password=get_password_hash(user.password), 
        company_id=user.company_id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user