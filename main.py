from car_wishlist import CarWishlist

wishlist = CarWishlist()
wishlist.load()

input("=====Welcome to the Car Wishlist=====\nPress Enter to continue...")
while True:
    print("===What would you like to do?====")
    print("====(A)dd to the wishlist====")
    print("====(R)emove a car from  the wishlist====")
    print("====(V)iew cars in wishlist====")
    print("====(Q)uit Car Wishlist====\n\n")

    choice = input('Enter your Selection: ').upper()

    if choice == "A":
        wishlist.add_car()
    elif choice == "R" :
        wishlist.remove_car()
    elif choice == "V" :
        wishlist.view_wishlist()
    elif choice == "Q":
        wishlist.save()
        break