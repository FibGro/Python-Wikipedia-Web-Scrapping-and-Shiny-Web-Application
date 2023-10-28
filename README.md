# Python Web Scrapping and Web Application Python Shiny (Top 50 Companies by Revenue)

![Example screenshot](./unsplash.jpg)

## Table of Contents
* [General Information](#general-information)
* [Dataset Information](#dataset-information)
* [Technologies Used](#technologies-used)
* [Deploy Shiny](#deploy-shiny)
* [End Result](#end-result)
* [Acknowledgements](#Acknowledgements)
<!-- * [License](#license) -->

## General Information
This project involves web scraping using BeautifulSoup on Wikipedia to gather information about the top 50 companies by revenue, utilizing Python. 
Subsequently, we conduct exploratory data analysis, focusing on data cleaning, wrangling, and creating visualizations based on the dataset. 
Finally, we showcase our visualization through a web application created with Shiny Python-Posit and deployed on GitHub.

Note : 
- The Jupyter Notebook contains all the guidelines for the web scraping process.
- The app.py contains code related to building the web application using Shiny.
- I tried Shinylive to build the web application, and then it created automatically the app.py in my VS code when I chose to save it on the disk.

## Dataset Information

The compilation we're working with represents the world's leading companies, determined by their consolidated revenue according to the 2023 Fortune Global 500 rankings and other reliable sources. This curated list spotlights the top 50 companies, each with annual revenues exceeding US$130 billion.

Link : https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue

## Technologies Used
- Jupyter Notebook/Visual Code
- Shinylive for Python
- Github to deploy

## Deploy Shiny

- Create a New Repo in GitHub
- Add the app.py, file.csv, and CSS (if you already built in VS code include all your files)
- Open the codespaces in your new repo and it will direct you to the terminal
- Install shiny:
    `pip install shiny`
- Install shinylive :
    `pip install shinylive`
- Install shinywidgets :
    `pip install shinywidgets`
- Create a docs :
    `shiny export . docs`
- Commit the change and sync into the branch
- After completing, go to your Repo and go to Settings
- In the sidebar, go to Pages
- Define your source and branch. Save.
- Wait for a few minutes and then, the GitHub will create the link for you. 

## End Result 

The link of the Shiny product : https://fibgro.github.io/Python-Wikipedia-Web-Scrapping-and-Shiny-Web-Application/

## Acknowledgements
- The deploying Shiny for Python can be seen in this [YouTube link](https://www.youtube.com/watch?v=eoJjtJfuUqE)
- The beautiful picture is made by [Owen Cavlys](https://www.example.com](https://unsplash.com/@owencavlys)https://unsplash.com/@owencavlys).
