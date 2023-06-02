import requests

class WordpressAuth:

    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def get_token(self, username, password):
        response = requests.post(
            f'{self.base_url}/wp-json/jwt-auth/v1/token',
            data={'username': username, 'password': password},
            headers={'X-API-KEY': self.api_key}
        )
        if response.status_code == 200:
            return response.json()['token']
        else:
            return None

    def verify_token(self, token):
        response = requests.post(
            f'{self.base_url}/wp-json/jwt-auth/v1/token/validate',
            headers={'Authorization': f'Bearer {token}', 'X-API-KEY': self.api_key}
        )
        return response.status_code == 200
