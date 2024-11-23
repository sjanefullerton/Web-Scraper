import pandas as pd
import os
import re
"""
# List of file names
comments = [
    "loop_comments.csv",
    "Virginia_comments.csv",
    "Tennessee_comments.csv",
    "NorthCarolina_comments.csv",
    "Georgia_comments.csv",
    "florida_comments.csv",
    "anxiety_comments.csv",
    "depression_comments.csv",
    "MentalHealthSupport_comments.csv",
    "mentalhealth_comments.csv"
]
# List of file names for posts
posts = [
    "loop_posts.csv",
    "Virginia_posts.csv",
    "Tennessee_posts.csv",
    "NorthCarolina_posts.csv",
    "Georgia_posts.csv",
    "florida_posts.csv",
    "anxiety_posts.csv",
    "depression_posts.csv",
    "MentalHealthSupport_posts.csv",
    "mentalhealth_posts.csv"
]
titles = [
    "loop_titles.csv",
    "Virginia_titles.csv",
    "Tennessee_titles.csv",
    "NorthCarolina_titles.csv",
    "Georgia_titles.csv",
    "florida_titles.csv",
    "anxiety_titles.csv",
    "depression_titles.csv",
    "MentalHealthSupport_titles.csv",
    "mentalhealth_titles.csv"
]
comments = ["2loop_comments.csv", "3loop_comments.csv"]
posts = ["2loop_posts.csv", "3loop_posts.csv"]
titles = ["2loop_titles.csv", "3loop_titles.csv"]
"""
comments = ["filtered_comments.csv", "2combined_comments.csv"]
posts = ["filtered_posts.csv", "2combined_posts.csv"]
titles = ["filtered_titles.csv", "2combined_titles.csv"]

# Load and combine datasets, skipping empty files
dataframes = []
for file in comments:
    if os.path.exists(file) and os.path.getsize(file) > 0:  # Check existence and non-emptiness
        try:
            df = pd.read_csv(file)
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")
    else:
        print(f"Skipping empty or missing file: {file}")

# Combine if there are valid dataframes
if dataframes:
    combined_comments = pd.concat(dataframes, ignore_index=True)
    combined_comments.to_csv("all_combined_comments.csv", index=False)
    print(combined_comments.head())
else:
    print("No valid files to combine.")

# Load and combine datasets, skipping empty files
dataframes = []
for file in posts:
    if os.path.exists(file) and os.path.getsize(file) > 0:  # Check existence and non-emptiness
        try:
            df = pd.read_csv(file)
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")
    else:
        print(f"Skipping empty or missing file: {file}")

# Combine if there are valid dataframes
if dataframes:
    combined_posts = pd.concat(dataframes, ignore_index=True)
    combined_posts.to_csv("all_combined_posts.csv", index=False)
    print(combined_posts.head())
else:
    print("No valid files to combine.")

# Load and combine datasets, skipping empty files
dataframes = []
for file in titles:
    if os.path.exists(file) and os.path.getsize(file) > 0:  # Check existence and non-emptiness
        try:
            df = pd.read_csv(file)
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")
    else:
        print(f"Skipping empty or missing file: {file}")

# Combine if there are valid dataframes
if dataframes:
    combined_titles = pd.concat(dataframes, ignore_index=True)
    combined_titles.to_csv("all_combined_titles.csv", index=False)
    print(combined_titles.head())
else:
    print("No valid files to combine.")



# Cleaning:

# Define regex patterns
patterns = [
    r"I am a bot",  # Match comments containing "I am a bot" (case-insensitive)
]
# Generalized function to check if a row matches any pattern
def matches_patterns(row):
    # Define columns to check based on the dataset type
    possible_columns = ["Text"]  # Add column names as needed

    # Check specific columns first
    for col in possible_columns:
        if col in row:  # Ensure the column exists
            if any(re.search(pattern, str(row[col]), re.IGNORECASE) for pattern in patterns):
                return True

    # Fallback to checking the entire row as a string
    row_str = str(row)
    if any(re.search(pattern, row_str, re.IGNORECASE) for pattern in patterns):
        return True

    return False


datasets = {
    "comments": "all_combined_comments.csv",
    "titles": "all_combined_titles.csv",
    "posts": "all_combined_posts.csv",
}

for name, file in datasets.items():
    # Load the dataset
    df = pd.read_csv(file)

    # Filter out rows matching the patterns
    filtered_df = df[~df.apply(matches_patterns, axis=1)]

    # Save the cleaned dataset
    filtered_file = f"filtered_{name}.csv"
    filtered_df.to_csv(filtered_file, index=False)

    print(f"{name.capitalize()} cleaned and saved to {filtered_file}")
    print(filtered_df.head())

# Checking for duplicate titles and keeping only one
# Datasets to process
datasets = {
    "titles": "all_combined_titles.csv",
    "posts": "all_combined_posts.csv",
    "comments": "all_combined_comments.csv",
}

# Column name for deduplication
dedup_column = "Text"

# Loop through each dataset
for name, file in datasets.items():
    if os.path.exists(file) and os.path.getsize(file) > 0:  # Check if file exists and is not empty
        try:
            # Load the dataset
            df = pd.read_csv(file)

            if dedup_column in df.columns:
                # Remove duplicates based on the 'text' column
                deduplicated_df = df.drop_duplicates(subset=dedup_column, keep="first")

                # Save the deduplicated dataset to a new file
                deduplicated_file = f"deduplicated_{name}.csv"
                deduplicated_df.to_csv(deduplicated_file, index=False)

                print(f"Deduplicated {name} saved to {deduplicated_file}")
                print(deduplicated_df.head())
            else:
                print(f"Column '{dedup_column}' not found in {name} dataset.")
        except Exception as e:
            print(f"Error processing {name}: {e}")
    else:
        print(f"File {file} is missing or empty.")
