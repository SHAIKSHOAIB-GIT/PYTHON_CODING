import os
continue_bid = True
bid = {}
while continue_bid:
    name = input("enter your name : \n")
    price = int(input("enter your bid price ₹ \n"))
    bid[name] = price

    continues=input("enter 'yes' if there are want to bid else enter 'no' \n")
    if continues == "yes":
        #searched from browser
        clear = lambda: os.system('clear')
        clear()
    if continues == "no":
        heighest_bidder = 0
        for highest in bid:
            highest_bid = bid[highest]
            if highest_bid > heighest_bidder:
                heighest_bidder = highest_bid 
                heighest_bidder_name =highest
        print(f"highest bidder is {heighest_bidder_name} and highest bid ₹{heighest_bidder}")   
        continue_bid = False
