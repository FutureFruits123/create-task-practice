restaurants = ["In-N-Out", "Five Guys", "Cheesecake Factory", "Jack in the Box"]

new_restaurant = input("What restaurant would you like to add to the list?")

def restaurant_sorter(new_restaurant):
    print("Your updated restaurants ranking is: " + str(restaurants))

"""
choice1 = input("Do you prefer " + restaurants[0] + " or " + new_restaurant).lower()

if choice1 == new_restaurant.lower():
  restaurants.insert(0, new_restaurant)
elif choice1 == restaurants[0].lower():
  choice2 = input("Do you prefer " + restaurants[1] + " or " + new_restaurant)

  if choice2 == new_restaurant.lower():
    restaurants.insert(1, new_restaurant)
  elif choice2 == restaurants[1].lower():
    choice3 = input("Do you prefer " + restaurants[2] + " or " +           
  new_restaurant)

    if choice3 == new_restaurant.lower():
      restaurants.insert(2, new_restaurant)
    elif choice3 == restaurants[2].lower():
      choice4 = input("Do you prefer " + restaurants[3] + " or " +         
    new_restaurant)

      if choice4 == new_restaurant.lower():
        restaurants.insert(3, new_restaurant)
      elif choice4 == restaurants[3].lower():
        restaurants.insert(4, new_restaurant)
      else:
        print("error")
        
    else:
      print("error")
    
  else:
    print("error")
else:
  print("error")
"""
