from app.database import get_engine
from app.ingestion import extract_data
from app.transformation import transform_data
from app.load import load_data


def run_pipeline():
    engine = get_engine()

    df = extract_data()
    df = transform_data(df)
    load_data(df, engine)

    print("Pipeline executado com sucesso!")


if __name__ == "__main__":
    run_pipeline()