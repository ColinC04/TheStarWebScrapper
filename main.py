##
# Program that Collects all the Main headlines from the news and prints it to the user
#
# @authour Colin Chambachan
# @date July 20th, 2020

## Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

## Open the Browser and go to thestar.com 
# Declare path for Chrome webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.minimize_window()
driver.get("https://www.thestar.com/")

# Cretes a list of headlines where all the headlines will be appended to
listOfHeadlines = []

def collect_headlines():
    """ Scrapes thestar.com to pull some of the headlines on the website """
    # Finds the headlines 
    all_spans = driver.find_elements_by_xpath("//span[@data-test-id='mediacard-headline']")
    # Append all the headlines ot the previous list
    for span in all_spans:
        listOfHeadlines.append(span.text)
        # Limit the number of news titles given, list appends the top 5 news headlines
        if len(listOfHeadlines)> 5:
            break

# Call the collect_headlines() function
collect_headlines()
# Ouput the headlines to the user
print(listOfHeadlines)