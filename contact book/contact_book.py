def contact_book():
    contacts ={}
    choice= ""
    while choice!="6":
        choice= input (""" =====contact book====
        1.Add contact
        2.view all contacts 
        3.Delete contact
        4.search contact 
        5.update contact
        6.exit  

""")

        if choice == "1":
            name = input("Add name: ")
            number = input("Add number: ")

            if name in contacts:
                update = input("Contact already exists. Update it? (y/n): ")

                if update.lower() == "y":
                    contacts[name] = number
                    print("Contact updated successfully.")
                else:
                    print("Contact not updated.")
            else:
                contacts[name] = number
                print("Contact added successfully.")

        elif choice   == "2":
            for name in contacts:
                
             print(f"{name} : {contacts[name]}") 

        elif choice=="3":
            name = input ("enter  name ")
            if name in contacts:
                del contacts[name]
                print (" contact is deleted ")
            else :
                print("contact not found ")

        elif choice =="4":
            found = False
        
            search  = input ("search name : ")
            for contact in contacts:
                if search.lower() in contact.lower() :
                    print (contact , contacts[contact])
                    found = True
            if not found:
                print('contact not found')
        elif choice== "5":
            name = input (" Enter contact  to update number ")
            if name in contacts:
                new_num= int (input ("enter number "))
                contacts[name]=new_num
                print (f" {name} : {new_num} number updated ")
            else:
                print ("name not to be found") 
        elif choice==   "6":
            print ('exited')

contact_book()                



        
     











    


