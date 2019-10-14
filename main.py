import datetime


#Here I get today's date
today = datetime.date.today()
#This variable is the payment interval
monthdelta = datetime.timedelta(days=30.4167)
weeklydelta = datetime.timedelta(days=7)

total_debt = int(input("What is the total debt?\n$"))
amnt_to_pay = int(input("What would be the recurrent amoumt?\n$"))

total_payments = total_debt / amnt_to_pay

print("This would make", total_payments,"payments.")
print("")
#input on wether is monthly or weekly
frequency = int(input("How often will you pay? \n1. monthly 2.weekly\n"))

if frequency == 1:
    frequency = monthdelta
elif frequency == 2:
    frequency = weeklydelta
print('')
lenght_of_time = int(total_payments)
print("")
print("Starting today, This is how you payments will look like:")
for i in range(lenght_of_time):
    balance = total_debt - amnt_to_pay * (i + 1)
    nd = today + frequency * (i + 1)
    print(nd.strftime("%B %d, %Y"))

    if balance > 0 and amnt_to_pay > balance:
        print("The balance after payment is now ${}".format(balance))
        print('')
        nd = today + frequency * (i + 2)
        print("Last payment of ${}".format(balance), "will be on", nd.strftime("%B %d, %Y") )
    else:
        print("The balance after payment is now ${}".format(balance))
        print("")
print('')    

# Textual month, day and year	
# d2 = a.strftime("%B %d, %Y")
# print("")
# print("New Date =", d2, "\n")
