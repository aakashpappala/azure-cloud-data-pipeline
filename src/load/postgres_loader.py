from sqlalchemy import create_engine

def load_to_postgres(df):

    engine = create_engine(
        "postgresql://postgres:Aakash@localhost/salesdb"
    )

    df.to_sql(
        "sales",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data Loaded Successfully")