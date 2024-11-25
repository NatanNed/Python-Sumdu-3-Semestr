# Author: Natan Nedaikhlib

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
import string

# Ensure the necessary NLTK data packages are downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')  # Added to resolve the LookupError

def process_text(input_file, output_file):
    """
    Reads text from input_file, processes it, and writes the result to output_file.
    """
    # Read text from input_file
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        print(f"Successfully read from {input_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
        return
    
    # Tokenization
    tokens = word_tokenize(text)
    print(f"Number of tokens after tokenization: {len(tokens)}")
    # Uncomment below to see tokens
    # print(tokens)
    
    # Initialize lemmatizer and stemmer
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    
    # Remove punctuation from tokens
    tokens_no_punct = [word for word in tokens if word not in string.punctuation]
    print(f"Number of tokens after removing punctuation: {len(tokens_no_punct)}")
    # Uncomment below to see tokens
    # print(tokens_no_punct)
    
    # Convert tokens to lowercase
    tokens_lower = [word.lower() for word in tokens_no_punct]
    print(f"Number of tokens after converting to lowercase: {len(tokens_lower)}")
    # Uncomment below to see tokens
    # print(tokens_lower)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens_no_stop = [word for word in tokens_lower if word not in stop_words]
    print(f"Number of tokens after removing stop words: {len(tokens_no_stop)}")
    # Uncomment below to see tokens
    # print(tokens_no_stop)
    
    # Lemmatization
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens_no_stop]
    print(f"Number of tokens after lemmatization: {len(lemmatized_tokens)}")
    # Uncomment below to see tokens
    # print(lemmatized_tokens)
    
    # Stemming
    stemmed_tokens = [stemmer.stem(word) for word in lemmatized_tokens]
    print(f"Number of tokens after stemming: {len(stemmed_tokens)}")
    # Uncomment below to see tokens
    # print(stemmed_tokens)
    
    # Join tokens back into a string
    processed_text = ' '.join(stemmed_tokens)
    print(f"Length of processed text: {len(processed_text)} characters")
    
    # Write processed text to output_file
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(processed_text)
        print(f"Processed text written to {output_file}")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")

def main():
    input_file = 'input.txt'    # Input file containing up to 100 words
    output_file = 'output.txt'  # Output file to write the processed text
    
    process_text(input_file, output_file)

if __name__ == "__main__":
    main()
