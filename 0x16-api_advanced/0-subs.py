#!/usr/bin/python3
"""This function queries the Reddit API 
    and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    number_of_subscribers returns the total number of subscribers 
    """
    # Construct the URL for the Reddit API
    given_apiurl = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Define headers for the HTTP request
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    # Make a GET request to the Reddit API
    http_response = requests.get(given_apiurl, headers=headers, allow_redirects=False)
    # Check if the subreddit exist or not.
    if http_response.status_code == 404:
        return 0
    result = http_response.json().get("data")
    # Return the number of subscribers
    return result.get("subscribers")