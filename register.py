import csv

def register_user(username, password, email):
    # TODO: Validate input

    # Add user to CSV file
    with open('users.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username, password, email])

# TODO: Create form to collect user information
