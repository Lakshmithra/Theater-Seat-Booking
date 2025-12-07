"""
Cinema Seat Booking System

A Python console application for booking and managing movie theater seats
with color-coded seating and persistent storage of seat layouts.

Author: R.Lakshmithra
Date: 07-12-2025
"""

import os

# Importing colorama library to print colored text in the console
from colorama import init , Fore , Style 

# Initialize colorama with autoreset so colors reset automatically after each print
init(autoreset = True)

movies = ["Squid Game" , "Stranger Things"]
show_times = ["10.00 A.M" , "1.30 P.M" , "5.00 P.M"]
seat_types = {'A':'Platinum','B':'Platinum','C':'Platinum','D':'Gold','E':'Gold','F':'Gold','G':'Silver','H':'Silver','I':'Silver','J':'Silver'}
seat_price = {'Platinum':300, 'Gold':200 , 'Silver':150}
rows = ['A','B','C','D','E','F','G','H','I','J']
cols = [1,2,3,4,5,6,7,8,9,10]
movie = ""
show = ""
file = None   # Will store the filename corresponding to the selected movie and showtime
movie_selected = False
seat_layout = []

def load_seat_layout(file):
    
    # use the global seat_layout so changes affect the whole program
    global seat_layout

    # check if saved layout exists for this movie & showtime
    if os.path.exists(file):

        seat_layout = []
        with open(file , "r") as f:
            lines = f.readlines()
            for i , line in enumerate(lines):
                if i >= 10:                     # ensure we only read 10 rows even if file has extra lines
                    break
                row = line.strip().split()      # convert line into list of seats
                while len(row)<10:
                    row.append('O')             # pad row to 10 seats if some are missing
                seat_layout.append(row)

    # if no file exists, create new 10x10 layout of open seats        
    else: 
        seat_layout = [['O'] * 10 for _ in range(10)]
        save_seat_layout(file)   # save this new layout for future use

def save_seat_layout(file):
    # ensure we access the current seat layout of the program
    global seat_layout
    with open(file , "w") as f: # open file in write mode, overwriting existing layout
        for row in seat_layout:
            f.write(" ".join(row) + "\n") # convert row list to string and write to file

def display_movies_showtimes():
    
    print("\nAvailable movies : ")
    for i , j in enumerate(movies,1):
        print(f"{i}.{j}")
    try:
        
        movie_choice = int(input("\nSelect your movie (1-2): "))
        selected_movie = movies[movie_choice-1]
    except:
        print("ERROR ! Invalid Choice")
        return display_movies_showtimes()
    
    print(f"\nAvailable show times for {selected_movie}")
    for i , j in enumerate(show_times , 1):
        print(f"{i}.{j}")
        
    try:
        
      show = int(input("\nSelect your showtime(1-3) : "))
      selected_show = show_times[show-1]
    except:
        print("ERROR ! Invalid Choice")
        return display_movies_showtimes()

    movie_name = selected_movie.replace(" " ,"")
    show_name = selected_show.replace(" ","").replace(":" , "").replace(".","")
    file_name = movie_name + "_" + show_name

    return selected_movie , selected_show , file_name
           

def display_seats(file):

    seat_colors = {'Platinum': Fore.MAGENTA, 'Gold': Fore.YELLOW , 'Silver': Fore.CYAN}
    print("\nPlatinum (A - C) - 300\tGold (D - F) - 200\tSilver (G - J) - 150\n")

    # Printing column numbers
    print("    ", end ="")
    for i in cols:
        print(f"{i:^4}",end = "  ")
    print()

    # Printing row with seats

    for i in range(10):
        print(f"{rows[i]:<4}", end = "")
        for j in seat_layout[i]:
            seat_type = seat_types[rows[i]]   # get type based on row
            color = seat_colors[seat_type]    # get color for that type
            print(f"{color}{j:^4}\033[0m", end = "  ")
        print()

