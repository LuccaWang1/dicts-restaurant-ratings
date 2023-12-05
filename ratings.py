"""Restaurant rating lister: List the restaurants and their ratings, then prompt the user to add a restaurant with a rating they give that restaurant"""

data = open("scores.txt")

restaurant_ratings_dict = {}

for line in data: 
    words = line.rstrip().split(":")
    restaurant = words[0]
    rating = words[1]
    restaurant_ratings_dict[restaurant] = rating

restaurant_ratings_dict = sorted(restaurant_ratings_dict.items(), reverse=False)

print(restaurant_ratings_dict)

restaurant_ratings_list = []

for tup in restaurant_ratings_dict:
    tups_as_lists = list(tup)
    restaurant_ratings_list.append(tups_as_lists)

print(restaurant_ratings_list)

for list in restaurant_ratings_list:
    restaurant = list[0]
    rating = list[1]
    rating = str(rating)
    print(f'{restaurant} is at rating {rating}.')

user_input = input("What restaurant would you like to add?")
user_rating = input("What rating on a scale of 1-10 do you give this restaurant?")

restaurant_ratings_list.append([user_input, user_rating])
restaurant_ratings_list = sorted(restaurant_ratings_list)
restaurant_ratings_dict = dict(restaurant_ratings_list)

print(restaurant_ratings_dict)