import sys
from src.session_parser import parse_folder_structure, filter_by_date

def main():
    # --- Edit these as needed ---
    root_path = 'processed/Ctx-Layer23'  # Change if path is different
    start_date = '2024-06-01'            # YYYY-MM-DD -> Adjust dates for desired time period
    end_date = '2024-06-05'              

    print(f"\n Parsing session folders in: {root_path}")
    df = parse_folder_structure(root_path)

    print(f"\n Filtering sessions from {start_date} to {end_date or start_date}")
    filtered_df = filter_by_date(df, start_date, end_date)

    print(f"\n {len(filtered_df)} sessions found:\n")
    print(filtered_df)

if __name__ == "__main__":
    main()
