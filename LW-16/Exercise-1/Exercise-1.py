# Author: Natan Nedaikhlib

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import matplotlib.pyplot as plt
import string
from collections import Counter

# Download necessary NLTK data packages
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('gutenberg')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

def load_text():
    """
    Loads the 'Julius Caesar' text from Project Gutenberg using NLTK.
    """
    from nltk.corpus import gutenberg
    # Ensure the file exists
    if 'shakespeare-caesar.txt' in gutenberg.fileids():
        text = gutenberg.raw('shakespeare-caesar.txt')
    else:
        raise ValueError("The file 'shakespeare-caesar.txt' was not found in the Gutenberg corpus.")
    return text

def word_count(text):
    """
    Counts the number of words in the text.
    """
    tokens = word_tokenize(text)
    num_words = len(tokens)
    print(f"Total number of words in the text: {num_words}")
    return tokens

def most_common_words(tokens, num=10):
    """
    Finds the most common words in the list of tokens.
    """
    word_counts = Counter(tokens)
    most_common = word_counts.most_common(num)
    return most_common

def plot_word_frequency(word_freq, title, filename=None):
    """
    Plots a bar chart of word frequencies.
    Optionally saves the plot to a file.
    """
    words, counts = zip(*word_freq)
    plt.figure(figsize=(12, 8))
    bars = plt.bar(words, counts, color='skyblue')
    plt.xlabel('Words', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title(title, fontsize=16)
    plt.xticks(rotation=45, ha='right')
    
    # Add numerical labels above the bars
    for bar in bars:
        height = bar.get_height()
        plt.annotate(f'{height}',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),  # Offset above the bar
                     textcoords="offset points",
                     ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    
    if filename:
        plt.savefig(filename)
        print(f"Plot saved as '{filename}'.")
    plt.show()

def remove_stopwords_punctuation(tokens):
    """
    Removes stop words and punctuation from the list of tokens.
    """
    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)
    filtered_tokens = [
        word.lower() for word in tokens
        if word.lower() not in stop_words and word not in punctuation
    ]
    return filtered_tokens

def lemmatize_tokens(tokens):
    """
    Lemmatizes tokens, converting them to their base form.
    """
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized

def filter_by_pos(tokens, allowed_tags={'NN', 'JJ'}):
    """
    Filters tokens by parts of speech.
    By default, retains only nouns (NN) and adjectives (JJ).
    """
    pos_tags = pos_tag(tokens)
    filtered_tokens = [word for word, tag in pos_tags if tag in allowed_tags]
    return filtered_tokens

def main():
    # Load the text
    text = load_text()

    # Task 1: Determine the number of words in the text
    tokens = word_count(text)

    # Task 2: Find the 10 most frequently used words and plot the chart
    most_common = most_common_words(tokens, 10)
    print("\n10 Most Frequent Words (Including Stop Words and Punctuation):")
    for word, freq in most_common:
        print(f"{word}: {freq}")
    plot_word_frequency(
        most_common,
        "Top 10 Most Frequent Words (Including Stop Words and Punctuation)",
        filename='most_common_including_stopwords.png'
    )

    # Task 3: Remove stop words and punctuation, then re-analyze
    filtered_tokens = remove_stopwords_punctuation(tokens)
    filtered_common = most_common_words(filtered_tokens, 10)
    print("\n10 Most Frequent Words (After Removing Stop Words and Punctuation):")
    for word, freq in filtered_common:
        print(f"{word}: {freq}")
    plot_word_frequency(
        filtered_common,
        "Top 10 Most Frequent Words (After Removing Stop Words and Punctuation)",
        filename='most_common_filtered.png'
    )

    # Additional Task 4: Lemmatization
    lemmatized_tokens = lemmatize_tokens(filtered_tokens)
    lemmatized_common = most_common_words(lemmatized_tokens, 10)
    print("\n10 Most Frequent Words (After Lemmatization):")
    for word, freq in lemmatized_common:
        print(f"{word}: {freq}")
    plot_word_frequency(
        lemmatized_common,
        "Top 10 Most Frequent Words (After Lemmatization)",
        filename='most_common_lemmatized.png'
    )

    # Additional Task 5: Filtering by Parts of Speech
    # For example, retain only nouns and adjectives
    pos_filtered_tokens = filter_by_pos(lemmatized_tokens, allowed_tags={'NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS'})
    pos_filtered_common = most_common_words(pos_filtered_tokens, 10)
    print("\n10 Most Frequent Words (After Filtering by Parts of Speech):")
    for word, freq in pos_filtered_common:
        print(f"{word}: {freq}")
    plot_word_frequency(
        pos_filtered_common,
        "Top 10 Most Frequent Words (After Filtering by Parts of Speech)",
        filename='most_common_pos_filtered.png'
    )

if __name__ == "__main__":
    main()
