
# coding: utf-8

# # Mission to Mars

# In[3]:


# Import dependencies
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import re
from time import sleep

# In[4]:
def Scrape():

    # Create browser instance
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)


    # #### Scrape the latest News Title and Paragraph Text

    # In[11]:


    #visit the url
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    sleep(1)

    # Scrape the latest News Title and Paragraph Text
    html = browser.html
    soup = bs(html, 'html.parser')
    news_title = soup.find("div", class_="content_title").find("a").text
    news_p = soup.find("div", class_="article_teaser_body").text


    # #### Mars Space Images

    # In[14]:


    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    browser.find_by_id('full_image').click()
    sleep(1)
    html = browser.html
    soup = bs(html,"html.parser")
    img = soup.find('img',class_="fancybox-image")['src']
    featured_image_url = "https://www.jpl.nasa.gov" + img


    # #### Mars Weather

    # In[27]:




    url ="https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    sleep(1)

    html = browser.html
    soup = bs(html,"html.parser")
    tweet_list = soup.find_all("li", class_="stream-item")
    for tweet in tweet_list:
        tweet_text = tweet.find("div").find("p").text
        if re.match("SOL ",tweet_text):
            break
        else:
            pass
    mars_weather = tweet_text
    mars_weather


    # #### Mars Facts

    # In[32]:


    url="https://space-facts.com/mars/"
    browser.visit(url)
    sleep(1)

    tables = pd.read_html("https://space-facts.com/mars/")

    mars_table = tables[0]
    html_table = mars_table.to_html(header=False, index=False)


    # #### Mars Hemisphere

    # In[57]:


    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": ""},
        {"title": "Cerberus Hemisphere", "img_url": ""},
        {"title": "Schiaparelli Hemisphere", "img_url": ""},
        {"title": "Syrtis Major Hemisphere", "img_url": ""},
    ]


    for i in range(len(hemisphere_image_urls)):
        browser.visit(url)
        sleep(1)
        name = hemisphere_image_urls[i]["title"]
        browser.click_link_by_partial_text(name)
        html = browser.html
        soup = bs(html,"html.parser")
        download = soup.find_all("li")[-4]
        hemisphere_image_urls[i]["img_url"] = download.find('a')['href']

    mars_data = {"latest_news_title":news_title,"latest_news_paragraph": news_p,"featured_image": featured_image_url, "mars_weather":mars_weather,"mars_data_table": html_table,"hemisphere_data": hemisphere_image_urls}
    return mars_data

# Scrape()