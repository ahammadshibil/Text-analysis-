import os
import pandas as pd



# List to hold the articles' content
articles_content = []
input_data = pd.read_excel("/home/shibil/Annual report/Webscrape/Input.xlsx")
# Load each article based on the URL_ID from your input_data DataFrame
for index, row in input_data.iterrows():
    url_id = int(row['URL_ID'])
    file_path = f'articles/{url_id}.txt'
    
    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            articles_content.append(file.read())
    else:
        articles_content.append("")

# Load all the stopwords lists

stopwords_files = [
    "/home/shibil/Annual report/Webscrape/StopWords/StopWords_Auditor.txt",
    "/home/shibil/Annual report/Webscrape/StopWords/StopWords_Currencies.txt",
    "/home/shibil/Annual report/Webscrape/StopWords/StopWords_DatesandNumbers.txt",
    "/home/shibil/Annual report/Webscrape/StopWords/StopWords_Generic.txt",
    "/home/shibil/Annual report/Webscrape/StopWords/StopWords_GenericLong.txt"
]


# Combine all stopwords into a single set
all_stopwords = set()

for file_path in stopwords_files:
    try:
        # Try reading with utf-8 encoding first
        with open(file_path, 'r', encoding='utf-8') as file:
            all_stopwords.update([word.strip().lower() for word in file.readlines()])
    except UnicodeDecodeError:
        # If utf-8 fails, try with ISO-8859-1 encoding
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            all_stopwords.update([word.strip().lower() for word in file.readlines()])




cleaned_articles = []
# Save the cleaned articles back to their respective files

for index, (cleaned_article, row) in enumerate(zip(cleaned_articles, input_data.iterrows())):
    url_id = int(row[1]['URL_ID'])
    file_path = f'articles/{url_id}.txt'
    
    # Save the cleaned article
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_article)
for article in articles_content:
    cleaned_article = ' '.join([word for word in article.split() if word.lower() not in all_stopwords])
    cleaned_articles.append(cleaned_article)
