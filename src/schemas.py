from dataclasses import dataclass
from typing import List


@dataclass
class PlayerListing:
    name: str
    best_sell_price: int
    best_buy_price: int

    def calc_profit(self):
        return self.best_buy_price*0.10 - self.best_sell_price


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