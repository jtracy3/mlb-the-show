import pandas as pd
import utils
import scrape_community_market_v2 as scm

# column_names_items = ['name', 'rarity', 'team',
#                       'ovr', 'age', 'bat_hand',
#                       'throw_hand', 'stamina', 'pitching_clutch',
#                       'hits_per_bf', 'k_per_bf', 'bb_per_bf',
#                       'hr_per_bf', 'pitch_velocity', 'pitch_control',
#                       'pitch_movement', 'contact_left', 'contact_right',
#                       'power_left', 'power_right', 'plate_vision',
#                       'plate_discipline', 'batting_clutch', 'bunting_ability',
#                       'drag_bunting_ability', 'hitting_durability', 'fielding_ability',
#                       'arm_strength', 'arm_accuracy', 'reaction_time',
#                       'blocking', 'speed', 'baserunning_ability',
#                       'baserunning_aggression']

column_names_prices = ['player', 'overall', 'buy_now',
                       'sell_now', 'series', 'set',
                       'team', 'pos', 'date_ran']

# card_data = utils.get_all_card_items()
# card_df = pd.DataFrame(card_data, columns=column_names_items)

##################################################################
############# I need to fix the community prices #################
##################################################################

card_prices = scm.get_all_card_prices()
card_prices_df = pd.DataFrame(card_prices, columns=column_names_prices)

# make sure the numerics are stored as numerics
card_prices_df['overall'] = card_prices_df['overall'].apply(pd.to_numeric)
card_prices_df['buy_now'] = card_prices_df['buy_now'].apply(pd.to_numeric)
card_prices_df['sell_now'] = card_prices_df['sell_now'].apply(pd.to_numeric)

# arbitrage possibility
card_prices_df['profit'] = card_prices_df['buy_now']*.9 - card_prices_df['sell_now']
card_prices_df['profit_margin'] = card_prices_df['profit'] / card_prices_df['sell_now']

df = card_prices_df.loc[:, ['player','overall','buy_now','sell_now','profit']].sort_values('profit', ascending=False)
df.loc[df['sell_now'] <= 30000]

##################################################################
##################### equipment prices ###########################
##################################################################


column_names_equipment = ['name','buy_now','sell_now',
                          'brand','type','date_ran']

equipment_prices = scm.get_all_equipment_prices()
equipment_prices_df = pd.DataFrame(equipment_prices, columns=column_names_equipment)

equipment_prices_df['buy_now'] = equipment_prices_df['buy_now'].apply(pd.to_numeric)
equipment_prices_df['sell_now'] = equipment_prices_df['sell_now'].apply(pd.to_numeric)

# arbitrage possibility
equipment_prices_df['profit'] = equipment_prices_df['buy_now']*.9 - equipment_prices_df['sell_now']
equipment_prices_df['profit_margin'] = equipment_prices_df['profit'] / equipment_prices_df['sell_now']

equipment_prices_df.loc[:, ['name','buy_now','sell_now','profit','profit_margin']].sort_values('profit', ascending=False)

####################################################################
##################### players to buy back ##########################
####################################################################

players_to_buy_back = ['Rich Gossage', 'Mark Prior', 'Matt Wieters',
                       'Fernando Rodney', 'Ernie Banks', 'Eddie Murray']

prices = card_prices_df.drop_duplicates()
live_series = prices.loc[prices['set'] == '-',:]
live_series = live_series[['players','overall','sell_now','pos','team']]
live_series['projected_sell_now'] = live_series.apply(lambda row: round(row['sell_now'] * .85,0) if row['overall'] > 85 else row['sell_now'], axis=1)
live_series['projected_sell_now_low'] = live_series.apply(lambda row: round(row['sell_now'] * .8,0) if row['overall'] > 85 else row['sell_now'], axis=1)

