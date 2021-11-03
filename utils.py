import requests
def get_random_dad_joke():
    url = "https://icanhazdadjoke.com/"
    try:
        answer = requests.get(url, timeout=3, headers={'Accept': 'application/json'}).json()
    except:
        return answer['status']
    return answer['joke']