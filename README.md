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

This project contains several Python scripts for scraping data from Reddit, processing it, and cleaning up the data for analysis. Below is a description of each script and how to use it.

### 1. `KEYcombineandclean_subredditdatasets.py`
This script combines and cleans multiple subreddit datasets. It reads in multiple CSV files, processes the data by removing duplicates, and merges the datasets into a clean, unified format for further analysis.

#### How to use:
- Place all your raw CSV files in the appropriate folder (e.g., `data/raw/`).
- Run the script to combine and clean the datasets:
  ```bash
  python KEYcombineandclean_subredditdatasets.py
  ```

### 2. `KEYhurricanehelenesubreddit.py`
This script uses PRAW (Python Reddit API Wrapper) to scrape data from subreddits that are relevant to Hurricane Helene. It filters posts, titles, and comments based on specific keywords related to the hurricane, focusing on emotional responses to the event.

#### How to use:
- Set up your Reddit API credentials (client ID, client secret, user agent).
- Run the script to scrape relevant Reddit data:
  ```bash
  python KEYhurricanehelenesubreddit.py
  ```

### 3. `KEYhurricanehelenesubreddit_withfilters.py`
This script is similar to `KEYhurricanehelenesubreddit.py` but with additional filtering steps. It uses the same keywords to scrape posts related to Hurricane Helene and further filters out irrelevant content based on predefined conditions (e.g., certain keywords or post types).

#### How to use:
- Set up your Reddit API credentials.
- Run the script to scrape and filter Reddit data:
  ```bash
  python KEYhurricanehelenesubreddit_withfilters.py
  ```

### 4. `KEYloopsubreddit.py`
This script loops through multiple subreddits (related to Hurricane Helene and other topics) and scrapes posts, comments, and titles that match relevant keywords. It handles multiple subreddits and continues scraping until a specified condition is met (e.g., scraping a certain number of posts or reaching the end of the subreddit).

#### How to use:
- Set up your Reddit API credentials.
- Run the script to start scraping data from multiple subreddits:
  ```bash
  python KEYloopsubreddit.py
  ```

### 5. `KEYloopsubreddit_andothersortings.py`
This script is an extension of `KEYloopsubreddit.py`. It includes additional sorting features to better organize the scraped data. After scraping, it can apply further sorting and filtering to categorize the data by specific criteria (e.g., post type, number of comments).

#### How to use:
- Set up your Reddit API credentials.
- Run the script to scrape and sort data from multiple subreddits:
  ```bash
  python KEYloopsubreddit_andothersortings.py
  ```

---

## Requirements

To run any of the above scripts, you must first set up your environment as outlined in the [Setting Up the Environment](#setting-up-the-environment) section.

---

## Setting Up the Environment

To get started with this project, you will need to create your own virtual environment and install the dependencies. Follow these steps:

1. **Create a virtual environment**:
   
   In your terminal, navigate to the project directory and create a virtual environment:
   
   ```bash
   python3 -m venv .venv
   ```

2. **Activate the virtual environment**:
   
   To activate the virtual environment, use the following command:
   
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

3. **Install the dependencies**:
   
   Once the virtual environment is activated, install the required Python packages by running:
   
   ```bash
   pip install -r requirements.txt
   ```

   This will install all the dependencies required for the project.

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
