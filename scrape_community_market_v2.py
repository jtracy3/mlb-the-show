import requests
import datetime
from bs4 import BeautifulSoup

# somehow I'm getting duplicate rows, when it's run at different times
# I want this behavior but I have no idea why it's doing that right now

def parse_them_rows(page_number, type_id):

    # url = 'https://mlb19.theshownation.com/community_market' + str(page_number) + '&type_id=0'
    url = 'https://mlb19.theshownation.com/community_market?page=' + str(page_number) + '&type_id=' + str(type_id)

    # Create a handle, page, to handle the contents of the website

    page = requests.get(url)
    # Store the contents of the website under doc
    soup = BeautifulSoup(page.content, 'html.parser')


    cards_table = soup.find_all("table", class_="items-results-table")[0]
    rows = cards_table.findChildren("tr", recursive=True)
    table = list()

    for row in rows[1:]:
        cells = row.findChildren("td", recursive=False)
        row_list = list()
        date_list = list()
        date_list.append(datetime.datetime.now())  # timestamp when this was ran to compare older prices

        for cell in cells:
            cell_text = cell.text.strip()
            if len(cell_text) > 0:
                row_list.append(cell_text)
        table.append(row_list + date_list)

    # print(table)

    return table

# if __name__ == '__main__':
#     parse_them_rows()

# really slow, should multiprocess
def get_all_card_prices():
    '''
    :return:
    '''
    print('Please wait as we gather card prices...')
    data = list()
    i = 1

    while True:
        try:
            data_ = parse_them_rows(page_number=i, type_id=0)
        except:
            break

        for d in data_:
            data.append(d)

        i += 1

    return data

# really slow, should multiprocess
def get_all_equipment_prices():
    '''
    :return:
    '''
    print('Please wait as we gather equipment prices...')
    data = list()
    i = 1

    while True:
        try:
            data_ = parse_them_rows(page_number=i, type_id=2)
        except:
            break

        for d in data_:
            data.append(d)

        i += 1

    return data