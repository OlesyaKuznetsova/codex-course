
import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name():
    return random.choice(prefixes) + ' ' + random.choice(suffixes)


def capitalize_suffix(suffix):
    return suffix.capitalize()


capitalized_suffixes = list(map(capitalize_suffix, suffixes))


random_names = [create_fantasy_name() for _ in range(10)]


def fire_in_name(name):
    return 'Fire' in name


filtered_names = list(filter(fire_in_name, random_names))


def concatenate_names(name1, name2):
    return name1 + ' | ' + name2


if filtered_names:  
    reduced_names = reduce(concatenate_names, filtered_names)
else:
    reduced_names = "No names with 'Fire'"


def display_name_info():
    print("🔹 Generated names:")
    for name in random_names:
        print(name)

    print("\n Names containing 'Fire':")
    print(filtered_names if filtered_names else "No names with 'Fire'")

    print("\n Concatenated names:")
    print(reduced_names)


display_name_info()
