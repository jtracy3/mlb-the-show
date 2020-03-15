""" Test shit """
import os
import pickle


def unpickle_it(file):
    if os.path.exists(file):
        with open(file, 'rb') as f:
            return pickle.load(f)


if __name__ == '__main__':
    player_listings = unpickle_it('cache.pkl')
    player_profits = [(listing.name,
                       listing.best_buy_price,
                       listing.best_sell_price,
                       listing.profit(),
                       listing.profit_ratio()) for listing in player_listings]
    player_profits.sort(key=lambda x: x[3], reverse=True)
    print('here')
