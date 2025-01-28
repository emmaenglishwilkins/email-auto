import pandas as pd
import json

# Categorize class names based on keywords
categories = {
    "Roblox": [],
    "Robotics": [],
    "Python": [],
    "Scratch": [],
    "Minecraft": [],
    "Other": []
}


file = "../csvs/export.csv"
# Load the CSV file into a DataFrame
df = pd.read_csv(file)

# Extract the unique class names from the 'class_name' column
unique_class_names = df['class_name'].unique().tolist()

# Categorize each class name
for class_name in unique_class_names:
    if "Roblox" in class_name:
        categories["Roblox"].append(class_name)
    elif "Robotics" in class_name:
        categories["Robotics"].append(class_name)
    elif "Python" in class_name:
        categories["Python"].append(class_name)
    elif "Scratch" in class_name:
        categories["Scratch"].append(class_name)
    elif "Minecraft" in class_name:
        categories["Minecraft"].append(class_name)
    else:
        categories["Other"].append(class_name)

# Save dictionary to a JSON file
with open('class_categories.json', 'w') as json_file:
    json.dump(categories, json_file)

with open('class_categories.json', 'r') as json_file:
    loaded_categories = json.load(json_file)

print(loaded_categories)