from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# Function to get the font path
def get_font_path(font_name, font_directory, extensions):
    # Iterate over each extension and check if the font is available
    for ext in extensions:
        font_path = os.path.join(font_directory, f"{font_name}.{ext}")
        if os.path.exists(font_path):
            return font_path

    # If font not found with any extension, return None
    return None

# Specify the directory where the fonts are located
font_directory = "certificate/font"

# Specify the list of font extensions to check
font_extensions = ['ttf', 'otf', 'woff']  # Add more extensions as needed

# Load fonts
name_font_path = get_font_path("LongPath", font_directory, font_extensions)
if name_font_path:
    name_font = ImageFont.truetype(name_font_path, size=75)
else:
    print("Font 'Long Path' not found!")
    name_font = None
sex_font_path = get_font_path("Kefa-Regular", font_directory, font_extensions)
id_font_path = get_font_path("Kefa-Regular", font_directory, font_extensions)
if id_font_path:
    id_font = ImageFont.truetype(id_font_path, size=21.5)
    sex_font = ImageFont.truetype(sex_font_path, size=40)
else:
    print("Font 'Kefa' not found!")
    id_font = None

# Check if both fonts are found before proceeding
if name_font and id_font:
    # Load the background image
    background_image = Image.open("certificate/cert_background.png")

    # Load the data from CSV or Excel file
    data = pd.read_csv("certificate/data/participants.csv")  # Change this to your file name

    # Create the results directory if it doesn't exist
    results_dir = "certificate/results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    # Define coordinates for name, ID, and sex fields
    name_x, name_y = 700, 390  # Center of the name line
    id_x, id_y = 935, 284  # Adjust these coordinates based on your template
    sex_x, sex_y = 540, 491  # Adjust these coordinates for male and female

    # Define the width of each character
    char_width = 20  # Adjust this based on the actual width of characters in the font

    # Iterate through each participant's data
    for index, row in data.iterrows():
        # Get participant's information
        name = row['Name']
        certificate_id = f"2024AECOT{row['ID']:03d}"
        sex = row['Sex']

        # Create a copy of the background image for each participant
        certificate = background_image.copy()
        draw = ImageDraw.Draw(certificate)

        # Count the number of characters in the name
        num_characters = len(name)

        # Calculate the total width of the name
        name_width = num_characters * char_width

        # Calculate the starting x-coordinate for the name to center it horizontally
        if 2 <= num_characters <= 4:
            name_start_x = name_x - (num_characters * -25)
        elif 6 <= num_characters <= 8:
            name_start_x = name_x - (num_characters * 2)
        elif 8 <= num_characters <= 9:
            name_start_x = name_x - (num_characters * 4)
        elif 9 <= num_characters <= 10:
            name_start_x = name_x - (num_characters * 5)
        elif 10 <= num_characters <= 11:
            name_start_x = name_x - (num_characters * 6)
        elif 11 <= num_characters <= 12:
            name_start_x = name_x - (num_characters * 6.5)
        elif 12 <= num_characters <= 13:
            name_start_x = name_x - (num_characters * 7)
        elif 13 <= num_characters <= 14:
            name_start_x = name_x - (num_characters * 7.5)
        elif 14 <= num_characters <= 15:
            name_start_x = name_x - (num_characters * 8)
        elif 15 <= num_characters <= 16:
            name_start_x = name_x - (num_characters * 8.1)
        elif 16 <= num_characters <= 17:
            name_start_x = name_x - (num_characters * 8.8)
        elif 17 <= num_characters <= 18:
            name_start_x = name_x - (num_characters * 9.8)
        elif 18 <= num_characters <= 19:
            name_start_x = name_x - (num_characters * 9.82)
        elif 19 <= num_characters <= 20:
            name_start_x = name_x - (num_characters * 9.83)
        elif 20 <= num_characters <= 21:
            name_start_x = name_x - (num_characters * 9.84)
        elif 21 <= num_characters <= 22:
            name_start_x = name_x - (num_characters * 9.85)
        elif 22 <= num_characters <= 23:
            name_start_x = name_x - (num_characters * 9.87)
        elif 23 <= num_characters <= 24:
            name_start_x = name_x - (num_characters * 10)
        elif 24 <= num_characters <= 25:
            name_start_x = name_x - (num_characters * 10.5)
        elif 25 <= num_characters <= 26:
            name_start_x = name_x - (num_characters * 10.9)
        elif 26 <= num_characters <= 27:
            name_start_x = name_x - (num_characters * 11.2)
        elif 27 <= num_characters <= 28:
            name_start_x = name_x - (num_characters * 11.4)
        elif 28 <= num_characters <= 29:
            name_start_x = name_x - (num_characters * 11.6)
        elif 29 <= num_characters <= 30:
            name_start_x = name_x - (num_characters * 12)
        else:
            name_start_x = name_x - name_width // 2

        # Add name, ID, and sex to the certificate using different fonts
        draw.text((name_start_x, name_y), name, fill="black", font=name_font)
        draw.text((id_x, id_y), str(certificate_id), fill="black", font=id_font)
        # Check sex and adjust coordinates and text accordingly
        if sex.lower() == "male":
            draw.text((sex_x, sex_y), "_", fill="black", font=sex_font)
        elif sex.lower() == "female":
            draw.text((sex_x, sex_y), "_", fill="black", font=sex_font)

        # Save the certificate with participant's name as the file name
        name_for_file = name.replace(" ", "_")  # Replace spaces with underscores
        certificate.save(f"{results_dir}/{name_for_file}_certificate.png")

    print("Certificates generated successfully!")
else:
    print("Fonts not found. Cannot generate certificates.")
