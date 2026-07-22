from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title="AI Routing Engine")
engine = create_engine(os.getenv("DATABASE_URL"))

@app.get("/")
def root():
    return {"message":"AI Routing Engine API is running"}

@app.get("/health/db")
def check_db():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT PostGIS_Version();")).scalar()
        return {"status":"success","postGIS_Version":result}
    except Exception as e:
        return {"status":"error","message":str(e)}
