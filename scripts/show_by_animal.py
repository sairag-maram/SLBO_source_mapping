import argparse
from src.session_parser import parse_folder_structure, filter_by_rat

def main():
    parser = argparse.ArgumentParser(description="Show all sessions for a given animal ID.")
    parser.add_argument('--animal', required=True, help="Animal ID (e.g., 5R7-1222)")

    args = parser.parse_args()
    root_path = 'processed/Ctx-Layer23'  # May need to change based on folder

    print(f"\n Parsing session folders in: {root_path}")
    df = parse_folder_structure(root_path)

    print(f"\n Showing sessions for animal: {args.animal}")
    filtered_df = filter_by_rat(df, args.animal)

    if filtered_df.empty:
        print("⚠  No sessions found for this animal.")
    else:
        print(f"\n {len(filtered_df)} sessions found:\n")
        print(filtered_df)

if __name__ == "__main__":
    main()
