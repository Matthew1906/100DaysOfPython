#### Day 97 of 100 Days of Python
#### Project Name: Custom Automation - Kaggle Dataset Downloader
#### Things I Implemented: Selenium (Web Automation) and PyAutoGUI (GUI Automation)

#### This program more or less works, but might have different steps according to users

#### How the program works:
1. The user must input a search keyword
2. The program logs in and search for datasets with the typed keyword (with limit of 10-50 mb and in csv format)
3. If there are no datasets, the program stops
4. If any datasets containing that keyword exists, download the most upvoted dataset, and unzip them using PyAutoGUI
