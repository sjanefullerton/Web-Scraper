# Reddit Data Scraper and Processor

This repository contains tools and scripts for scraping, cleaning, and processing data from Reddit. The project is designed to collect and analyze posts, titles, and comments from various subreddits. It is specialized for gathering data related to **Hurricane Helene**, making it particularly useful for research into natural disasters, social responses, and sentiment analysis during extreme weather events.

## Features
- **Specialization for Hurricane Helene**:
  - Scrapes posts, comments, and titles from subreddits that discuss Hurricane Helene.
  - Filters data to focus on hurricane-specific content.
  - Combines and organizes related datasets for analysis.
- **General Data Collection**: Scripts can be adapted to scrape other subreddits or topics.
- **Data Cleaning**: Removes duplicate data, bot-generated content, and irrelevant posts.

---
## Scraper and Data Processing Files

This project contains several Python scripts for scraping data from Reddit, processing it, and cleaning up the data for analysis. Below is a description of each script and how to use them.

### General Usage Instructions
Before running any of the following scripts, ensure that you have completed the following steps:
1. **Set up your environment**:
   - Create and activate a virtual environment (if you haven't already):
     ```bash
     python -m venv .venv
     source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
     ```
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```
2. **Set up Reddit API credentials**:
   - For scripts that scrape data from Reddit using the PRAW API, make sure to configure your Reddit API credentials (client ID, client secret, and user agent). You can find instructions on how to do this in the [PRAW documentation](https://praw.readthedocs.io/en/latest/getting_started/).
   
3. **Run the scripts**:
   - Once your environment is set up and credentials are configured, you can run any of the scripts as follows:
     ```bash
     python <script_name>.py
     ```
   - Replace `<script_name>` with the name of the specific script you wish to run.

### Individual Script Descriptions

#### 1. `KEYhurricanehelenesubreddit.py`
This script uses PRAW (Python Reddit API Wrapper) to scrape data from subreddits that are relevant to Hurricane Helene. It filters posts, titles, and comments based on specific keywords related to the hurricane, focusing on emotional responses to the event.

#### 2. `KEYhurricanehelenesubreddit_withfilters.py`
This script is similar to `KEYhurricanehelenesubreddit.py`, but with additional filtering steps. It uses the same keywords to scrape posts related to Hurricane Helene and further filters out irrelevant content based on predefined conditions (e.g., certain keywords or post types).

#### 3. `KEYloopsubreddit.py`
This script loops through multiple subreddits (related to Hurricane Helene and other topics) and scrapes posts, comments, and titles that match relevant keywords. It handles multiple subreddits and continues scraping until a specified condition is met (e.g., scraping a certain number of posts or reaching the end of the subreddit).

#### 4. `KEYloopsubreddit_andothersortings.py`
This script is an extension of `KEYloopsubreddit.py`. It includes additional sorting features to better organize the scraped data. After scraping, it can apply further sorting and filtering to categorize the data by specific criteria (e.g., post type, number of comments).

#### 5. `KEYcombineandclean_subredditdatasets.py`                                                                     
This script combines and cleans multiple subreddit datasets. It reads in multiple CSV files, processes the data by rem
oving duplicates, and merges the datasets into a clean, unified format for further analysis.   
---

## Requirements

To run any of the above scripts, you must first set up your environment as outlined in the [General Usage Instructions](#general-usage-instructions) section.

---

## Accessing the Data

This project includes raw and processed data that has been scraped. To access the data, you will need to unzip the `data.zip` file, which contains both the raw and processed data.

1. **Download the `data.zip` file** from the repository.

2. **Unzip the file**:
   
   Once you've downloaded the `data.zip` file, unzip it to your desired location using your preferred method:
   
   - On macOS/Linux:
     ```bash
     unzip data.zip -d data
     ```
   - On Windows, you can simply right-click the zip file and choose "Extract All".

---

## Additional Notes

- If you plan to add more data or make changes to the scraping process, ensure you are working within the virtual environment to avoid conflicts with global packages.
- The `requirements.txt` file contains all the necessary libraries to recreate the environment. If you need to set up the project in the future or on a different machine, simply follow the instructions above to recreate the environment.
