# Reddit Data Scraper and Processor

This repository contains tools and scripts for scraping, cleaning, and processing data from Reddit. The project is designed to collect and analyze posts, titles, and comments from various subreddits, with an emphasis on organizing and deduplicating large datasets. This can be especially useful for research, sentiment analysis, or general data exploration.

## Features
- **Data Collection**: Python scripts to scrape posts, titles, and comments from specific subreddits.
- **Data Cleaning**: Functions to filter out bot comments, remove duplicates, and organize data for analysis.
- **Data Organization**: Combined and deduplicated CSV files for streamlined analysis.
- **Flexible Workflow**: Easily extendable to handle additional subreddits or data requirements.

## File Structure
- **`data/raw/`**: Contains raw data files from the initial scraping process.
- **`data/processed/`**: Cleaned and deduplicated data, ready for analysis.
- **Scripts**: Python scripts for web scraping, cleaning, and deduplication:
  - `KEYcombineandclean_subredditdatasets.py`: Combines and cleans subreddit data.
  - `KEYloopsubreddit.py`: Iterative scraping for multiple subreddits.
  - `KEYhurricanehelenesubreddit.py`: Specialized scraper for Hurricane Helene-related subreddits.
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
   - To scrape data, use the appropriate script for your target subreddit:
     ```bash
     python KEYloopsubreddit.py
     ```
   - To clean and process the data:
     ```bash
     python KEYcombineandclean_subredditdatasets.py
     ```

3. **Analyze Data**:
   - Use the cleaned and deduplicated CSV files (`filtered_*.csv` or `deduplicated_*.csv`) for analysis in Python, R, or any data analysis tool.

## Applications
This repository can be useful for:
- Social media sentiment analysis.
- Topic modeling and clustering.
- Exploring trends or themes in Reddit discussions.
- Building datasets for machine learning models.

## Contributing
Contributions are welcome! If you'd like to add features, optimize the code, or enhance the documentation:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request for review.

