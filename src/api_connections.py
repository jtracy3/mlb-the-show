import requests
from schemas import PlayerListing


class ListingAPI:
    """ Connect to The Show Nation API for player listings in the community market """

    def __init__(self, year: int):
        self._listing_url = 'https://theshownation.com/mlb' + str(year)[2:] + '/apis/listings.json'

    def get_page_listings(self, params):
        response = requests.get(self._listing_url, params=params)
        listings = response.json()['listings']
        print(f'Processing page {params["page"]}')
        return listings

    def get_all_player_listings(self):
        print('Getting Community Market Player Prices')
        params = {'type': 'mlb_card', 'page': 1}
        all_listings = []
        while True:
            listings = self.get_page_listings(params=params)
            if len(listings) == 0:
                break
            all_listings.extend(listings)
            params['page'] += 1
        return [PlayerListing(**listing_dict) for listing_dict in all_listings]


class ItemsAPI:
    """ Connect to The Show Nation API for items """
    def __init__(self, year: int):
        self._items_url = 'https://theshownation.com/mlb' + str(year)[2:] + '/apis/items.json'


listings_api = ListingAPI(2020)
player_listings = listings_api.get_all_player_listings()
print('here')