#!/usr/bin/env python
import urllib2, json

# http://docs.themoviedb.apiary.io/

def api2data(id,x):
    request = urllib2.Request("http://api.themoviedb.org/3/movie/%s?api_key=%s&language=es" % (id,'YOUR_API_KEY_HERE'), headers={"Accept" : "application/json"})
    response = urllib2.urlopen(request).read()
    data = json.loads(response)
    return data[x]


def api2img(id,x):
    # ['poster_path','backdrop_path']
    base_url="http://image.tmdb.org/t/p/w500"
    #secure_base_url="https://d3gtl9l2a4fn1j.cloudfront.net/t/p/"
    request = urllib2.Request("http://api.themoviedb.org/3/movie/%s?api_key=%s&language=es" % (id,'YOUR_API_KEY_HERE'), headers={"Accept" : "application/json"})
    response = urllib2.urlopen(request).read()
    data = json.loads(response)
    return base_url + data[x]
