import json
import os

# The directory where the JSON files are located
directory = "C:\\Users\\alexa\\Documents\\selfLearning\\coding\\guessingGame\\dataFiles\\blocks"

# The final combined JSON data
combined_data = {}

# Iterate through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        # Read the JSON data from the file
        with open(os.path.join(directory, filename), 'r') as f:
            data = json.load(f)
        
        # Combine the JSON data
        combined_data[filename[:-5]] = data  # We remove the .json extension from the filename here

# Write the combined JSON data to a new file
with open("combined.json", 'w') as f:
    json.dump(combined_data, f)
