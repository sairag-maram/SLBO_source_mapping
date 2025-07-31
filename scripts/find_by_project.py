import argparse
from src.session_parser import parse_folder_structure, filter_by_project

def main():
    parser = argparse.ArgumentParser(description="Find all sessions from a specific project or experimental group.")
    parser.add_argument('--keyword', required=True, help="Project or group keyword (e.g., '5R7', 's02')")

    args = parser.parse_args()
    root_path = 'processed/Ctx-Layer23'  # May change based on filepath

    print(f"\n Parsing session folders in: {root_path}")
    df = parse_folder_structure(root_path)

    print(f"\n Filtering sessions for project keyword: {args.keyword}")
    filtered_df = filter_by_project(df, args.keyword)

    if filtered_df.empty:
        print(" No sessions found for that keyword.")
    else:
        print(f"\n {len(filtered_df)} sessions found:\n")
        print(filtered_df)

if __name__ == "__main__":
    main()
