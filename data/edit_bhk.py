import pandas as pd
import os

# ✅ Make sure the file is in the same folder as this script
csv_file = 'Bangalore_House_Prices.csv'

# Check if the file exists
if not os.path.exists(csv_file):
    print(f"Error: {csv_file} not found in this folder!")
else:
    # Load dataset
    df = pd.read_csv(csv_file)

    # 1️⃣ Rename column 'bhk' to 'Bedrooms'
    if 'bhk' in df.columns:
        df.rename(columns={'bhk': 'Bedrooms'}, inplace=True)
        print("Column 'bhk' renamed to 'Bedrooms'.")
    else:
        print("Column 'bhk' not found; skipping rename.")

    # 2️⃣ Edit a single value safely
    # Example: Change row with index 2 to 4 Bedrooms
    if 'Bedrooms' in df.columns and len(df) > 2:
        df.at[2, 'Bedrooms'] = 4
        print("Row 2 updated to 4 Bedrooms.")
    else:
        print("Row 2 or 'Bedrooms' column not found; skipping value edit.")

    # 3️⃣ Save updated dataset safely
    updated_csv = 'Bangalore_House_Prices_updated.csv'
    df.to_csv(updated_csv, index=False)
    print(f"Updated dataset saved as '{updated_csv}'.")

    # Optional: Preview first 5 rows
    print(df.head())
