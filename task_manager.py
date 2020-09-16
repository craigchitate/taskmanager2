


from datetime import date #imports the current date

def login():
    login_value = False
    u_username = input("Insert Username:")
    u_password = input("Insert Password:")
    with open('user.txt','r') as f:
        for line in f:
            s_username = line.split(',')[0]
            s_password = line.split(',')[1].strip()


            if s_username != u_username:
                continue
            if s_username == u_username:
                if s_password == u_password:
                    print("logged In as" + " " + u_username)
                    return s_username 
                else:
                    print("invalid password")
                    login()
    print("user not found")
    login()

    



def reg_user():
    print("Register New User")
    username = input("Username:")
    password = input("Password:")
    conf_password = input("confirm password")
    if password == conf_password:
        with open("user.txt",'a') as f:
            f.write('\n' + username + "," + password)
            f.close()
    else:
        print("password does not match \n")
        register()


def add_task():#allows users to add tasks 
    print("Adding New Tasks \n")
    username = input("Assignee username:")
    taskTittle = input("Title Of Task:")
    taskdescript = input("Description Of Task:")
    dueDate = input("Due Date:")
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    with open ("tasks.txt" ,'a') as f:
               f.write('\n' + username+ ","+ taskTittle + "," + taskdescript + ","+ today + dueDate + "NO")
    
    
    
def view_mine(): #allows users to view tasks 
    print("Viewing Available Tasks \n")
    with open ("tasks.txt",'r') as f:
        for line in  f:
            task = line.split(",")
            line = ''
            for element in task:
                line = line + '\t' + element 
            print(line)


            print("\n")
            
#this line generate reports
            
def generate_reports():
    
    print("Generate reports")
    with open("tasks.txt",'r+')as f:
        data = f.readlines()
        total_task = len(data)
        total_completed = 0
        total_uncompleted = 0
        
        for line in data:
            if line.endswith("Yes") or line.endswith("yes"):
                total_completed += 1
            else:
                total_uncompleted += 1

        avg_completed = total_completed / total_task #this code shows the number of completed tasks 
        avg_uncompleted = total_uncompleted / total_task #this code shows the number of uncomplited tasks


        with open("user.txt", "r+") as f2:
            users = f2.readlines()

            user_report = dict()
            
            for task in data:
                for user in users:
                    user = user.split(",")
                    if task.startswith(user[0].strip()) and user[0].strip() in user_report.keys():
                        user_report[user[0].strip()] += 1
                        
                    elif task.startswith(user[0].strip()):
                        user_report[user[0].strip()] = 1
                    else:
                        user_report[user[0].strip()] = 0

            user_completed = dict()
            for task in data:
                for user in users:
                    if line.endswith("Yes") or line.endswith("yes"):
                        user = user.split(",")
                        if task.startswith(user[0].strip()) and user[0].strip() in user_report.keys():
                            user_report[user[0].strip()] += 1
                            
                        elif task.startswith(user[0].strip()):
                            user_report[user[0].strip()] = 1
                        else:
                            user_report[user[0].strip()] = 0
                    
                        

        with open("user_overview.txt", 'w') as f: # opens useroverview textfile
            
            print("TASK COMPLETED PER USER")

            print("USER AVERAGE TASK COMPLETED per total assigned")
            for k,v in user_completed.items():
                for kk,vv in user_report.items():
                    print(f"{k} as completed {v/vv*100}%")

                f.write(f"{k} as completed {v/vv*100}%")


        with open ("task_overview.txt",'w') as f: #this code opens taskoverview text files 

            print("Total number of completed tasks") #prints out the number of completed tasks 
            for k,v in user_completed.items():
                for kk,vv in  user_report.items():
                      print(f"{k} as uncompleted {v/vv*100}%")


                task_overview.write(f"{k} as uncompleted {v/vv*100}%")

                      
                
            
                    


def view_all():#allows users to view their own tasks 
    print("Viewing Tasks For User" + s_username + "\n")
    with open ("tasks.txt",'r') as f:
        for line in f:
            if line.split(",")[0] == s_username:
                print(line)
                


def makeChoiceAdmin(): #allows admin to make his/her choice by either registering users or viewing tasks 
    print("r - register user \n")
    print("ds - Display Statistics \n")
    print("gr - generate_reports \n")

    
def stats():
    taskNum = 0
    with open("tasks.txt",'r') as f:
        for line in f:
            taskNum +=1
    userNum = 0
    with open('user.txt',"r") as f:
        for line in f:
            userNum += 1
            
    stat = " Number Of Tasks " + str(taskNum) + " \n Number Of Users " + str(userNum)
    print(stat)
    


def makeChoice():#allows user to make choice
    print("please select one the following options: \n")
    if s_username == "admin":
        makeChoiceAdmin()
    print("a - add task \n")
    print("va - view all my task \n")
    print("vm- view my task \n")
    print("e - exit \n")

    choice = input("Insert Option:")

    if choice == "r" and s_username == "admin":
        reg_user()
    elif choice == "ds" and s_username == "admin":
        stats()
    elif choice == "a":
        add_task()
    elif choice == "va":
        view_all()
    elif choice == "vm":
        view_mine()
    elif choice == "gr":
        generate_reports()
    elif choice == "e":
        exit()
          
    else:
        print("Invalid Selection")
        
s_username = login()
makeChoice()
