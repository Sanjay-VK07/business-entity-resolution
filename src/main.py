import pandas as pd
from normalize import normalize_name, normalize_address
from blocking import create_block_key

def run_pipeline():
    print("📥 Loading data...")
    df = pd.read_csv("data/raw_data.csv")

    print("🧹 Normalizing...")
    df['clean_name'] = df['name'].apply(normalize_name)
    df['clean_address'] = df['address'].apply(normalize_address)

    print("🔗 Creating block keys...")
    df['block_key'] = df.apply(create_block_key, axis=1)

    print("📦 Creating canonical records...")
    canonical = (
        df.sort_values(by=['clean_name'])
          .groupby('block_key', as_index=False)
          .first()
    )

    print("💾 Saving output...")
    canonical.to_json(
        "output/canonical_records.json",
        orient="records",
        indent=4
    )

    print("✅ Done! File → output/canonical_records.json")
    print(f"🔢 Raw: {len(df)} | Canonical: {len(canonical)}")

if __name__ == "__main__":
    run_pipeline()