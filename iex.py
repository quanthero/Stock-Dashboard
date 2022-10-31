import requests

class IEXStock:

    def __init__(self, token, symbol):
        self.BASE_URL = 'https://cloud.iexapis.com/v1'

        self.token = token
        self.symbol = symbol

    def get_logo(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/logo?token={self.token}"
        r = requests.get(url)
        
        return r.json()

    def get_company_info(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/company?token={self.token}"
        r = requests.get(url)

        return r.json()

    def get_stats(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/stats?token={self.token}"
        r = requests.get(url)

        return r.json() 

    def get_company_news(self, last=20):
        url = f"{self.BASE_URL}/stock/{self.symbol}/news/last/{last}?token={self.token}"
        r = requests.get(url)

        return r.json()

    def get_institutional_ownership(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/institutional-ownership?token={self.token}"
        r = requests.get(url)

        return r.json()

    def get_insider_transactions(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/insider-transactions?token={self.token}"
        r = requests.get(url)

        return r.json()

    def get_HISTORICAL_PRICES_FOR_1_MONTH(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/chart/6m?token={self.token}"
        r = requests.get(url)

        return r.json()
        
