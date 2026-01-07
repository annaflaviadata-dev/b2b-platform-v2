from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    cnpj = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    # Relacionamento: Uma empresa pode ter vários usuários
    users = relationship("User", back_populates="owner_company")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    # Chave Estrangeira: liga o usuário a uma empresa específica
    company_id = Column(Integer, ForeignKey("companies.id"))

    # Relacionamento: Volta para a empresa
    owner_company = relationship("Company", back_populates="users")