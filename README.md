eddit Data Scraper and Processor

This repository contains tools and scripts for scraping, cleaning, and processing data from Reddit. The project is designed to collect and analyze posts, titles, and comments from various subreddits. It is specialized for gathering data related to **Hurricane Helene**, making it particularly useful for research into natural disasters, social responses, and sentiment analysis during extreme weather events.

## Features
- **Specialization for Hurricane Helene**:
  - Scrapes posts, comments, and titles from subreddits that discuss Hurricane Helene.
  - Filters data to focus on hurricane-specific content.
  - Combines and organizes related datasets for analysis.
- **General Data Collection**: Scripts can be adapted to scrape other subreddits or topics.
- **Data Cleaning**: Removes duplicate data, bot-generated content, and irrelevant posts.

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
