import requests
import bs4
from datetime import datetime
from src.models.schemas import MarketData


class ScrapeMarket:

    def __init__(self, type_='mlb_card'):
        self._url = 'https://theshownation.com/mlb' + str(datetime.now().year)[2:] + '/community_market'
        self._type = type_

    def _parse_webpage(self, page):
        page = requests.get(self._url, params={
            'type': self._type, 'page': page, 'hide_trends': 1, 'hide_completed_orders': 1
        })
        return bs4.BeautifulSoup(page.content, 'html.parser')

    def __get_number_pages(self):
        page = self._parse_webpage(1)
        h3 = page.find_all('h3')[0].text.strip()
        total_pages = h3.split()[-1]
        return int(total_pages)

    def _get_table_children(self, page):
        page = self._parse_webpage(page=page)
        cards = page.find_all('table')[0]
        rows = cards.findChildren('tr', recursive=True)
        return rows

    def _gather_market_prices(self, page):
        data = list()
        rows = self._get_table_children(page)
        for row in rows[1:]:
            cells = row.findChildren("td", recursive=False)
            row_list = list()
            ints = [1, 2, 3]  # integer columns
            for i, cell in enumerate(cells[1:]):
                cell_text = cell.text.strip()
                if i in ints:
                    cell_text = int(cell_text)
                row_list.append(cell_text)
            data.append(MarketData(*row_list))
        return data

    def get_market_prices(self):
        data = list()
        page_iter = 1
        total_pages = self.__get_number_pages()
        while page_iter <= total_pages:
            print(f'Page: {page_iter}')
            page_data = self._gather_market_prices(page_iter)
            page_iter += 1
            data.extend(page_data)
        print('Parsed all pages')
        return data


# market = ScrapeMarket()
# market_data = market.get_market_prices()
# # Sort data by profit
# market_data.sort(key=lambda x: x.profit, reverse=True)
#
# # Filter data
# top_gold_arbitrage = list(filter(lambda x: x.rarity == 'Gold', market_data))
# top_diamond_arbitrage = list(filter(lambda x: x.rarity == 'Diamond', market_data))
# top_silver_arbitrage = list(filter(lambda x: x.rarity == 'Silver', market_data))
#
# print('here')
