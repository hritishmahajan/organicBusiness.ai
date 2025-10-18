# Step 1: Import all required libraries
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# download NLTK data files (only first time)
nltk.download('punkt')
nltk.download('stopwords')

# Step 2: Load dataset
data = pd.read_csv("reviews.csv")
print(data.head())
