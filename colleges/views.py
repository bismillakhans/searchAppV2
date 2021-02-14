from django.shortcuts import render
from django.http import JsonResponse
from elasticsearch_dsl import Search, Q
from elasticsearch import Elasticsearch

# Create your views here.
def index(request):
    return render(request,"index.html")

def suggest(request):
    key_words = request.GET.get('queryString', '')
    resp_data=[]
    
    
    
    client = Elasticsearch()
    # q = Q("bool", should=Q("match", college_name=key_words),minimum_should_match=1)
    # s = Search(using=client, index="colleges").query(q)[0:10]
    # search = Search(index='colleges')
    # s = search.filter('match', city_name=key_words)
    # s = s.suggest('my_suggestion', 'pyhton', term={'field': 'title'})
    # response=s.execute()
    res = client.search(index="colleges", body={"suggest": {"field-suggest" : {"prefix" : key_words,"completion" : {"field" : "city_name.suggest","fuzzy" : {"fuzziness" : 1 } }}}})
    response=res["suggest"]['field-suggest'][0]['options']

    for hit in response:  
        data_with_id= str(hit['_source']['id'])+'----'+hit['_source']['college_name'] 
        resp_data.append(data_with_id)  

    return JsonResponse(resp_data, safe=False)