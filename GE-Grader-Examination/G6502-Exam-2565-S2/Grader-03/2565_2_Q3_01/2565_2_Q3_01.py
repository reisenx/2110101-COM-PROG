# --------------------------------------------------
# File Name : 2565_2_Q3_01.py
# Problem   : Stock Investment
# Author    : Worralop Srichainont
# Date      : 2025-07-12
# --------------------------------------------------

# Initialize dictionaries to store company ratings
# and the total money invested in each rating category
company_ratings = {}
ratings_money = {
    "AAA": 0,
    "AA": 0,
    "A": 0,
    "BBB": 0,
    "BB": 0,
    "B": 0,
    "CCC": 0,
    "CC": 0,
    "C": 0,
    "D": 0,
    "None": 0,
}


# Input ratings for each company and store them in a dictionary
def input_ratings() -> None:
    while True:
        data = input().strip()
        # Stop when the input is "END"
        if data == "END":
            break
        # Extract the company name and its rating
        company, rating = data.split()
        # Remove "+" or "-" at the end of the rating
        rating = rating.strip("+-")
        # Store the rating in the company_ratings dictionary
        company_ratings[company] = rating


# Get the rating of a stock based on its company name
def get_company_rating(stock: str) -> str:
    # Check if the stock matches any company name in the dictionary
    for company, _ in company_ratings.items():
        # If the stock starts with the company name, return its rating
        if stock.find(company) == 0:
            return company_ratings[company]
    # If no match is found, return "None"
    return "None"


# Input stock investments and update the total money invested in each rating category
def input_stocks() -> None:
    while True:
        data = input().strip()
        # Stop when the input is "END"
        if data == "END":
            break
        # Extract the stock name and the amount of money invested
        stock, money = data.split()
        # Get the rating of the stock
        rating = get_company_rating(stock)
        # Add the money to the corresponding rating category
        ratings_money[rating] += int(money)


# Output the total money invested in each rating category
# along with the percentage of the total investment
def print_results() -> None:
    # Calculate the total money invested across all ratings
    total_money = sum(ratings_money.values())
    for rating, money in ratings_money.items():
        # Only print ratings with money invested greater than 0
        if money > 0:
            percentage = round((money / total_money) * 100, 2)
            print(f"{rating} {money} {percentage}%")


# Main function
def main() -> None:
    input_ratings()
    input_stocks()
    print_results()


# Execute the main function
main()
