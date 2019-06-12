import requests
import json

def get_the_goods(type, page, ITEMS=True):

    VALUE = 'items'

    if not ITEMS:
        VALUE = 'listings'

    params = {
        'type': type,
        'page': page
    }

    URL = 'https://mlb19.theshownation.com/apis/' + VALUE + '.json'

    # Create a handle, page, to handle the contents of the website
    response = requests.get(URL, params=params)
    dict_response = json.loads(response.content)
    data = list()

    for dict in dict_response['listings']:
        data_to_add = tuple(dict.values())
        data.append(data_to_add)

    return data

# if __name__ == '__main__':
#     get_the_goods()

# this is really slow, I should multiprocess this

def get_all_card_items():

    print('Please wait as we gather card data...')
    data = list()
    i = 1

    while True:

        data_ = get_the_goods('MLB_Cards', page=i, ITEMS=True)

        if len(data_) == 0:
            break

        for d in data_:
            data.append(d)

        # print(i)

        i += 1

    return data

# def get_all_card_listings():
#
#     data = list()
#     i = 1
#
#     while True:
#
#         data_ = get_the_goods('MLB_Cards', page=i, ITEMS=False)
#
#         if len(data_) == 0:
#             break
#
#         for d in data_:
#             data.append(d)
#
#         # print(i)
#
#         i += 1
#
#     return data

def get_all_stadium_items():

    data = list()
    i = 1

    while True:

        data_ = get_the_goods('Stadium', page=i, ITEMS=True)

        if len(data_) == 0:
            break

        for d in data_:
            data.append(d)

        i += 1

    return data

def get_all_equipment_items():

    data = list()
    i = 1

    while True:

        data_ = get_the_goods('Equipment', page=i, ITEMS=True)

        if len(data_) == 0:
            break

        for d in data_:
            data.append(d)

        i += 1

    return data

def get_all_sponsorship_items():

    data = list()
    i = 1

    while True:

        data_ = get_the_goods('Sponsorship', page=i, ITEMS=True)

        if len(data_) == 0:
            break

        for d in data_:
            data.append(d)

        i += 1

    return data