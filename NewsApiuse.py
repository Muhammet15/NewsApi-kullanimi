from newsapi import NewsApiClient
import datetime

YOURAPIKEY='';
newsapi = NewsApiClient(api_key=YOURAPIKEY)
simdikizaman= datetime.datetime.now()
text = str(simdikizaman)
print(text[:10]) #şimdiki zaman için hep güncel haberler

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          #category='sports',
                                          language='en',
                                          #country='us',
                                          )
# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      from_param=text[:10],
                                      to=text[:10],
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
# /v2/top-headlines/sources
selfd = newsapi.get_sources()
diziurl=[]
dizidescription=[]
dizicategory=[]
dizitittle=[]
for i in all_articles['articles']:
    dizitittle.append(i['title'])
    diziurl.append (i['url'])
    dizidescription.append(i['description'])
    #dizicategory.append(i['category'])

print (diziurl[0]+ " -- " + dizidescription[0])

