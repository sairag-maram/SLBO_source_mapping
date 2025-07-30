import os
import pandas as pd
from datetime import datetime

def parse_folder_structure(root_dir='processed/Ctx-Layer23'):
    records = []

    for rat_name in os.listdir(root_dir):
        rat_path = os.path.join(root_dir, rat_name)
        if not os.path.isdir(rat_path):
            continue

        for session_folder in os.listdir(rat_path):
            session_path = os.path.join(rat_path, session_folder)
            if not os.path.isdir(session_path):
                continue

            try:
                date_str, session_id = session_folder.split('_', 1)
                session_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                session_date = None
                session_id = session_folder

            records.append({
                'cortical_layer': 'Ctx-Layer23',
                'rat': rat_name,
                'session_id': session_id,
                'session_date': session_date,
                'full_path': session_path
            })

    return pd.DataFrame(records)

# Query 1: List sessions by date or range
def filter_by_date(df, start_date, end_date=None):
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else start
    return df[(df['session_date'] >= start) & (df['session_date'] <= end)]

# Query 2: Show sessions for a given animal
def filter_by_rat(df, rat_name):
    return df[df['rat'] == rat_name]

# Query 3: Filter by project or experimental group (if encoded in name)
def filter_by_project(df, keyword):
    return df[df['rat'].str.contains(keyword, case=False, na=False)]

# Query 4: Identify sessions by imaging modality
# (assumes keywords like "2p" or "widefield" in session_id)
def filter_by_modality(df, modality_keyword):
    return df[df['session_id'].str.contains(modality_keyword, case=False, na=False)]
