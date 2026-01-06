def superman_divide(earth_population, super_speed_factor):
    # Superman tries to calculate some crazy factor
    return earth_population / super_speed_factor  # ZeroDivisionError if factor = 0

def hulk_add_strength(hulk_strength, iron_suit_level):
    # Hulk tries to add his strength to Iron Man suit level
    return hulk_strength + iron_suit_level  # TypeError if iron_suit_level is string

def flash_team_check(avenger_team, avenger_position):
    # Flash tries to access a member of the Avengers
    return avenger_team[avenger_position]  # IndexError if out of range

def batman_justice_lookup(justice_league_roster, hero_name):
    # Batman checks Justice League hero
    return justice_league_roster[hero_name]  # KeyError if hero not found

def doctor_strange_spell_cast(spell_power_input):
    # Doctor Strange tries to cast spell with given power
    return int(spell_power_input)  # ValueError if not a number

def aquaman_swim_attempt(aquaman_ability):
    # Aquaman tries to swim using a non-existent method
    return aquaman_ability.swim()  # AttributeError

def loki_import_trick():
    # Loki tries to import a non-existent module
    import thanos_module  # ImportError
