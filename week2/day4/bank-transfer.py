accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an balance of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - balance
#
# Print "404 - account not found" if any of the account numbers don't exist

n = input("Please enter clientname: ")
def namebalance(n):
    s = 0
    for p in accounts:
        if p['client_name'] == n:
            s += 1
            print(str(n) + " balance: " + str(p['balance']))
    if s == 0:
        print("404 - account not found")
namebalance(n)
