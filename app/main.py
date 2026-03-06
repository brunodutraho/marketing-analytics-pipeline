import os
import uvicorn
from fastapi import FastAPI, BackgroundTasks
from app.database import get_engine
from app.ingestion import generate_mock_data
from app.transformation import transform_data
from app.load import load_data

app = FastAPI()

def run_pipeline():
    engine = get_engine()
    
    df = generate_mock_data()
    df_transformed = transform_data(df)
    load_data(df_transformed, engine)
    print("Pipeline executado com sucesso no Railway!")

@app.get("/")
def home():
    return {"status": "Pipeline de Marketing Analytics Ativo", "endpoint_para_rodar": "/run"}

@app.post("/run")
def trigger_pipeline(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_pipeline)
    return {"message": "Pipeline iniciado em segundo plano!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
