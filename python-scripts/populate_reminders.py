import pandas as pd
import os
from pathlib import Path

def process_reminder_files(evals_file, reminder_folder):
    """
    Process reminder files and add evaluation links and recommendations.
    """
    print(f"\nStarting process with:")
    print(f"Evals file: {evals_file}")
    print(f"Reminder folder: {reminder_folder}")
    
    # Check if evals file exists
    if not os.path.exists(evals_file):
        print(f"ERROR: Evals file {evals_file} not found!")
        return
        
    # Read the evaluations file
    print("\nReading evals file...")
    evals_df = pd.read_csv(evals_file)
    print(f"Found {len(evals_df)} rows in evals file")
    print("Evals columns:", evals_df.columns.tolist())
    
    evals_df.columns = evals_df.columns.str.strip()
    evals_df['student_name'] = evals_df['student_name'].str.strip()
    
    # Check reminder folder
    reminder_folder = Path(reminder_folder)
    if not reminder_folder.exists():
        print(f"ERROR: Reminder folder {reminder_folder} not found!")
        return
        
    # List all CSV files in the folder
    reminder_files = list(reminder_folder.glob('*.csv'))
    
    # Process each reminder file
    for reminder_file in reminder_files:
        print(f"\nProcessing {reminder_file.name}...")
        
        # Read the reminder file
        reminder_df = pd.read_csv(reminder_file)
        print(f"Found {len(reminder_df)} rows in reminder file")
        print("Reminder columns:", reminder_df.columns.tolist())
        
        reminder_df.columns = reminder_df.columns.str.strip()
        reminder_df['student_name'] = reminder_df['student_name'].str.strip()
        
        # Merge with evals
        print("\nMerging with evals data...")
        updated_df = reminder_df.merge(
            evals_df[['student_name', 'class_link', 'RecommendedNextClass']],
            on='student_name',
            how='left'
        )
        
        # Create output filename
        output_file = reminder_folder / f"processed_{reminder_file.name}"
        
        # Save the updated file
        updated_df.to_csv(output_file, index=False)
        print(f"Saved processed file to {output_file}")
        print(f"Processed file has {len(updated_df)} rows")
        print("Final columns:", updated_df.columns.tolist())

# Usage
if __name__ == "__main__":
    evals_file = 'evals.csv'
    reminder_folder = './reminder'  # Adjust this path as needed
    
    process_reminder_files(evals_file, reminder_folder)