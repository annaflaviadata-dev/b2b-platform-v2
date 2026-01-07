from pydantic import BaseModel

class CompanyBase(BaseModel):
    name: str
    cnpj: str

class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True