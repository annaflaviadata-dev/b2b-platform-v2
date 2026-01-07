from app.api import company, user
from fastapi import FastAPI
from app.db.database import engine, Base
from app.api import company 

Base.metadata.create_all(bind=engine)
app = FastAPI(title="B2B Platform")
app.include_router(company.router)
app.include_router(user.router)