This is the repository for News articles analysis related to stock data using Pyspark, LLMs

Installation and setup:

1. Create a conda environment
2. Install all the packages from the requirements.txt file
3. Create a new api key for https://newsapi.org/
4. Use any GPU suitable for you (we have used A100)

Main Code file:
/src/newsanalysis.ipynb

Output files:<br /> 
news_data.json - articles extracted (if save = True) <br /> 
sentiment_data.json - sentiment labels given by the Flan-T5 model for all the articles extracted within given date range<br /> 
gt_sentiment_openai.json - ground truth sentiment labels generated using GPT4-o-mini<br /> 
top_k_openai.json - list of top 5 most discussed topics identified using GPT4-o-mini<br /> 

Test Cases and Experiments:<br /> 
1. We have used the topic “apple stock” and estimated the stock trend for the dates ranging from 2024-11-15 to 2024-11-22.<br /> 
2. Perfomance of the model is evaluated using Accuracy metric, with ground truth from GPT4-o-mini.<br /> 
3. System evaluation metrics we have used are Throughput and Memory usage.<br /> 
