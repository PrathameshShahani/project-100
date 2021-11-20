class Atm(object):
    def __init__(self,card_number,pin_number):
        self.card_number=card_number
        self.pin_number=pin_number

    def balance_enquiry(self):
        print("Your balance is 35603")

    def cash_withdrawl(self,amount):
        print("You have withdrawn ",amount)
        print("Your balance is ",35603-amount)

    def cash_deposit(self,amount):
        print("You have deposited ",amount)    
        print("Your balance is ",35603+amount)

def main():
    card_number=input("Enter your card number: ")
    pin_number=input("Enter your pin: ")
    user=Atm(card_number,pin_number)
    print('Choose your activity: ')
    print("1. Balance Enquiry")
    print("2. Cash withdrawal")
    print("3. Cash deposit")
    activity=int(input("Enter your activity number: "))

    if(activity==1):
        user.balance_enquiry()
    elif(activity==2):
        amount=int(input("Enter the amount: "))
        user.cash_withdrawl(amount)
    elif(activity==3):
        amount=int(input("Enter the amount: "))
        user.cash_deposit(amount) 
    else:
        print("Enter a valid number")       

main()





