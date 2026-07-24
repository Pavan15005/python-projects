

def student_manager():
    
    choice = ""
    students = {}
    

    while choice != "6":
        choice=input("""===== Student Manager =====
1. Add Student
2. Remove Student
3. View Students
4. Average Marks
5. upddate
6. exit                     

Enter your choice:""")
        if choice == "1":
            
            print ("add student")
            name = input("enter name ")
            marks = int(input("enter marks"))
            students[name]=marks
            

        elif choice =="2":
            
            print ("remove student")
            name = input("name to remove")
            if name in students:
                del students[name]
                print("name deleted")
            else:
                print ("name not found")



        elif choice == "3":
             
             print ("view student")
             for student in students:
                 print (student, students[student])
             
        elif choice =="4":
            
            if len(students)==0:
                print("no students ")
            else:    
                print ("average marks of student")
                total=0
                for i in students:
                    total+=students[i]
                average = total/len(students)        
                print (average)
        elif choice =="5":
            
            print("update student marks")
            name = input("name of student")
            if name in students:
                new_marks = int(input("enter new marks"))
                students[name]=new_marks
                print (new_marks, "marks updated")
            else:
                print("student not found")
           
                       
student_manager()    
    




    