from src.community_market import ScrapeMarket


def main():
    market = ScrapeMarket()
    return market.get_market_prices()


if __name__ == '__main__':
    main()
