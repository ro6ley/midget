from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import logging
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


from .shortener import create_url


redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)
url_validator = URLValidator()
logger = logging.getLogger(__name__)


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

            logger.info("| Operation=ShortenURL | ResponseCode=201 | ResponseMsg=Shortened {} to {} | Status=success |".format(
                request.data['url'], response['url']))
            return Response(response, status=201)
        except ValidationError:
            response = {
                'status': 'error',
                'msg': 'Invalid URL. Check and try again.'
            }
            logger.error("| Operation=ShortenURL | ResponseCode=400 | ResponseMsg=Cannot shorten {} | Status=error |".format(
                request.data['url']))
            return Response(response, status=400)

    # DELETE action to purge a short url
    elif request.method == "DELETE":
        if redis_instance.get(link):
            redis_instance.delete(link)
            logger.info(
                "| Operation=DeleteURL | ResponseCode=204 | ResponseMsg=Deleted {} | Status=success |".format(link))
            return Response({'status': 'success', 'msg': 'Deleted.'},
                            status=204)
        else:
            logger.info(
                "| Operation=DeleteURL | ResponseCode=404 | ResponseMsg=Could not delete {} | Status=error |".format(link))
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
            logger.info(
                "| Operation=GetAllURLs | ResponseCode=200 | ResponseMsg=Fetched {} urls | Status=success |".format(count))
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
                logger.info("| Operation=GetURL | ResponseCode=200 | ResponseMsg=Fetched long URL \'{}\' for \'{}\'  | Status=success |".format(
                    long_url.decode("utf-8"), link))
                return HttpResponseRedirect(long_url)
            else:
                response = {
                    'msg': 'Not found.',
                    'status': 'error'
                }
                logger.error(
                    "| Operation=GetURL | ResponseCode=404 | ResponseMsg=Cannot find long_url for {} | Status=error |".format(link))
                return Response(response, status=404)
