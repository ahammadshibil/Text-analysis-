Text Analysis Methodology Documentation
Table of Contents

    Sentimental Analysis
        Cleaning using Stop Words Lists
        Creating a Dictionary of Positive and Negative Words
        Extracting Derived Variables
    Analysis of Readability
    Average Number of Words Per Sentence
    Complex Word Count
    Word Count
    Syllable Count Per Word
    Personal Pronouns
    Average Word Length

1. Sentimental Analysis <a name="sentimental-analysis"></a>

Sentimental analysis involves determining whether a piece of writing is positive, negative, or neutral. The following algorithm is designed for use in financial texts.
1.1 Cleaning using Stop Words Lists <a name="cleaning-using-stop-words-lists"></a>

Stop Words Lists in the "StopWords" folder are utilized to clean the text, excluding words found in the Stop Words List.
1.2 Creating a Dictionary of Positive and Negative Words <a name="creating-a-dictionary-of-positive-and-negative-words"></a>

The Master Dictionary in the "MasterDictionary" folder is used to create a dictionary of positive and negative words, excluding those found in the Stop Words Lists.
1.3 Extracting Derived Variables <a name="extracting-derived-variables"></a>

The text is tokenized using the NLTK tokenize module, and the following variables are calculated:

    Positive Score
    Negative Score
    Polarity Score
    Subjectivity Score

2. Analysis of Readability <a name="analysis-of-readability"></a>

Readability is calculated using the Gunning Fox index formula, incorporating:

    Average Sentence Length
    Percentage of Complex Words
    Fog Index

3. Average Number of Words Per Sentence <a name="average-number-of-words-per-sentence"></a>

Calculated by dividing the total number of words by the total number of sentences.
4. Complex Word Count <a name="complex-word-count"></a>

Count of words in the text containing more than two syllables.
5. Word Count <a name="word-count"></a>

Total cleaned words in the text, removing stop words and punctuation.
6. Syllable Count Per Word <a name="syllable-count-per-word"></a>

Count of syllables in each word, handling exceptions.
7. Personal Pronouns <a name="personal-pronouns"></a>

Counts of personal pronouns - "I," "we," "my," "ours," and "us" using regex, excluding the country name "US."
8. Average Word Length <a name="average-word-length"></a>

Calculated by summing the total number of characters in each word and dividing by the total number of words.
