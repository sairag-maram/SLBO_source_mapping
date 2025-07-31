import argparse
from src.session_parser import parse_folder_structure, filter_by_modality

def main():
    parser = argparse.ArgumentParser(description="Identify sessions with a particular imaging modality (e.g. 1P, 2P)")
    parser.add_argument('--modality', required=True, help="Imaging modality keyword (e.g., 1P, 2P)")

    args = parser.parse_args()
    root_path = 'processed/Ctx-Layer23'  # Adjust if needed

    print(f"\n Parsing session folders in: {root_path}")
    df = parse_folder_structure(root_path)

    print(f"\n Filtering sessions with modality: {args.modality}")
    filtered_df = filter_by_modality(df, args.modality)

    if filtered_df.empty:
        print(" No sessions found with that modality.")
    else:
        print(f"\n {len(filtered_df)} sessions found:\n")
        print(filtered_df)

if __name__ == "__main__":
    main()
