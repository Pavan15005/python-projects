def atm_simulator():
    pin = int(input("Enter your pin : "))
    correct_pin = 1234 
    if pin==correct_pin:
        print("login sucessfull")
        balance=5000   
        choice=""
         
        while choice!="5":
            choice=input("""***** ATM MANAGER*****
       1. Check Balance
       2. Deposit
       3. Withdraw
       4. Change PIN
       5. Exit
        
        ENTER """)
           
        
        
            if choice=="1":
              print (f"your balance is {balance}")
            elif choice=="2":
                new_amt=int(input("enter amount" ))
                balance+=new_amt
                print(f"total is {balance}")
            elif choice=="3":
                take=int(input("enter amount "))
                if balance<take:
                 print ("low balance")
                else:
                 balance-=take
                 print (f"after withdrawl amount is {balance}")
            elif choice=="4":
               pin = int(input("Enter your currernt pin : "))
               if pin != correct_pin:
                  print("wrong pin ")
               else:        
                   pin == correct_pin
                   correct_pin =int(input("enter new pin "))
                   print ("pin updated ")
            elif choice=="5":
               print("exited")


                    
            
    else:
        print("wrong pin ")
                
atm_simulator()      










