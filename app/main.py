from fastapi import FastAPI
from app.routers import products
from app.database import engine
from app.models.product import Base
import logging

logger = logging.getLogger(__name__)  
app = FastAPI() 

try :
    Base.metadata.create_all(bind=engine)  
except Exception as e:
    logger.error(f"Failed to create database tables: {e}")
    raise

app.include_router(products.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Ecommerce API"}