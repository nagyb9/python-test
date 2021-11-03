import requests
def get_random_dad_joke():
    url = "https://icanhazdadjoke.com/"
    answer = requests.get(url, timeout=3, headers={'Accept':'application/json'}).json()
    print(answer)
    try:
        return answer['joke']
    except:
        return answer['status']
