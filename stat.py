from urllib.parse import urlparse
import requests
import constant
import sys

GITHUB_API_URL = "https://api.github.com"

def get_repo_path(args):
    clone_url = args[1]
    parsed_url = urlparse(clone_url)
    path = str(parsed_url.path)
    path = path[:-4]
    
    return path


def build_query_url(path):
    return GITHUB_API_URL + "/repos" + path

def make_api_call(url):
    req = requests.get(url)
    resp = None

    try:
        resp = req.json()
    except Exception as e:
        print("ValueError: No JSON object could be decoded")
    return resp

def print_response(resp):
    print("Repository: " + resp['name'])
    print("Description: " + resp['description'])
    print("Language: " + resp['language'])
    print("Size: " + str(int(resp['size']) / 1000) + " MB")
    print("Stars: " + str(resp['stargazers_count']))
    print("Watchers: " + str(resp['watchers_count']))
    print("Forks: " + str(resp['forks']))


def main():
    print_response(make_api_call(build_query_url(get_repo_path(sys.argv))))



if __name__ == "__main__":
    main()
