import requests
import bs4


class TSNCommunityMarket:

    def __init__(self, year):
        self._year = year
        self._url = 'https://theshownation.com/mlb' + str(year)[2:] + '/community_market'
        print(self._url)

    def _get_page(self):
        page = requests.get(self._url)
        return bs4.BeautifulSoup(page.content, 'html.parser')


market = TSNCommunityMarket(2020)
page_ = market._get_page()
player_cards = page_.find_all('table')[0]
rows = player_cards.findChildren("tr", recursive=True)

for row in rows[1:]:
    # if isinstance(row, bs4.NavigableString):
    #     continue
    cell = row.findChildren("td", recursive=False)
    print(cell)

print('here')
