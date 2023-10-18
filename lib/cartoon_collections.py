def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, 1):
        print(f"{i}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    captain_planet_calls = [call.capitalize() + '!' for call in planeteer_calls]
    return captain_planet_calls


def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False


def find_the_cheese(ingredients):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for ingredient in ingredients:
        if ingredient in cheese_types:
            return ingredient
    return None

