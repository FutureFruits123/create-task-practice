#The Restaurant Ranker takes a user input and asks questions in order to determine
#where that input should be placed in a list.
restaurants = ["In-N-Out", "Five Guys", "Cheesecake Factory", "Jack in the Box"]

def ranker(new_restaurant):
  x = 0
  y = len(restaurants)

  for i in restaurants:
    choice = input("Do you prefer " + restaurants[x] + " or " + new_restaurant).lower()
    if choice == new_restaurant.lower():
     restaurants.insert(x, new_restaurant)
     print("Your updated restaurants ranking is: " + str(restaurants))
     break
    elif choice == restaurants[x].lower() and x < y:
      x = x + 1
      if x == y:
        restaurants.append(new_restaurant)
        print("Your updated restaurants ranking is: " + str(restaurants))
        break
    else:
      print("error")
      break

ranker(input("Hello user, this is the Restaurant Ranker! What restaurant would you like to add to the list?"))
#^ function called ^