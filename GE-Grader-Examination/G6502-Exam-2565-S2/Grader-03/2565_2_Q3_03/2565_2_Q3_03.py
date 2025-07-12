# --------------------------------------------------
# File Name : 2565_2_Q3_03.py
# Problem   : CUEng Sport 2023
# Author    : Worralop Srichainont
# Date      : 2025-07-12
# --------------------------------------------------

# Initialize dictionaries to store person per team of each sport,
# sport registration details, and sport teams details
person_per_team = {}
sport_registration = {}
sport_teams = {}


# Input the number of persons per team for each sport and store it in a dictionary
def input_person_per_team() -> None:
    while True:
        # Read input line until it is "END"
        line = input().strip()
        if line == "END":
            break
        # Extract sport and person per team and store them in the dictionary
        sport, person = line.split()
        person_per_team[sport] = int(person)


# Participants register for sports
def register_sport() -> None:
    # Initialize dictionary for every sport
    for sport, _ in person_per_team.items():
        sport_registration[sport] = {}

    while True:
        # Read input line until it is "END"
        line = input().strip()
        if line == "END":
            break

        # Extract name, department, and sports from the line
        name, department, sports = line.split()
        # Register the participant in each sport they are interested in
        for sport in sports.split(","):
            # If the sport is not already registered, initialize it
            if department not in sport_registration[sport]:
                sport_registration[sport][department] = set()
            # Add the participant's name to the set of department members for that sport
            sport_registration[sport][department].add(name)


# Calculate the number of department teams and substitutes for each sport
def calculate_sport_teams() -> None:
    for sport, departments in sport_registration.items():
        # Initialize the sport in the sport_teams dictionary
        if sport not in sport_teams:
            sport_teams[sport] = {}

        for department, members_set in departments.items():
            # Calculate the number of teams and substitutes for each department
            members = len(members_set)
            teams = members // person_per_team[sport]
            subs = members % person_per_team[sport]
            # If there are teams, store the count in the sport_teams dictionary
            if teams > 0:
                sport_teams[sport][department] = [teams, subs]


# Output the sport teams in the required format
def print_sport_teams() -> None:
    # Sort the sport_teams dictionary by sport alphabetically
    for sport, departments in sorted(sport_teams.items()):
        # Initialize the output line with the sport name
        line = f"{sport}:"
        # Sort the departments by its name alphabetically
        for department, [teams, subs] in sorted(departments.items()):
            # Add the department and its teams/substitutes to the output line
            line += f"{department}({teams},{subs})"
        # Print the formatted line
        print(line)


# Main function
def main() -> None:
    input_person_per_team()
    register_sport()
    calculate_sport_teams()
    print_sport_teams()


# Execute the main function
main()