def booking_seats(file):

     n = int(input("\nEnter number of seats to be booked : "))
     total_amount = 0
     booked_seats = []
     i = 0  # Counts how many seats have been successfully booked
     while i < n: # Continue until all requested seats are booked

        try:
            seat_no = input(f"\nEnter seat no {i+1} : ").upper()
            row_index = rows.index(seat_no[0])
            col_index = int(seat_no[1:]) - 1
            
            if seat_layout[row_index][col_index] == 'O':
                seat_layout[row_index][col_index] = 'X'
                seat_type = seat_types[seat_no[0]]
                price = seat_price[seat_type]
                total_amount += price
                i += 1  # Only increment when a seat is successfully booked
                print(f"\nSeat {seat_no} - {seat_type} booked successfully")
                booked_seats.append(f"{seat_no} - {seat_type} - {price}")

            else:
                print(f"\nSeat {seat_no} is already booked.Choose another seat")
        except:
            print("ERROR ! Enter valid seat no")

     print("-------RECEIPT-------")
     print(f"Movie : {movie}")
     print(f"Showtime : {show}")
     print(f"\nBooked seats : \n")
     for i in booked_seats:
         print(i)
     print(f"\nTotal Price : {total_amount}")
     print("Thank you for booking !")
     print("-" * 21)
     
     save_seat_layout(file)  # Save updated seat layout to file
     display_seats(file)     # Show updated seating chart

def cancelling_seats(file):

     n = int(input("\nEnter number of seats to be cancelled : "))
     total_amount = 0  
     i = 0          # Counts successfully cancelled seats
     while i < n:   # Counts successfully cancelled seats

        try:
            seat_no = input(f"\nEnter seat no {i+1} : ").upper()
            row_index = rows.index(seat_no[0])
            col_index = int(seat_no[1:]) - 1
            
            if seat_layout[row_index][col_index] == 'X':
                seat_layout[row_index][col_index] = 'O'
                print(f"\nSeat {seat_no} cancelled successfully")
                seat_type = seat_types[seat_no[0]]
                price = seat_price[seat_type]
                total_amount += price
                i += 1                        # Only increment when cancellation succeeds
                
            else:
                print(f"\nSeat {seat_no} wasn't booked.")
        except:
            print("ERROR ! Enter valid seat no")

     refund = total_amount * 0.6          # Refund policy: 60% of ticket price
     print(f"\nRefund amount : {refund}")
     print("Your cancellation has been processed successfully !")
     print("We hope to see you again soon!") 
     save_seat_layout(file)
     display_seats(file)

def ensure_movie_selection():

    # Access global variables to update selection status and file info
    global movie_selected , movie , show ,file

     # Check if a movie/showtime has already been selected
    if not movie_selected:
         
         print("\nPlease select the movie and showtime first !")
         movie , show , file = display_movies_showtimes()  # Let user pick movie and showtime
         load_seat_layout(file)    # Load the seat layout for the selected movie/showtime
         movie_selected = True     # Mark that a selection has been made


print("Welcome to our GRL Theater")
print("We always give you the best experience !")

# Infinite loop to repeatedly show menu until user exits
while True:

    print("\n1.Select movies and showtimes\n2.Display Seats\n3.Book seats\n4.Cancel seats\n5.Exit")
    choice = int(input("\nEnter your choice : "))
    
    if choice == 1:
        movie , show , file = display_movies_showtimes()
        load_seat_layout(file)
        print(f"You selected {movie} - {show}")
        movie_selected = True
        display_seats(file)
        
    elif choice == 2:
        ensure_movie_selection()
        display_seats(file)

    elif choice == 3:
        ensure_movie_selection()
        booking_seats(file)
        
    elif choice == 4:
        ensure_movie_selection()
        cancelling_seats(file)
        
    elif choice == 5:
        print("Thank you for coming ! We hope to see you again !")
        break
