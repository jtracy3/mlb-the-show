from dataclasses import dataclass, field
from typing import List


@dataclass
class PlayerListing:
    name: str
    best_sell_price: int
    best_buy_price: int
    profit: float = field(init=False)
    profit_ratio: float = field(init=False)

    def __post_init__(self):
        self.profit = self.__calc_profit()
        self.profit_ratio = self.__calc_profit_ratio()

    def __calc_profit(self):
        """Calculate arbitrage profit of buying and selling"""
        return round(self.best_sell_price*0.90 - self.best_buy_price, 3)

    def __calc_profit_ratio(self):
        """Calculate profit ratio, profit / investment"""
        try:
            profit_ratio = round(self.__calc_profit() / self.best_buy_price, 3)
        except ZeroDivisionError:
            profit_ratio = None
        return profit_ratio


@dataclass
class MarketData:
    name: str
    overall: int
    rarity: str = field(init=False)
    buy_now_price: int
    sell_now_price: int
    profit: float = field(init=False)
    profit_ratio: float = field(init=False)
    series: str
    set: str
    team: str
    pos: str

    def __post_init__(self):
        self.profit = self.__calc_profit()
        self.profit_ratio = self.__calc_profit_ratio()
        self.rarity = self.__get_rarity()

    def __calc_profit(self):
        """Calculate arbitrage profit of buying and selling"""
        return round(self.buy_now_price*0.90 - self.sell_now_price, 3)

    def __calc_profit_ratio(self):
        """Calculate profit ratio, profit / investment"""
        try:
            profit_ratio = round(self.__calc_profit() / self.sell_now_price, 3)
        except ZeroDivisionError:
            profit_ratio = None
        return profit_ratio

    def __get_rarity(self):
        if self.overall > 84:
            return 'Diamond'
        elif self.overall > 79:
            return 'Gold'
        elif self.overall > 74:
            return 'Silver'
        elif self.overall > 64:
            return 'Bronze'
        else:
            return 'Common'

@dataclass
class Pitches:
    name: str
    speed: int
    control: int
    movement: int


@dataclass
class PlayerStats:
    name: str
    rarity: str
    team: str
    ovr: int
    age: int
    bat_hand: str
    throw_hand: str
    stamina: int
    pitching_clutch: int
    hits_per_bf: int
    k_per_bf: int
    bb_per_bf: int
    hr_per_bf: int
    pitch_velocity: int
    pitch_control: int
    pitch_movement: int
    contact_left: int
    contact_right: int
    power_left: int
    power_right: int
    plate_vision: int
    plate_discipline: int
    batting_clutch: int
    bunting_ability: int
    drag_bunting_ability: int
    hitting_durability: int
    fielding_ability: int
    arm_strength: int
    arm_accuracy: int
    reaction_time: int
    blocking: int
    speed: int
    baserunning_ability: int
    baserunning_aggression: int
    pitches: List[Pitches]
