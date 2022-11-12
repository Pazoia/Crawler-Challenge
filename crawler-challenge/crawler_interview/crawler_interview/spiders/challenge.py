import scrapy
from crawler_interview.crawler_helpers.sanitisation import sanitise_title

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
        inputs_css_selector = response.css("div#alphabet")

        letters_css_selector = inputs_css_selector.css('input::attr(value)').getall()
        letters_css_selector.pop(-1)
        
        for letter in letters_css_selector:
            # Extract letter 'A'
            first_letter_url = f"https://laws.bahamas.gov.bs/cms/en/legislation/acts.html?view=acts_only&submit4={letter}" 
            yield response.follow(first_letter_url, self.extract_data)

            if letter == "Z":
                last_letter_url = f"https://laws.bahamas.gov.bs/cms/en/legislation/acts.html?view=acts_only&submit4={letter}"
                yield response.follow(last_letter_url, self.extract_data)
            else:
                current_letter_index = letters_css_selector.index(letter)
                next_letter = letters_css_selector[current_letter_index + 1]
                next_letter_url = f"https://laws.bahamas.gov.bs/cms/en/legislation/acts.html?view=acts_only&submit4={next_letter}"
                yield response.follow(next_letter_url, self.extract_data)

    def extract_data(self, response):
            # 1. Write a CSS selector that finds all of the table rows
            """
            I originally tried to get all the rows using the 'tr.row0' css selector
            but I noticed that some of the 'tr' elements within the table didn't 
            have the class 'row0', my solution to this was to use the css selector
            all 'tr' elements that have 'tbody' as the parent element.
            """
            css_selector = "tbody > tr"

            rows = response.css(css_selector)

            for row in rows:
                """
                I am checking below if the `title` data query returns a `truthy` value below
                because the css selector 'css_selector' is picking up the '</tbody>' closing tag,
                and throwing an error as there is missing data.
                So if one of the required data elements returns the value of 'None',
                it is ignored.
                """
                # 2. Extract the title of the document link from the row
                title = row.css("td > a::text").get()

                if title:
                    # 3. Extract the URL (href attribute) of the document link in the row
                    source_url = row.css("td > a::attr(href)").get()

                    # 4. Ensure that the source_url is complete, i.e starts with "http://laws.bahamas.gov.bs"
                    full_source_url = f"http://laws.bahamas.gov.bs{source_url}"

                    # 5. Extract the date from the row
                    date = row.css("td.commencement::text").get()

                    # 6. Clean up the date text by stripping any blank spaces that appear before and after it.
                    date = date.strip()

                    yield {
                        "title": sanitise_title(title),
                        "source_url": full_source_url,
                        "date": date,
                    }         
