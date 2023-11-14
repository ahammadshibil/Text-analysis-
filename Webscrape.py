import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

# Load the Excel file
input_data = pd.read_excel("/home/shibil/Annual report/Webscrape/Input.xlsx")

# Create a folder for saving the articles
if not os.path.exists('articles'):
    os.makedirs('articles')

# Loop through each URL and extract the article
for index, row in input_data.iterrows():
    url = row['URL']
    url_id = int(row['URL_ID'])

    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the article title and text (may need adjustment based on website structure)
        title = soup.find('h1').text
        content = soup.find('div', class_='td-post-content')  # This class might need to be changed
        if content:
            article_text = content.text

            # Save to a text file
            with open(f'articles/{url_id}.txt', 'w', encoding='utf-8') as file:
                file.write(title + '\n')
                file.write(article_text)
    else:
        print(f"Failed to fetch URL: {url}")

print("Articles extraction completed!")
