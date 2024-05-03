import csv
import random

# Read data from participants.csv
participants_data = []
with open('preparation/participants_name_counts.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        participants_data.append(row)

# Function to calculate name count (including spaces)
def calculate_name_count(name):
    return len(name)

# Generate name counts for each participant
for participant in participants_data:
    participant['Name_Count'] = calculate_name_count(participant['Name'])

# Sort participants based on name count
participants_data.sort(key=lambda x: x['Name_Count'])

# Write data to participants.csv
with open('preparation/participants.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Name_Count', 'ID', 'Sex']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i, participant in enumerate(participants_data, start=1):
        writer.writerow({'Name': participant['Name'], 'Name_Count': participant['Name_Count'],
                         'ID': participant['ID'], 'Sex': participant['Sex']})

print("Names reorder with the counts being extracted and saved to participants.csv")
