# Bible Search App ![BibleSearchApp](https://img.shields.io/badge/BibleSearchApp-black) ![API](https://img.shields.io/badge/API-gray) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django)

Welcome to the Bible Search App, a simple web app that allows users to search for a Bible verse by entering the Book, Chapter, and Verse.

## Overview


The Bible Search App is a straightforward application that retrieves a Bible verse based on the book name, chapter number, and verse number. It utilizes an API to retrieve the search results. The app employs forms on the front end to receive user input, which is then sent to the back end. The back end processes the input, interacts with the API endpoints, and returns the response to the front end. The returned answers are stored in a database and sent to the front end, ensuring that the displayed answers remain on the web page even when the browser window is refreshed.

## Installation
1. Ensure that Flask, SQLAlchemy, Requests, and Python are installed on your machine.
2. Clone the repository and run the following commands:
```
git clone https://github.com/Adniyi/bible-search-app.git
cd bible-search-app
```
3. Open the folder with any text editor or IDE and run the app.py file. This will create a development server on your machine and open your browser window at `http://127.0.0.1:5000` (localhost).


## How to Use
1. Once the app is running, copy the URL or hold down the Control key and right-click on the URL.
2. This will open the app in your default browser. Input the book of the Bible you want to search, along with the chapter number and verse number (the book name should be in lowercase).
3. Click on the FIND button to display the result.


## Example
Here’s a demonstration of how the system works:

![Bible-Search-Image](<Screenshot (22).png>)

The above image shows how the system operates and the result.

## Bugs
Currently, there is no way to delete or clear the page once the result is displayed.
The application also has no way of processing multiple verses at once. 


## Conclusion
The Bible Search App is a simple application that retrieves Bible verses using a free Bible API.

You can find the API by visiting: [Bible Api](https://github.com/wldeh/bible-api).
