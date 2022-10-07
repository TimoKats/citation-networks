from pygooglenews import GoogleNews
import pandas as pd

class data:
    def __init__(self, topic, country, language, amount):
        data = GoogleNews(lang = language, country = country)
        self.amount = amount
        if topic == 'top':
            self.articles = data.top_news()
        else:
            self.articles = data.topic_headlines(topic)

    def sub_articles(self):
        edge_list = pd.DataFrame(columns=['source', 'target'])
        for article in self.articles['entries'][:self.amount]:
            row = {}
            for sub_article in article.sub_articles:
                row['source'] = article['source'].title
                row['target'] = sub_article['publisher']
                if row['source'] != row['target']:
                    edge_list = edge_list.append(row,ignore_index=True)
        return edge_list