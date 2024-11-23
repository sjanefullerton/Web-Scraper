# Reddit Data Scraper and Processor

This repository contains tools and scripts for scraping, cleaning, and processing data from Reddit. The project is designed to collect and analyze posts, titles, and comments from various subreddits. It is specialized for gathering data related to **Hurricane Helene**, making it particularly useful for research into natural disasters, social responses, and sentiment analysis during extreme weather events.

## Features
- **Specialization for Hurricane Helene**:
  - Scrapes posts, comments, and titles from subreddits that discuss Hurricane Helene.
  - Filters data to focus on hurricane-specific content.
  - Combines and organizes related datasets for analysis.
- **General Data Collection**: Scripts can be adapted to scrape other subreddits or topics.
- **Data Cleaning**: Removes duplicate data, bot-generated content, and irrelevant posts.
- **Data Organization**: Consolidated and cleaned datasets for efficient analysis.

## File Structure
- **`data/raw/`**: Contains raw data files from the initial scraping process.
- **`data/processed/`**: Cleaned and deduplicated data, organized and ready for analysis.
- **Scripts**:
  - `KEYcombineandclean_subredditdatasets.py`: Combines and cleans subreddit data, including Helene-related posts.
  - `KEYhurricanehelenesubreddit.py`: Tailored scraper for Hurricane Helene discussions.
  - `KEYloopsubreddit.py`: Iterative scraper for collecting data from multiple subreddits.
- **Output Files**:
  - `all_combined_<data_type>.csv`: Consolidated data from multiple subreddits.
  - `deduplicated_<data_type>.csv`: Deduplicated files for each data type (posts, titles, comments).
  - `filtered_<data_type>.csv`: Cleaned data, excluding unwanted content (e.g., bot-generated messages).

## How to Use This Repository
1. **Setup**:
   - Clone this repository:  
     ```bash
     git clone https://github.com/sjanefullerton/Web-Scraper.git
     cd Web-Scraper
     ```
   - Install dependencies (if applicable) using a virtual environment:
     ```bash
     python -m venv .venv
     source .venv/bin/activate  # For Mac/Linux
     .\.venv\Scripts\activate  # For Windows
     pip install -r requirements.txt
     ```
   
2. **Running Scripts**:
   - To scrape Hurricane Helene data, use the specialized script:
     ```bash
     python KEYhurricanehelenesubreddit.py
     ```
   - To clean and process the scraped data:
     ```bash
     python KEYcombineandclean_subredditdatasets.py
     ```

3. **Analyze Data**:
   - Use the cleaned and deduplicated CSV files (`filtered_*.csv` or `deduplicated_*.csv`) for analysis in Python, R, or any data analysis tool.

## Applications
This repository is particularly suited for:
- **Hurricane Helene Research**: Analyze public response and discussion trends around Hurricane Helene.
- **Sentiment Analysis**: Understand the emotional tone of Reddit discussions during natural disasters.
- **Topic Modeling**: Explore themes and patterns in Reddit content about extreme weather.
- **Building Datasets for ML Models**: Create labeled datasets for machine learning applications in disaster studies.



