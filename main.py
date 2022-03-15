# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists.

# (5 points): As a user, I want a destination to be randomly selected for my day trip.

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

# (10 points): As a user, I want to display my completed trip in the console.

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

import random
destinations = ["Hyrule", "Ocean Biome", "Orgrimmar", "The Mushroom Kingdom", "Disneyworld"]
restaurants = ["Mushroom soup from a mushroom Vendor", "Bread from a villager", "Steak A la Mode from Oribos", "Another Mushroom refernce", "Expensive normal food"]
transports = ["Horse Travel", "Minecart", "Swift Spectral Tiger", "Kart racing on Rainbow Road (Good Luck)", "Normal Bus"]
entertainments = ["Sword fight to the death", "A walk through the nether", "Actually Dieing and visiting the Shadowlands", "Saving a Princess", "A theme park"]
item_list = ["destination", "transportation", "food", "entertainment"]
num_list = [0, 1, 2, 3]
con_list = ["one", "two", "three", "four"]

def greetings():
    print("Welcome to the Day Trip Generator! If you are not sure what you want to do during your day-long trip, then you have come to the right place!")

def destination():
    ran_dest = random.choice(destinations)
    return ran_dest

def transport():
    ran_trans = random.choice(transports)
    return ran_trans

def restaurant():
    ran_rest = random.choice(restaurants)
    return ran_rest

def ent():
    ran_ent = random.choice(entertainments)
    return ran_ent

def ran_app():
    ran_dest = destination()
    ran_trans = transport()
    ran_rest = restaurant()
    ran_ent = ent()
    return [ran_dest, ran_trans, ran_rest, ran_ent]

def ind_con():
    ran_list = ran_app()
    for each in num_list:
        ind_ans = input(f"Does {ran_list[each]} sound good for your {item_list[each]}? Please enter y/n")
        while ind_ans == "n":
            ran_list = ran_app()
            ind_ans = input(f"Does {ran_list[each]} sound good for your {item_list[each]}? Please enter y/n")
        con_list[each] = ran_list[each]
    return [con_list[0], con_list[1], con_list[2], con_list[3]]

def all_con():
    chosen_list = ind_con()
    con_answer = input(f"It looks like you have chosen to spend your day at {chosen_list[0]}. You will travel there via {chosen_list[1]}. While you are there you will have fun while experiencing the {chosen_list[3]}. Afterwards, you will finish the night by eating some delicious {chosen_list[2]}. Does this sound good to you? Please enter y/n")
    while con_answer == "n":
        chosen_list = ind_con()
        con_answer = input(f"It looks like you have chosen to spend your day at {chosen_list[0]}. You will travel there via {chosen_list[1]}. While you are there you will have fun while experiencing the {chosen_list[3]}. Afterwards, you will finish the night by eating some delicious {chosen_list[2]}. Does this sound good to you? Please enter y/n")
    print("Enjoy Your Trip!")

greetings()
all_con()