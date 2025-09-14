import logging
import time

# Setup logging
logging.basicConfig(filename="cinema_log.txt",
                    level=logging.INFO,
                    format="%(asctime)s - %(message)s")

# Movies list
movies = ["TIRANGA", "HORROR RAAZ", "ARANMANAI", "APPU", "KABIR SINGH"]

# Ticket settings
total_tickets = 5
tickets_booked = 0

print('The movies available are "Tiranga","Horror Raaz","aranmanai","Appu","Kabir Singh".')

# Booking loop
while tickets_booked < total_tickets:
    movie_choice = input("\nWhat film would you like to watch?: ").upper()

    if movie_choice not in movies:
        print("We don't have that film..")
        logging.info(f"Movie not available: {movie_choice}")
        continue

    # Age check
    age = int(input("How old are you?: "))
    if age < 5 and movie_choice in ["ARANMANAI", "HORROR RAAZ"]:
        print("You are too young to see that film!")
        logging.info(f"Denied: {movie_choice} for age {age}")
        continue

    # Ticket booking
    if tickets_booked < total_tickets:
        tickets_booked += 1
        remaining = total_tickets - tickets_booked
        print("Your movie ticket is booked. Enjoy the film!")
        if remaining > 0:
            print(f"The number of tickets booked are {tickets_booked} and remaining are {remaining}")
        logging.info(f"Booked: {movie_choice} for age {age}. Tickets left: {remaining}")
    else:
        print("Sorry, we are sold out!")
        logging.info(f"Attempted booking when sold out for {movie_choice}")
        break

    # Simulate schedule delay (like showtime gap)
    time.sleep(1)

print("\nAll tickets sold. Come back tomorrow!")
