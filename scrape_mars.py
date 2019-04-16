
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist

def scrape():

    url = "https://mars.nasa.gov/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    Marstitle = soup.title.text.strip()
    Marstitle

    MarsP = soup.p.text.strip()
    MarsP

    executable_path = {'executable_path': "/Users/Renee/Downloads/chromedriver_win32/chromedriver.exe"}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "http://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    browser.click_link_by_partial_text('FULL IMAGE')
    
    browser.click_link_by_partial_text('more info')
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.findAll(attrs ={"main_image"})
    for image in images:
        url_image = image.attrs['src']
        featured_image = ['https://www.jpl.nasa.gov/' + url_image]     
        
    featured_image

    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all('li', class_='js-stream-item stream-item stream-item ')
    for result in results:
        mars_weather = result.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text

    mars_weather

    url = "https://space-facts.com/mars/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    import pandas as pd

    tables = pd.read_html(url)
    tables

    df = tables[0]

    df.columns = ['Description', 'Data']

    df.head()

    html_table = df.to_html()
    html_table

    url = "https://astrogeology.usgs.gov/search/results/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    test = browser.find_by_css('div.description')
 
    hemisphere_list = []
    for i in range(len(test)):
        dict1 = {}
        browser.find_by_css('div.description')[i].find_by_css('h3').click()
        sample = browser.find_link_by_text('Sample').first
        dict1['image_url'] = sample['href']
        #print(sample['href'])                                           
        text = browser.find_by_css('h2.title').text
        dict1['title'] = text
        hemisphere_list.append(dict1)
        browser.back()

    hemisphere_list

