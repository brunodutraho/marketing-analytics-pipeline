from app.database import get_engine
from app.ingestion import generate_mock_data
from app.transformation import transform_data
from app.load import load_data


def run_pipeline():
    engine = get_engine()

    df = generate_mock_data()
    df_transformed = transform_data(df)
    load_data(df_transformed, engine)

    print("Pipeline executado com sucesso!")


if __name__ == "__main__":
    run_pipeline()