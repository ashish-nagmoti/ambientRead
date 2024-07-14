
from textblob import TextBlob

from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Go to the page that contains the book
driver.get('http://127.0.0.1:8000/reader/2/')

# Wait for the JavaScript code to execute and the book to be loaded
driver.implicitly_wait(10)

# Get the text of the book
text = driver.execute_script('return $("#bb-bookblock").data("text");')

# Perform sentiment analysis with TextBlob
blob = TextBlob(text)
sentiment = blob.sentiment

print('Sentiment: ', sentiment)

# Close the browser
driver.quit()
# Make a GET request to the web page

