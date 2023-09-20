import  nltk
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords, gutenberg
from collections import Counter
from nltk.stem import PorterStemmer
from nltk import FreqDist
from  nltk.sentiment import SentimentIntensityAnalyzer

# Read the file

data = gutenberg.raw('melville-moby_dick.txt')
tokens = word_tokenize(data)
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w.lower() not in stop_words]
tagged = pos_tag(tokens)

tags = [tag for word, tag in tagged]
tag_counts=Counter(tags)
most_commen_tags = tag_counts.most_common(5)
stemmer=PorterStemmer()
stemmed_tokens={}
for i in range(0,20):
   stemmed_tokens[i]=stemmer.stem(filtered_tokens[i])

print('Lemmatization of the top 20tokens i:',stemmed_tokens)

freq_dist = FreqDist(tags)

freq_dist.plot()
plt.xlabel('Parts of Speech')
plt.ylabel('Frequency')
plt.title('Frequency of Parts of Speech')
plt.xticks(rotation=45)
plt.show()

sia = SentimentIntensityAnalyzer()
sentiment_scores = [sia.polarity_scores(token)["compound"] for token in filtered_tokens]

average_sentiment_score = sum(sentiment_scores) / len(sentiment_scores)

if average_sentiment_score > 0.05:
    overall_sentiment = "positive"
else:
    overall_sentiment = "negative"

# Display Results
print("Average Sentiment Score:", average_sentiment_score)
print("Overall Text Sentiment:", overall_sentiment)