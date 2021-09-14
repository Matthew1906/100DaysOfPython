#### Day 96 of 100 Days of Python
#### Project name: Online Shop
#### Things I Implemented: Web Development, Database, Template Filters, Online Shop System

#### This project supposedly includes payment processing, but the suggested api don't really include my country and it kinda felt like fraud to me, using sandbox doesn't seem to achieve anything
#### Please take note that this website is not responsive at all:v, This project's purpose is to practice by skills in backend using flask. Furthermore, I kinda have to speedrun this project

#### My Approach toward this project
1. Create Flowchart and ERD, design tables
2. Build database, Create basic layout of website(navbar and footer), add categories to the database (save the block of code into ./init/init.txt)
3. User Authentication (login, register, logout) and Mock data for products (taken from amazon, with a little tinkering) -> saved to .csv
4. Insert Mock Data into Database, Add product management functionality (Add new products and Update products), add Admin only decorator, and implemented template filter 
5. Add to Cart function, Pagination, and Search
6. Transaction and Checkout
7. Add Product Review Section, Slightly fix responsiveness

#### Steps of Deployment:
1. Clone this repository
2. Set up a virtual environment by typing 'python -m venv env' in the command line
3. Set your interpreter path to the virtual environment path
4. Download all the dependencies (modules) by typing 'python -m pip install -r requirements.txt'
5. When first deploying the app, don't forget to paste the code from init/init.txt to create database and add initial data
6. Lastly, don't forget to setup SECRET_KEY from .env file so that the program can start
7. Start the application by running the code, and then go to http://127.0.0.1:5000/