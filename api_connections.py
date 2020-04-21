import requests
from datetime import datetime
from src.models.schemas import PlayerListing, PlayerStats
import time
import csv

class ListingAPI:
    """ Connect to The Show Nation API for player listings in the community market """

    def __init__(self):
        self._listing_url = 'https://theshownation.com/mlb' + str(datetime.now().year)[2:] + '/apis/listings.json'

    def __get_listings(self, params):
        """
        Get player listings by page
        Args:
            params (dict) : contains query parameters for request
        Return:
             listings(list(dict)) : json response containing player listings
        """
        response = requests.get(self._listing_url, params=params)
        listings = response.json()['listings']
        print(f'Processing page {params["page"]}')
        return listings

    def get_all_player_listings(self):
        """
        Get all listings on Community Market by player
        Return:
            List(PlayerListing) : List of PlayerListing objects
        """
        print('Getting Community Market Player Prices')
        params = {'type': 'mlb_card', 'page': 1}
        all_listings = []
        start = time.time()
        while True:
            listings = self.__get_listings(params=params)
            if len(listings) == 0:
                break
            all_listings.extend(listings)
            params['page'] += 1
        stop = time.time()
        print(f'Processing time {stop - start}s')
        return [PlayerListing(**listing_dict) for listing_dict in all_listings]


class ItemsAPI:
    """ Connect to The Show Nation API for items """

    def __init__(self):
        self._items_url = 'https://theshownation.com/mlb' + str(datetime.now().year)[2:] + '/apis/items.json'

    def __get_player_stats(self, params):
        """
        Get player listings by page
        Args:
            params (dict) : contains query parameters for request
        Return:
             items(list(dict)) : json response containing player stats
        """
        response = requests.get(self._items_url, params=params)
        items = response.json()['items']
        print(f'Processing page {params["page"]}')
        return items

    def get_all_player_listings(self):
        """
        Get all listings on Community Market by player
        Return:
            List(PlayerListing) : List of PlayerListing objects
        """
        print('Getting Player Stats')
        params = {'type': 'mlb_card', 'page': 1}
        all_player_stats = []
        start = time.time()
        while True:
            player_stats = self.__get_player_stats(params=params)
            if len(player_stats) == 0:
                break
            all_player_stats.extend(player_stats)
            params['page'] += 1
        stop = time.time()
        print(f'Processing time {stop - start}s')
        return [PlayerStats(**player_dict) for player_dict in all_player_stats]

    @staticmethod
    def to_csv(self):
        with open('mlb_the_show_players.csv', 'w', newline='') as csvfile:
            fieldnames = player_stats[0].__dict__.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for player in player_stats:
                writer.writerow(player.__dict__)

# listings_api = ListingAPI()
# player_listings = listings_api.get_all_player_listings()
# player_listings.sort(key=lambda x: x.profit, reverse=True)
#
# middle_buy_class = list(filter(lambda x: x.buy_class == '10k to 25k', player_listings))
# middle_low_buy_class = list(filter(lambda x: x.buy_class == '1k to 10k', player_listings))
# silver_buy_class = list(filter(lambda x: x.buy_class == '1k and less', player_listings))
#
# print('here')
