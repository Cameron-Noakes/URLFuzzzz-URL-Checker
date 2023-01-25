import requests

# AUTHOR: Cameron Noakes
# Had time to experiment with cool pen testing tool development to potentially
# help me in the future when performing security engineering tasks.

# base URL to target
base_url = "http://www.example.com"

# list of endpoint strings to test
endpoints = ["/test1", "/test2", "/test3", "/admin", "/secure"]

# iterate through the endpoints
for endpoint in endpoints:
    # send a GET request to the full URL
    url = base_url + endpoint
    response = requests.get(url)

    # check the status code of the response
    if response.status_code == 200:
        print(f"Endpoint found: {url}")
    else:
        print(f"Endpoint not found: {url}")

