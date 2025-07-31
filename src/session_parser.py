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

            # Parse session date and ID
            try:
                date_str, session_id = session_folder.split('_', 1)
                session_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                session_date = None
                session_id = session_folder

            # Detect modalities (look for subfolders like 1P, 2P)
            modalities = []
            for modality in ['1P', '2P']:
                modality_path = os.path.join(session_path, modality)
                if os.path.isdir(modality_path):
                    modalities.append(modality)

            records.append({
                'cortical_layer': 'Ctx-Layer23',
                'rat': rat_name,
                'session_id': session_id,
                'session_date': session_date,
                'modalities': modalities,
                'full_path': session_path
            })

    return pd.DataFrame(records)

# -----------------------------
# Query 1: Filter by date range
# -----------------------------
def filter_by_date(df, start_date, end_date=None):
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else start
    return df[(df['session_date'] >= start) & (df['session_date'] <= end)]

# -------------------------------
# Query 2: Filter by animal (rat)
# -------------------------------
def filter_by_rat(df, rat_name):
    return df[df['rat'] == rat_name]

# -----------------------------------------------------
# Query 3: Filter by project/group keyword in rat name
# -----------------------------------------------------
def filter_by_project(df, keyword):
    return df[df['rat'].str.contains(keyword, case=False, na=False)]

# ------------------------------------------------------
# Query 4: Filter by imaging modality (e.g., 1P, 2P etc.)
# ------------------------------------------------------
def filter_by_modality(df, modality_keyword):
    return df[df['modalities'].apply(lambda x: modality_keyword in x)]
