from bs4 import BeautifulSoup
from selenium import webdriver




# Creat an instance of the FirefoxOptions class
options = webdriver.FirefoxOptions()

# add the "--headless" argument to the options to run the browser on headless mode
options.add_argument("--headless")

#start a web driver, using the option
driver = webdriver.Firefox(options=options)


#load the website
url = input("input url of your product from daraz official wbsites:\n")
driver.get(url)

#wait for the dinamic content to load
driver.implicitly_wait(5)


#get the HTML source code
html_text = driver.page_source

#use Beautifulsoup to parse the HTML
soup = BeautifulSoup(html_text, "lxml")

#extracting data
main = soup.find("div",{"id":"root"})
products = main.find("div",{"class":"box--LNmE6"})
container_list = products.find("div",{"class":"ant-row main--pIV2h"})
product_list = container_list.find("div",{"class":"ant-col-24"})
common_list = product_list.find("div",{"class":"ant-row"})
content_list = common_list.find("div",{"class":"ant-col-20 ant-col-push-4 side-right--Tyehf"})
box = content_list.find("div",{"class":"box--ujueT"})
grid_item = box.find_all("div",{"class":"gridItem--Yd0sa"})
products_list = []
for item in grid_item:
    item_box = item.find("div",{"class":"box--pRqdD"})
    box_inner = item_box.find("div",{"class":"inner--SODwy"})
    info = box_inner.find("div",{"class":"info--ifj7U"})
    title = info.find("div",{"class":"title--wFj93"}).text
    price = info.find("div",{"class":"price--NVB62"}).text
    original_price_element = info.find("div",{"class":"priceExtra--ocAYk"})
    original_price = original_price_element.text if original_price_element else ""
    if "-" in original_price:
        original_price, discount = original_price.split("-")
        original_price = original_price.replace("Rs.", "").strip()
    else:
        discount = ""
    price = price.replace("Rs.", "").strip()
    product = {
        "title": title,
        "current_price":price,
        "original_price":original_price,
        "discount": discount
    }
    products_list.append(product)
    print(f"""
       name of product => {title}
       original price => {original_price}
       current price => {price}""")
    print("")
min_price = float(input("Enter your budget range:Rs "))
result = [ p for p in products_list if float(p["current_price"].replace(",","")) <= min_price]
#printing data
for product in result:
    print(f"""
    name of product =>{product["title"]}
    discount => {product["discount"]}
    product price =>Rs{product["current_price"]} including discount
    """)
#closing driver
driver.quit()
