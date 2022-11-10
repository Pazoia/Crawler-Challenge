import scrapy


class ChallengeSpider(scrapy.Spider):
    name = "challenge"
    allowed_domains = ["laws.bahamas.gov.bs"]
    start_urls = ["http://laws.bahamas.gov.bs/cms/en/legislation/acts.html"]

    """
    -------- Challenge 1 --------
    Scrape the table for acts starting with the letter 'A' only 
    from the table found on the below page:
    http://laws.bahamas.gov.bs/cms/en/legislation/acts.html
    
    Update the implementation of the parse method to output the intended data.
    Save your spider output by running it with the following command:
    
    scrapy crawl challenge -o output.json
    (Make sure you are in the directory which contains scrapy.cfg when running this)

    NOTE: If you wish to use XPATH queries instead of CSS selectors
    you may modify the code and do so.
    
    -------- Challenge 2 --------
    Recent graduates or junior applicants are not required to complete this, but are welcome to have a go.
    
    Is there a way to scrape all tables for acts beginning with all letters?
    If so, please modify/add to the code as you see fit, 
    or alternatively note down your ideas to discuss in the follow-up interview if
    you run out of time.
 
    *** Please do not spend more than 1 hour in total on the task.***
    """

    def parse(self, response):
        # 1. Write a CSS selector that finds all of the table rows
        css_selector = "tbody > tr"

        rows = response.css(css_selector)
        for row in rows:
            # 2. Extract the title of the document link from the row
            title = row.css("td > a::text").get()

            # 3. Extract the URL (href attribute) of the document link in the row
            source_url = row.css("td > a::attr(href)").get()

            # 4. Ensure that the source_url is complete, i.e starts with "http://laws.bahamas.gov.bs"
            source_url = f"http://laws.bahamas.gov.bs{source_url}"

            # 5. Extract the date from the row
            date = row.css("td.commencement::text").get()

            # 6. Clean up the date text by stripping any blank spaces that appear before and after it.
            date = date.strip()

            yield {
                "title": title,
                "source_url": source_url,
                "date": date,
            }
