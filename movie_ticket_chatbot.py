import random
theaters = {
    "M1": {
        "S1": {
            "RRR": 150.0,
            "KGF": 130.0,
        },
        "S2": {
            "OG": 140.0,
        },
    },
    "MGB Cinemas": {
        "S1": {
            "RRR": 155.0,
            "KGF": 135.0,
        },
        "S2": {
            "OG": 145.0,
        },
    },
    "PVR": {
        "S1": {
            "RRR": 160.0,
            "KGF": 140.0,
        },
        "S2": {
            "OG": 150.0,
        },
    },
}

screen_seats = {
    "M1": {
        "S1": {
            "RRR": list(range(1, 21)),  
            "KGF": list(range(1, 31)),  
        },
        "S2": {
            "OG": list(range(1, 26)), 
        },
    },
    "MGB Cinemas": {
        "S1": {
            "RRR": list(range(1, 21)), 
            "KGF": list(range(1, 31)),  
        },
        "S2": {
            "OG": list(range(1, 26)), 
        },
    },
    "PVR": {
        "S1": {
            "RRR": list(range(1, 21)),  
            "KGF": list(range(1, 31)),  
        },
        "S2": {
            "OG": list(range(1, 26)),  
        },
    },
}

user_bookings = {}

def display_theaters():
    print("Available Theaters:")
    for theater in theaters.keys():
        print(theater)

def display_screens(theater):
    print(f"\nAvailable Screens at {theater}:")
    for screen in theaters[theater].keys():
        print(screen)

def display_movies(theater, screen):
    print(f"\nAvailable Movies at {theater}, Screen {screen}:")
    for movie, price in theaters[theater][screen].items():
        print(f"{movie} - Rs.{price:.2f}")

def book_ticket(theater, screen, movie, num_tickets):
    if theater not in theaters:
        return "Sorry, the selected theater is not available."
    
    if screen not in theaters[theater]:
        return "Sorry, the selected screen is not available in this theater."

    if movie not in theaters[theater][screen]:
        return "Sorry, the selected movie is not available in this screen."

    available_seats = screen_seats[theater][screen][movie]

    if len(available_seats) < num_tickets:
        return "Sorry, there are not enough available seats for your request."

    selected_seats = random.sample(available_seats, num_tickets)
    for seat in selected_seats:
        available_seats.remove(seat)

    user_bookings[(theater, screen, movie)] = user_bookings.get((theater, screen, movie), []) + selected_seats

    return f"You have successfully booked {num_tickets} tickets for {movie} at {theater}, Screen {screen}. Your seat(s): {', '.join(map(str, selected_seats))}."

def main():
    print("Welcome to Movie Ticket Booking Movies Chatbot!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Display available theaters")
        print("2. Book a ticket")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_theaters()
        elif choice == "2":
            theater = input("Enter the name of the theater: ")
            if theater not in theaters:
                print("Invalid theater name. Please try again.")
                continue
            display_screens(theater)
            screen = input("Enter the name of the screen: ")
            if screen not in theaters[theater]:
                print("Invalid screen name. Please try again.")
                continue
            display_movies(theater, screen)
            movie = input("Enter the name of the movie you want to book: ")
            num_tickets = int(input("Enter the number of tickets you want to book: "))
            result = book_ticket(theater, screen, movie, num_tickets)
            print(result)
        elif choice == "3":
            print("Thank you for using the Movie Ticket Booking Movies Chatbot. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()