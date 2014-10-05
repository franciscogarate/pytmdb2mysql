#!/usr/bin/env python
import urllib2, json

# http://www.themoviedb.org/talk/51f0302a19c2957cfd0656e6
# http://docs.themoviedb.apiary.io/
"""
"images": {
        "base_url": "http://d3gtl9l2a4fn1j.cloudfront.net/t/p/",
        "secure_base_url": "https://d3gtl9l2a4fn1j.cloudfront.net/t/p/",
        "poster_sizes": [
            "w92",
            "w154",
            "w185",
            "w342",
            "w500",
            "original"
            
DATOS:
"backdrop_path"
"genres":[{"id":35,"name":"Comedy"}]
"id":43294,
"imdb_id":"tt0046705",
"original_title":"Un Americano a Roma",
"overview"?
"poster_path":"/kjq7qCywBHGvoU98jgE4TrDlYHQ.jpg",
"production_countries"
"release_date":"1954-01-01",
"runtime":94,
"title":"An American in Rome",
"vote_average":10.0
            
"""
import urllib2

def api2data(id,x):
    request = urllib2.Request("http://api.themoviedb.org/3/movie/%s?api_key=%s&language=es" % (id,'YOUR_API_KEY_HERE'), headers={"Accept" : "application/json"})
    response = urllib2.urlopen(request).read()
    data = json.loads(response)
    return data[x]


def api2img(id,x):
    base_url="http://d3gtl9l2a4fn1j.cloudfront.net/t/p/w500"
    request = urllib2.Request("http://api.themoviedb.org/3/movie/%s?api_key=%s&language=es" % (id,'YOUR_API_KEY_HERE'), headers={"Accept" : "application/json"})
    response = urllib2.urlopen(request).read()
    data = json.loads(response)
    return base_url + data[x]

# Testing:
#print api2data2(550,'title')
#
#datos = ['poster_path','vote_average']
#for i in datos:
#    try:
#        print api2img(550,i)
#    except:
#        pass