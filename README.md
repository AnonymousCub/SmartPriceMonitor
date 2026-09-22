## Smart Price Monitor

A Python project that monitors the price of a product on a website and sends an email notification when the price reaches or drops below a target price.

## What It Does

The Smart Price Monitor:

- Retrieves product information from a website
- Checks the current product price
- Compares the price against a target price
- Sends an email notification when the target price is reached
- Uses web scraping to collect the product information

## Technologies Used

- Python
- Requests
- BeautifulSoup
- SMTP / Email
- Web scraping

## What I Learned

This project gave me hands-on experience working with Python libraries, HTTP requests, HTML parsing, and automated email notifications.

I also learned how to troubleshoot issues with dependencies, requests, and extracting information from webpages.

## How It Works

The basic process is:

1. Send a request to the product webpage.
2. Parse the webpage using BeautifulSoup.
3. Find the product name and current price.
4. Compare the current price with the target price.
5. Send an email notification if the price meets the target.

## Future Improvements

Some features I would like to add in the future:

- Monitor multiple products
- Run the monitor automatically on a schedule
- Add price history tracking
- Store price data in a database
- Improve error handling
- Add configurable email settings
- Create a simple user interface

## Project Status

This is an ongoing personal Python project, I plan to continue adding features and improving the monitoring and notification system.
