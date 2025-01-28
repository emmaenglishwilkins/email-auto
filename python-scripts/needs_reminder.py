'''
this would have done the whole job but since she kinda already did half im going to use a different python file (populate_reminder)
this is solving the issue that parent name is not in the evals columns information so it uses the export csv from the previous semester as well 
student was signed up for the previous semester and recieved a recomendation for the next class
    final csv has 
        parent_name 
        parent_email
        student_name
        class_name
        class_rec
        class_link
'''
import pandas as pd

# Read all CSV files
df = pd.read_csv('evals.csv')
current_signedup_df = pd.read_csv('exports.csv')
previous_exports_df = pd.read_csv('last_semester_exports.csv')  # Add the previous semester's exports

# Clean column names by stripping whitespace
df.columns = df.columns.str.strip()
current_signedup_df.columns = current_signedup_df.columns.str.strip()
previous_exports_df.columns = previous_exports_df.columns.str.strip()

# Clean student names
df['student_name'] = df['student_name'].str.strip()
current_signedup_df['Attendee'] = current_signedup_df['Attendee'].str.strip()
previous_exports_df['Attendee'] = previous_exports_df['Attendee'].str.strip()

# Find students in evals who are NOT in the current signup list
not_signed_up = df[~df['student_name'].isin(current_signedup_df['Attendee'])].copy()

# Add parent information from previous semester's exports
# Merge with previous exports data
not_signed_up = not_signed_up.merge(
    previous_exports_df[['Attendee', 'parent_name', 'parent_email']], 
    left_on='student_name', 
    right_on='Attendee', 
    how='left'
)

# Drop the duplicate Attendee column from the merge
not_signed_up = not_signed_up.drop('Attendee', axis=1)

# Save the results
not_signed_up.to_csv("missing_students_with_parents.csv", index=False)

print(f"Found {len(not_signed_up)} students who haven't signed up this semester")
print("\nFirst few students who haven't signed up:")
print(not_signed_up.head())
print("\nColumns in output:", not_signed_up.columns.tolist())

# find students who signed up who are not signed up for this semester -- no parent_name
'''
import pandas as pd

# Read the CSV files
df = pd.read_csv('evals.csv')
signedup_df = pd.read_csv('exports.csv')

# Clean column names by stripping whitespace
df.columns = df.columns.str.strip()
signedup_df.columns = signedup_df.columns.str.strip()

# Clean student names
df['student_name'] = df['student_name'].str.strip()
signedup_df['Attendee'] = signedup_df['Attendee'].str.strip()

# Find students in evals who are NOT in the signup list
not_signed_up = df[~df['student_name'].isin(signedup_df['Attendee'])]

# Save the results
not_signed_up.to_csv("missing_students.csv", index=False)

print(f"Found {len(not_signed_up)} students who haven't signed up this semester")
print("\nFirst few students who haven't signed up:")
print(not_signed_up.head())

'''