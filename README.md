# Crawler Challenge

## Table of Contents

- [Client requirements](#client-requirements)
- [Technologies](#technologies)
- [How to run program](#how-to-run-program)
- [Project Status](#project-status)

## Client requirements

Scraping is the process of extracting information from websites using code.
We would like you to extract the URLs of legal documents, their titles and dates.

-------- Challenge 1 --------

- Scrape the table for acts starting with the letter 'A' only from the table found on the below page:  
  http://laws.bahamas.gov.bs/cms/en/legislation/acts.html

- Update the implementation of the parse method to output the intended data.

- Save your spider output by running it with the following command:

```
scrapy crawl challenge -o output-1.json
```

> (Make sure you are in the directory which contains scrapy.cfg when running this)

> NOTE: If you wish to use XPATH queries instead of CSS selectors you may modify the code and do so.

-------- Challenge 2 --------

- Is there a way to scrape all tables for acts beginning with all letters?

- If so, please modify/add to the code as you see fit, or alternatively note down your ideas to discuss in the follow-up interview if you run out of time.

- Save your spider output by running it with the following command:

```
scrapy crawl challenge -o output-2.json
```

> (Make sure you are in the directory which contains scrapy.cfg when running this)

## Technologies

- Python 3.8  
  [Installation instructions](https://www.python.org/)
- Scrapy 2.7

## How to run Crawler

1 - Fork or clone project into your machine

> It's good practice to work on a virtual environment with it's own depencies and packages.

2 - To create a virtual environment on your machine follow the commands below:

```
$ python3 -m venv venv
```

3 - Activate the newly created environment:

```
$ source venv/bin/activate
```

You should see the env_name now on your terminal like in the shown example

```
(venv) [computer:~/projects/crawler_challenge]$
```

4 - Running the crawler

> (Make sure you are in the directory which contains scrapy.cfg when running this)

```
scrapy crawl challenge -o <filename>
```

### **Dependencies**

> To install all dependencies saved in the Pipfile in your virtual environment run the command below:

```
$ pipenv install
```

## Project Status

> To Do's

> Done

- Install and activate virtual environment
- Add .gitignore file
- Initialize git repository
- Create a branch to hold the code with the changes on the parse method using css_selectors. Extracting all acts starting with the letter `A`
- Refactor parse function to extract acts that start with the letter `A`
- Create a branch to hold the code with the changes on the parse method using css_selectors. Extracting all acts starting with the letter `A` to `Z`
- Merge branch to main containing solution for both challenges
- Improve README file with relevant information about project
