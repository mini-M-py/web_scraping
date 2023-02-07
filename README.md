# web_scrapping
This project uses BeautifulSoup and Selenium to extract product information (name, original price, and current price) from Daraz, a popular online shopping platform in Nepal.

## Usages
1) Run the scrip in terminal: main.py
2) Enter the Url of the product you want to scrape from Daraz's official websites.

## Explanation of the code
1) First the script creates an instance of the "FirefoxOptions" class and sets the browser to run on headless mode by adding "--headless" argument to the options.
2) Then, the script opens a web driver using options and loads the website.
3) After the website is loaded, the script waits for the dynamic content to load.
4) The HTML source code is then extracted and parsed using BeautifulSoup.
5) The required product information is extracted by finding specific HTML elements and their classes/ids.
6) The extracted data is then printed in formatted manner.
7) Finally,the web driver is closed.

## Conclusion
This project is just a basic example of web scraping with BeautifulSoup and Selenium. The code can be furthur optimized and extende to scrape more information and more complex operations.
