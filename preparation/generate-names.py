import random
import csv
import string


# Function to generate random names
def generate_name():
    # Generate first name
    first_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))
    first_name = first_name.capitalize()

    # Generate last name
    last_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
    last_name = last_name.capitalize()

    # Generate middle name
    middle_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))
    middle_name = middle_name.capitalize()

    # Generate suffix
    suffix = random.choice(['', '', '', 'Jr.', 'Sr.'])

    # Construct full name
    if suffix:
        name = f"{first_name} {middle_name} {last_name} {suffix}"
    else:
        if random.random() > 0.5:
            name = f"{first_name} {middle_name} {last_name}"
        else:
            name = f"{first_name} {last_name}"

    # Get the length of the generated name including spaces
    name_count = len(name)

    return name, name_count


# Generate random names and lengths
names_with_counts = [generate_name() for _ in range(40)]

# Sort the names based on name count (from smaller to larger)
names_with_counts.sort(key=lambda x: x[1])

# Write names and counts to CSV file
with open('preparation/participants_name_counts.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Name_Count', 'ID', 'Sex']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i, (name, name_count) in enumerate(names_with_counts, start=1):
        writer.writerow(
            {'Name': name, 'Name_Count': name_count, 'ID': f'{i:03d}', 'Sex': random.choice(['Male', 'Female'])})

print("Names generated with counts (including spaces) and saved to participants_name_counts.csv")
