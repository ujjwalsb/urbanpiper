
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.shortcuts import render
from aylienapiclient import textapi
from .models import hackerNewsAPI
from operator import itemgetter
from django.db.models import Q
import requests
import json


headers = {
    'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

sentiment_app_id = "de4c997b"
sentiment_api_key = "fe3100503897f9b3da5d85ed7d2437c4"
base_item_url = "https://hacker-news.firebaseio.com/v0/item/"
end_point_url = ".json"

topstories_link_ids = 'https://hacker-news.firebaseio.com/v0/topstories.json'
response = requests.request("GET", topstories_link_ids, headers=headers)

topstories_ids = json.loads(response.text)
# top_30_ids = topstories_ids[:30]              // To fetch from top 30 news only.

def newslist(request):
    # for ids in top_30_ids:                    // If fetching from top 30 items
    for ids in topstories_ids:
        if not hackerNewsAPI.objects.filter(article_id=ids).exists():
            neswdetails_base_link = base_item_url+str(ids)+end_point_url
            details_response_request = requests.request("GET", neswdetails_base_link, headers=headers)
            details_response = json.loads(details_response_request.text)
            client = textapi.Client(sentiment_app_id, sentiment_api_key)
            sentiment_dict = client.Sentiment({'text': details_response.get('title')})
            sentiment = sentiment_dict.get('polarity')
            hackerNewsAPI.objects.create(article_id=details_response.get('id'), 
                                        username=details_response.get('by'), 
                                        title=details_response.get('title'), 
                                        url=details_response.get('url'), 
                                        score=details_response.get('score'),
                                        sentiment=sentiment
                                        )
        else:
            pass

    queryset_list = hackerNewsAPI.objects.all()
    paginator = Paginator(queryset_list, 30)
    page = request.GET.get('page')
    queryset = paginator.get_page(page)

    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(Q(title__icontains=query)).distinct()
        paginator = Paginator(queryset_list, 30)
        page = request.GET.get('page')
        queryset = paginator.get_page(page)

    context = {
        'queryset': queryset
    }
    return render(request, "newslist.html", context)

