#!/usr/bin/python3
"""This Python script prints the titles of the
    top 10 hot posts from a specified subreddit."""
import requests


def top_ten(subreddit):
    """
    top_ten Print the titles of the 10 hottest
    posts on a given subreddit
    """
    # Construct the URL for the Reddit API
    given_apiurl = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    # Define headers for the HTTP request
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    # Set parameters for the request
    request_param = {
        "limit": 10
    }
    # Make a GET request to the Reddit API
    http_response = requests.get(
            given_apiurl,
            headers=headers,
            params=request_param,
            allow_redirects=False
    )
    # Check if the subreddit exist or not.
    if http_response.status_code == 404:
        print("None")
        return
    result = http_response.json().get("data")
    # print the title of each one
    [print(c.get("data").get("title")) for c in result.get("children")]
