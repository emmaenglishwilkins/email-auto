import pandas as pd
import json

# with open('class_categories.json', 'r') as json_file:
#     loaded_categories = json.load(json_file)

file = '../csvs/curr_pop.csv'
logins = '../csvs/new-students.csv'

# Load the class list and login credentials
df = pd.read_csv(file)  # Class information
login_df = pd.read_csv(logins)  # Login credentials

# Strip whitespace from column names
df.columns = df.columns.str.strip()
login_df.columns = login_df.columns.str.strip()

# Print the columns of login_df to check for 'Attendee'
print("Columns in login_df:", login_df.columns)

# Function to map class names to their corresponding login columns
'''
def get_login_columns(class_name):
    if "Python" in class_name:
        return "Microsoft Outlook Account id:94230", "Microsoft Outlook Password id:94231"
    elif "Scratch" in class_name:
        return "Scratch ID id:12166", "Scratch password id:12151"
    elif "Minecraft" in class_name:
        return "Minecraft ID id:16746", "MInecraft Password id:16747"
    elif "Roblox" in class_name:
        return "Roblox Username id:23748", "Roblox Password id:23749"
    else:
        return None, None  # Default for unsupported classes
'''
# Ensure indices are aligned
df = df.reset_index(drop=True)
login_df = login_df.reset_index(drop=True)

# Initialize empty lists for username and password
usernames = []
passwords = []

# Iterate through each student in the class list
for i, row in df.iterrows():
    # class_name = row['class_name']
    student_name = row['student_name'].strip()  # Strip whitespace

    # Check if username and password are already populated
    if pd.isna(row.get('username')) and pd.isna(row.get('password')):
        # Find the login info for this student from login_df using the 'Attendee' column
        student_row = login_df[login_df['Attendee'].str.strip() == student_name]  # Strip whitespace

        print(f"Looking for {student_name} in login_df")

        if not student_row.empty:
            # Extract the username and password for this student
            username = student_row.iloc[0]['username']
            password = student_row.iloc[0]['password']
        else:
            # If no match is found, handle accordingly
            print(f"No login info found for {student_name}")
            username = password = None

        # Append the results to the lists
        usernames.append(username)
        passwords.append(password)
    else:
        # If the username and password are already populated, append existing values
        usernames.append(row['username'])
        passwords.append(row['password'])

# Assign the lists to the DataFrame
df['username'] = usernames
df['password'] = passwords

# Save the updated DataFrame
df.to_csv("updated_class_info.csv", index=False)

print(df.head())


'''

def main():
    export = "export.csv"
    login_info = 
    # output = "login_pop.csv"

    try:
        df = pd.read_csv(file)

        for index, row in df():
            class_name = row['class_name']

        # make list of all unique class_names

        #delete_df.to_csv(output, index=False)

    except FileNotFoundError:
        print(f"Error: File {file} not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: File {file} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
'''


        
