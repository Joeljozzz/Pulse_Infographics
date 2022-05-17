from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    topheadlines = newsapi.get_top_headlines(sources="business-insider")
    s= 'the-times-of-india',  'bbc-news', 'abc-news','al-jazeera-english', 'ars-technica', 'associated-press', 'bleacher-report', 'bloomberg' ,
    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    links = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        links.append(myarticles['url'])

    mylist = zip(news, desc, img, links)

    return render_template('index.html', context=mylist)




if __name__ == "__main__":
    app.run(debug=True)