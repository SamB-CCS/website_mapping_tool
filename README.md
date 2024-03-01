# Website Mapping Tool

## Description

This Website Mapping tool is a Python-based web scraping application that uses scrapy to obtain source and target urls for a given website.

## Table of Contents

- [Installation](#installation)

## Installation

Please ensure you have Python installed on your system. The version used for this application is 3.11.7. If using a mac and homebrew use the command: `brew install python`

1. **Check Pip is installed**: To check if Pip is installed, open your terminal and type: `pip --version`.

2. **Install Scrapy**: Install it using Pip by running the following command in your terminal: `pip install scrapy`
 
3. **Clone the Repository**: Clone this repository to your local machine using the command: `git clone https://github.com/SamB-CCS/website_mapping_tool` 

4. **Navigate to the Project Directory**: Change your current directory to the cloned respository and navigate to the `spiders` directory using the command: `cd web_crawler/web_crawler/spiders`

5. **Change the default source url**: Amend the `start_urls` to your source url and amend the `allowed_domains` too if using the mapping to in the `crawler.py` file to your target domain. To use the sitemap tool amend the `start_urls` in the `sitemap.py` file

6. **Use the mapping tool**: To use this tool run the command: `scrapy crawl mycrawler -o output.json`

7. **Use the sitemap generator tool**: To use this tool run the command: `scrapy crawl sitemap_spider -o sitemap.xml`

#### The output files will generate as a json for the mapping too and and xml for the sitemap. 


