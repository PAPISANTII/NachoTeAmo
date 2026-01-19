import requests

def test_dog_api():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    data = response.json()
    print(response.status_code)
    print(data)