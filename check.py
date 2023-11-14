import nltk
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import os
import pandas as pd


# List to hold the articles' content
cleaned_articles = []
input_data = pd.read_excel("/home/shibil/Annual report/Webscrape/Input.xlsx")
# Load each article based on the URL_ID from your input_data DataFrame
for index, row in input_data.iterrows():
    url_id = int(row['URL_ID'])
    file_path = f'articles/{url_id}.txt'
    
    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            cleaned_articles.append(file.read())
    else:
        cleaned_articles.append("")



def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='ISO-8859-1') as f:
            return f.read()

# Read and tokenize positive and negative words
positive_words_text = read_file("/home/shibil/Annual report/Webscrape/MasterDictionary/MasterDictionary/positive-words.txt")
negative_words_text = read_file("/home/shibil/Annual report/Webscrape/MasterDictionary/MasterDictionary/negative-words.txt")

positive_word_tokens = set(word_tokenize(positive_words_text))
negative_word_tokens = set(word_tokenize(negative_words_text))

# Define a basic function to count syllables
def count_syllables(word):
    vowels = "AEIOUYaeiouy"
    count = 0
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith('e'):
        count -= 1
    if count == 0:
        count += 1
    return count

def compute_article_metrics(article):
    # Tokenize the article
    word_tokens = set(word_tokenize(article))
    
    # Count positive and negative words
    positive_score = sum(1 for token in word_tokens if token in positive_word_tokens)
    negative_score = sum(1 for token in word_tokens if token in negative_word_tokens)
    
    blob = TextBlob(article)
    
    # Polarity and Subjectivity
    polarity_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity
    
    # Average Sentence Length
    num_sentences = len(blob.sentences)
    num_words = len(word_tokens)
    avg_sentence_length = num_words / num_sentences if num_sentences else 0
    
    # Word Count and Complex Word Count
    word_count = len(word_tokens)
    complex_word_count = sum(1 for token in word_tokens if count_syllables(token) > 2)
    
    # Percentage of Complex Words
    percentage_complex_words = (complex_word_count / word_count) * 100 if word_count else 0
    
    # Fog Index
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    
    # Syllable Per Word
    total_syllables = sum(count_syllables(token) for token in word_tokens)
    syllable_per_word = total_syllables / word_count if word_count else 0
    
    # Personal Pronouns
    personal_pronouns = ["i", "me", "we", "us", "you", "he", "him", "she", "her", "it", "they", "them"]
    personal_pronouns_count = sum(1 for token in word_tokens if token.lower() in personal_pronouns)
    
    # Average Word Length
    total_word_length = sum(len(token) for token in word_tokens)
    avg_word_length = total_word_length / word_count if word_count else 0
    
    return {
        "POSITIVE_SCORE": positive_score,
        "NEGATIVE_SCORE": negative_score,
        "POLARITY_SCORE": polarity_score,
        "SUBJECTIVITY_SCORE": subjectivity_score,
        "AVG_SENTENCE_LENGTH": avg_sentence_length,
        "PERCENTAGE_OF_COMPLEX_WORDS": percentage_complex_words,
        "FOG_INDEX": fog_index,
        "AVG_NUMBER_OF_WORDS_PER_SENTENCE": avg_sentence_length,
        "COMPLEX_WORD_COUNT": complex_word_count,
        "WORD_COUNT": word_count,
        "SYLLABLE_PER_WORD": syllable_per_word,
        "PERSONAL_PRONOUNS": personal_pronouns_count,
        "AVG_WORD_LENGTH": avg_word_length
    }

# Compute metrics for all cleaned articles
article_metrics = [compute_article_metrics(article) for article in cleaned_articles]
article_metrics[:5]  # Display the metrics for the first 5 articles


# Load the provided Excel file
output_data_structure = pd.read_excel('/home/shibil/Annual report/Webscrape/Output Data Structure.xlsx')

# Extract the structure and recognize the required columns
columns = output_data_structure.columns


for i, metrics in enumerate(article_metrics):

    for key, value in metrics.items():

        # Ensure the column name matches the Excel column naming

        column_name = key.replace('_', ' ').upper()

        if column_name in columns:

            output_data_structure.at[i, column_name] = value



# Save the updated DataFrame back into the Excel file

output_file_path = "/home/shibil/Annual report/Webscrape/Output Data Structure.xlsx"

output_data_structure.to_excel(output_file_path, index=False)



output_file_path