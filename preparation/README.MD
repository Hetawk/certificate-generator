# Certificate Preparation

This Python script automates the preparation of certificates by performing the following tasks:

1. **Generating Random Names**: The script generates random names along with their counts (including spaces) and saves them to a CSV file named `participants_name_counts.csv`.

2. **Reordering Names**: It reads the data from `participants_name_counts.csv`, calculates the name count for each participant, and reorders the names based on the name count. The reordered data is then saved to `participants.csv`.

3. **Extracting Image Properties**: A separate script is provided (`get-image-property.py`) to extract properties of the background image used for certificates. This information is saved to a text file named `image-property.txt`.
**Background Image Properties**
- The background image for certificates has the following properties:

- Width: 1160 pixels
- Height: 828 pixels
- Format: PNG
- Color Mode: RGBA

## Prerequisites

- Python 3.x
- Required Python packages listed in `requirements.txt`

## Setup

1. Clone or download this repository to your local machine.
2. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## USAGE

1. Generate Names and Counts
- Run the script `generate-names.py` to generate random names along with their counts. 
- This will create a CSV file named `participants_name_counts.csv` in the `preparation` directory.

2. Reorder Names:
- Run the script `get-name.py` to reorder the names based on their counts.
- The reordered names will be saved to `participants.csv` in the `preparation` directory.

3. Extract Image Properties:
- Run the script `get-image-property.py` to extract properties of the background image used for certificates.
- This will create a text file named `image-property.txt` in the `preparation` directory.