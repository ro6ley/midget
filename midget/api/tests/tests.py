import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


# Create your tests here.
class ShortenerTestCases(TestCase):
    """
    Tests for the shortener project
    """

    def setUp(self):
        """
        Define the test client and initial variables for the test suite
        """
        self.client = APIClient()
        self.url = '/api/links/'
    
    def test_shorten_url(self):
        """
        Test that a URL can be shortened
        """
        response = self.client.post(self.url, {"url": "http://google.com"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fetch_url(self):
        """
        Test that when a shortened URL is accessed, we redirect the user to
        the full URL
        """
        response = self.client.post(self.url, {"url": "http://google.com"})
        # Confirm that it has been created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        fetch_response = self.client.get('/{}'.format(response.data['url']))
        # Confirm that it returns a redirect
        self.assertEqual(fetch_response.status_code, status.HTTP_302_FOUND)
    
    def test_shorten_invalid_url(self):
        """
        Test that shortening an invalid URL raises an error
        """
        response = self.client.post(self.url, {"url": "www.google.com"})
        # Confirm that it has not been created
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('status'), "error")

    def test_fetch_all_links(self):
        """
        Test that all the urls in the redis store can be fetched
        """
        self.client.post(self.url, {"url": "http://google.com"})
        response = self.client.get('/all')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('status'), "success")
        self.assertTrue(response.data.get('count'))

    def test_delete_url(self):
        """
        Test that a shortened url can be deleted
        """
        creation_response = self.client.post(self.url, {"url": "http://google.com"})
        created_url = creation_response.data.get('url')
        print(created_url)

        response = self.client.delete('/{}'.format(created_url))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data.get('status'), "success")     
