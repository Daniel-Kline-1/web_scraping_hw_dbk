#!/usr/bin/env python
# coding: utf-8




import requests
from bs4 import BeautifulSoup
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time




def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)



def scrape():


    r = requests.get('https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest')











    soup = BeautifulSoup(r.text, 'html.parser')






    result1 = soup.find_all('div', attrs={'class':'content_title'})











    news_title = result1[0].a.text






    result2 = soup.find_all('div', attrs={'class':'rollover_description_inner'})









    news_p = result2[0].text



    # # Nasa .gov Site




    short_url = "https://www.jpl.nasa.gov/"
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    r2 = requests.get(url)





    soup2 = BeautifulSoup(r2.text, 'html.parser')











    result3 = soup2.find_all('article', attrs={'class':'carousel_item'})





    split1 = result3[0]["style"].split("(")





    short_url_2 = split1[1].split("'")[1]











    featured_image_url = short_url + short_url_2











    from IPython.display import Image
    Image(featured_image_url)


    # #  Nasa Twitter Weather
    # 




    url_tw = "https://twitter.com/marswxreport?lang=en"
    r3 = requests.get(url_tw)
    soup3 = BeautifulSoup(r3.text, 'html.parser')





    result4 = soup3.find_all('div', attrs={'class':'js-tweet-text-container'})






    mars_weather = result4[0].p.text.split("pic")[0]


    # # Mars Facts




    fact_url = "https://space-facts.com/mars/"
    r4 = requests.get(fact_url)
    soup4 = BeautifulSoup(r4.text, 'html.parser')






    result5 = soup4.find_all(attrs={'class':'column-2'})
    result6 = soup4.find_all(attrs={'class':'column-1'})






    data_list1 = []
    data_list2 = []
    for x in list(range(7,16)):
        data_list1.append(result5[x].text)
        data_list2.append(result6[x].text)
        
    df1 = pd.DataFrame({"Value":data_list1},index=data_list2)






    df1.to_html('mars_weather.html')


    # # Mars Image




    img_url1 = "https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg"
    Image(img_url1)





    title1 = "Cerberus Hemisphere"





    img_url2 = "https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg"
    Image(img_url2)





    title2 = "Schiaparelli Hemisphere"





    img_url3 = "https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg"
    Image(img_url3)





    title3 = "Syrtis Major Hemisphere"





    img_url4 = "https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg"
    Image(img_url4)





    title4 = "Valles Marineris Hemisphere"





   


    # Store data in a dictionary
    mars_data = {
       "news_title":news_title,
        "news_p":news_p,
        "featured_image_url":featured_image_url,
        "value":"Value",
        "mars_weather":mars_weather,
        "df1i1":df1.index[0],
        "df1i2":df1.index[1],
        "df1i3":df1.index[2],
        "df1i4":df1.index[3],
        "df1i5":df1.index[4],
        "df1i6":df1.index[5],
        "df1i7":df1.index[6],
        "df1i8":df1.index[7],
        "df1i9":df1.index[8],
        "df1v1":df1.Value[0],
        "df1v2":df1.Value[1],
        "df1v3":df1.Value[2],
        "df1v4":df1.Value[3],
        "df1v5":df1.Value[4],
        "df1v6":df1.Value[5],
        "df1v7":df1.Value[6],
        "df1v8":df1.Value[7],
        "df1v9":df1.Value[8],
        "df2t1":title1,
        "df2t2":title2,
        "df2t3":title3,
        "df2t4":title4,
        "df2i1":img_url1,
        "df2i2":img_url2,
        "df2i3":img_url3,
        "df2i4":img_url4
        
    }


 # Return results
    return mars_data




    




