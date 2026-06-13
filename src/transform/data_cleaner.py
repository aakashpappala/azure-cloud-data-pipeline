def clean_data(df):
    print("Cleaner Executed Successfully")

    df.columns = df.columns.str.lower().str.strip()

    df = df.drop_duplicates()

    df["total_amount"] = df["quantity"] * df["price"]

    return df