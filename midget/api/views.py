from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


from .shortener import create_url


redis_instance = redis.StrictRedis(host='localhost', port=6379, db=0)
url_validator = URLValidator()


@api_view(['GET', 'POST', 'DELETE'])
def manage_links(request, link=None, *args, **kwargs):
    # POST action to create a short url
    if request.method == "POST":
        try:
            url_validator(request.data['url'])
            response = {
                'url': create_url(request.data['url']),
                'status': 'success',
                'msg': 'Created'
                }
            return Response(response, status=201)            
        except ValidationError:
            response = {
                'status': 'error',
                'msg': 'Invalid URL. Check and try again.'
                }
            return Response(response, status=400)


    # DELETE action to purge a short url
    elif request.method == "DELETE":
        if redis_instance.get(link):
            redis_instance.delete(link)
            return Response({'status': 'success', 'msg': 'Deleted.'},
                            status=204)
        else:
            return Response({'status': 'error', 'msg': 'Not found.'},
                            status=404)

    # GET action to get all links or just one link
    elif request.method == "GET":
        if link == 'all':
            links = {}
            count = 0
            for key in redis_instance.keys("*"):
                links[key.decode("utf-8")] = redis_instance.get(key)
                count += 1
            
            response = {
                    'count': count,
                    'msg': 'Found.',
                    'status': 'success',
                    'links': links
                }
            return Response(response, status=200)
        elif link != 'all':
            # Fetch the single url and return a redirect
            long_url = redis_instance.get(link)
            if long_url:
                response = {
                    'msg': 'Found.',
                    'status': 'success',
                    'link': long_url
                }
                return HttpResponseRedirect(long_url)
            else:
                response = {
                    'msg': 'Not found.',
                    'status': 'error'
                }
                return Response(response, status=404)
        else:
            # Redirect to home
            response = {
                'msg': 'Welcome to mdgt.url',
                'status': 'success'
            }
            return Response(response, status=200)
