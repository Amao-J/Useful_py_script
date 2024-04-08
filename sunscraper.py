from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


website="https://www.thesun.co.uk/sport/football/"
chrome_option=webdriver.ChromeOptions() 
chrome_option.add_experimental_option("detach",True)
chrome_option.binary_location="C:/Users/user/OneDrive/Desktop/chrome-win64/chrome-win64/chrome.exe"
driver=webdriver.Chrome(options=chrome_option)

driver.get(website)
containers=driver.find_elements(By.XPATH,"//div[@class='teaser__copy-container']")

titles=[]
subtitles=[]
links=[]

for container in containers:
    title=container.find_element(By.XPATH,"./a/h3").text
    subtitle=container.find_element(By.XPATH,"//div[@class='teaser__copy-container']/a/p")
    link=container.find_element(By.XPATH,"./a").get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)


mydict={'title':titles,'subtitle':subtitles,'link':links}

df_headlines=pd.DataFrame(data=mydict)
df_headlines
df_headlines.to_csv('headlines3.csv')

driver.quit()
