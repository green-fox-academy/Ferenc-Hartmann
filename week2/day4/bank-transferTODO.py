accounts = [
	{ 'client_name': 'Igor', 'account_number': 1, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 2, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 3, 'balance': 1353600.0 }
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





fac = 0
tac = 0
bal = 0

def transfer():
	fac = input("Please enter the account number where you want to start the transfer: ")
	tac = input("Please enter the account number where you want to do the transfer: ")
	bal = input("Please enter the balance what you want to transfer: ")
	n = 0
	for i in accounts:
		n += 1
		if i['account_number'] == int(fac):
			q = accounts[(n -1)]['balance']
			print("Starter balance before: " + str(q))
			q -= int(bal)
			print("Starter balance after: " + str(q))
			t = 0
			for j in accounts:
				t += 1
				if j['account_number'] == int(tac):
					p = accounts[(t -1)]['balance']
					print("End balance before: " + str(p))
					p += int(bal)
					print("End balance after: " + str(p))
transfer()
