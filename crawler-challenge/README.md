# crawler-interview

Scraping is the process of extracting information from websites using code.

In this take-home task you will be scraping information from the Government of Bahamas website.
We would like you to extract the URLs of legal documents, their titles and dates.
This is a typical site that a scraping engineer at Reg-Genome may encounter.

There are two challenges. Recent graduates or junior applicants are only required to complete the first.
Please do not spend more than 1 hour in total on both challenges.

## Instructions
1. Navigate to the challenge.py file located in the following directory: 
crawler_interview/crawler_interview/spiders/challenge.py

2. Complete the below task consisting of two challenges (also outlined in the challenge.py file)

> -------- Challenge 1 --------
> 
> Scrape the table for acts starting with the letter 'A' only 
> from the table found on the below page:
> http://laws.bahamas.gov.bs/cms/en/legislation/acts.html
> 
> Update the implementation of the parse method to output the intended data.
> 
> Save your spider output by running it with the following command:
> 
> `scrapy crawl challenge -o output-1.json`
> 
> (Make sure you are in the directory which contains scrapy.cfg when running this)
>
> NOTE: If you wish to use XPATH queries instead of CSS selectors
> you may modify the code and do so.
>
> -------- Challenge 2 --------
> 
> Recent graduates or junior applicants are not required to complete this, but are welcome to have a go.
> 
> Is there a way to scrape all tables for acts beginning with all letters?
>
>so, please modify/add to the code as you see fit, 
> or alternatively note down your ideas to discuss in the follow-up interview if
> you run out of time.
>
> Save your spider output by running it with the following command:
> 
> `scrapy crawl challenge -o output-2.json`
> 
> (Make sure you are in the directory which contains scrapy.cfg when running this)
 
3. Please do not spend more than 1 hour in total on the task.
