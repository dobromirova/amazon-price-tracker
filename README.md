## Amazon Price Tracker
A Python-based web scraping application that monitors the price of a predefined Amazon product and automatically notifies users when a price drop is detected.

The application retrieves the product's current price, compares it with the previously recorded price, and sends an email notification whenever the price decreases.

# Features
**Web Scraping:** Extracts product price information from Amazon using BeautifulSoup.

**Price Monitoring:** Periodically checks the price of a predefined product.

**Price Drop Detection:** Compares the current price against the previously retrieved price to identify decreases.

**Email Notifications:** Automatically sends an email containing the updated price whenever a decrease is detected.

# Technical Implementation
The application is developed in Python and combines web scraping, price comparison, and email automation.

Key components:
- BeautifulSoup for HTML parsing and data extraction.
- Price comparison logic to identify price decreases.
- Automated price monitoring.
- Email functionality for sending notifications to users.


# Technologies Used
- Python
- BeautifulSoup
- HTML Parsing
- SMTP / Email Services
