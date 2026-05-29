import random, csv

# Open two name csv files and pick a random row from each one
def generate_name() -> str:
    with open("names/first_names.csv") as f:
        first_names = csv.reader(f)
        chosen_first_name = random.choice(list(first_names))[0]
    with open("names/last_names.csv") as f:
        last_names = csv.reader(f)
        chosen_last_name = random.choice(list(last_names))[0]
    
    # Return the first and last name
    return f"{chosen_first_name} {chosen_last_name}"

