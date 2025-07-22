
import art
print(art.logo)

bidderYn = 'yes'
bidder_list = []
while bidderYn == 'yes':
    name = input("What is your name? ")
    bid = int(input("What's your bid? "))
    bidder_list.append({"name" : name, "bid" : bid})
    bidderYn = input("Are there any other bidders? Type 'yes' or 'no'\n")
    print("\n" * 100)

bid = 0

for bidder in bidder_list:
    if bid < bidder['bid']:
        bid = bidder['bid']
        name = bidder['name']

print(f'The winner is {name} with a bid of ${bid}.')


# # 1. Ask the user for input
# name = input("What is your name? ")
# bid = int(input("What's your bid? "))
# bids = {}
# # 2. save data into dictionary {name : price}
# bids[name] = bid
# # 3. whether if new bids need to be added
# should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n")
# continue_bidding = True
# while continue_bidding:
#     name = input("What is your name? ")
#     bid = int(input("What's your bid? "))
#     bids[name] = bid
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()

#     if should_continue == "no":
#         winner,bid_amount = find_highest_bidder(bids)
#         print(f'The winner is {winner} with a bid of ${bid_amount}.')
# # 4. compare bids in dictionary

# def find_highest_bidder(bidding_dictionary):
#     highest_bid = 0
#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
        
#     return winner,highest_bid


