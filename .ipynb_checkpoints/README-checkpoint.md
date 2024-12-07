This is the repository for News articles analysis related to stock data using Pyspark, LLMs

Installation and setup:

1. Create a conda environment
2. Install all the packages from the requirements.txt file
3. Create a new api key for https://newsapi.org/
4. Use any GPU suitable for you (we have used A100)

Main Code file:
/src/newsanalysis.ipynb

Output files:
news_data.json - articles extracted (if save = True)
sentiment_data.json - sentiment labels given by the Flan-T5 model for all the articles extracted within given date range
gt_sentiment_openai.json - ground truth sentiment labels generated using GPT4-o-mini
top_k_openai.json - list of top 5 most discussed topics identified using GPT4-o-mini
