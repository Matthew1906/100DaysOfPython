from art import logo

bidders = {}

print(logo)
print("Welcome to the Secret Auction Program!")

while True:
    name = input("What's your name?\n>> ")
    bid = int(input("What's your bid?\n>> $"))
    bidders[name] = bid
    other_bid = input("Is there any other bidder? Type 'yes' or 'no'\n>> ").lower()
    if other_bid == 'no':
        break
    for i in range(0,20):
        print("")

# find max value
max_bid = max(bidders.values())
max_name  = ""
# find name
for key in bidders.keys():
    if bidders[key] == max_bid:
        max_name = key
        break

print(f"The winner is {max_name} with a bid of ${max_bid}.")
    