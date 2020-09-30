from datetime import datetime
#to get the user input
def user_input():
    print("enter 1 for single user log collection ")
    print("enter 2 for all user log collection ")
    print("enter 3 to exit the application")
    choice = str(input("Please enter your choice: "))
    while choice == '1':
        singleuser()
    while choice == '2':
        alluser()
    while choice == '3':
        print("you have choose to exit the application!")
        exit()
    else:
        invalid_entry()

#to handle the input errors
def invalid_entry():
    print("please enter a valid option")
    answer = str(input("do you want to continue:"))
    if answer == 'yes':
        user_input()
    if answer == 'no':
        print("you have choosed to exit the application!")
        exit()
    else:
        invalid_entry()


#for single user logging
def singleuser():
    #choice = str(input("Press 1 if you want single user logging: "))
    #while choice == '1':
        global s_date
        global c_date
        search = input("please enter the uname: ")
        sesidlist = [key for (key, value) in myusers.items() if search in value]
        f = open("apm.9", "r")
        mysessions={}
        for line in f:
            fields = line.split(" ")
            if 'PPP' in fields[8] and 'tunnel' in fields[9]: #and tid in fields[10]:
                sesid=str(line.split()[7].split(':')[2])
                tid = str(fields[10])
                if sesid not in mysessions:
                    mysessions.update({tid:sesid})
        res= [key for key,val in mysessions.items() if any(y in val for y in sesidlist)]
        #print("the keys mapped to" + str(sesidlist) + "are:" +str(res))
        #cab=str(res)
        counter= len(res)
        print("Month" "\t" "Day" "\t\t" "Time" "\t\t\t" " Tunnel ID" "\t\t\t"" SessionID" "\t\t\t" " Username" "\t\t\t" " Status""\t\t\t" " Duration")
        for x in range(counter):
            f = open("apm.9", "r")
            for line in f:
                fields = line.split(" ")
                if 'PPP' in fields[8] and 'tunnel' in fields[9] and res[x] in fields[10]:
                    print(fields[0] ,end='')
                    print("\t\t",fields[1] ,end='')
                    print("\t\t",fields[2] ,end='')
                    #print("\t\t",fields[7].split(':')[2], end='')
                    r = [val for key, val in myusers.items() if fields[7].split(':')[2] in key]
                    print("\t\t", fields[10], end='')
                    print("\t\t",fields[7].split(':')[2],end='')
                    print("\t\t\t","".join(r),"\t",end='')
                    line.strip("\n")
                    print("\t\t",fields[13],end='')
                # to print the time duration for single user
                if 'PPP' in fields[8] and 'tunnel' in fields[9] and res[x] in fields[10] and 'started' in fields[13]:
                     s_date = datetime.strptime(fields[2],'%H:%M:%S')
                if 'PPP' in fields[8] and 'tunnel' in fields[9] and res[x] in fields[10] and 'closed' in fields[13]:
                     c_date = datetime.strptime(fields[2],'%H:%M:%S')
                     print("\t" * 20, c_date - s_date)
        f.close()
        answer = str(input("do you want to continue:"))
        if answer == 'yes':
            user_input()
        if answer == 'no':
            print("you have choose to exit the application!")
            exit()
        else:
            invalid_entry()
        exit()
    #else:
    #    print("please enter a valid option")
    #    answer = str(input("do you wnt to continue:"))
     #   if answer == 'yes':
     #       singleuser()
      #  else:
       #     exit()

#for all user logging
def alluser():
    #choice=str(input("enter 2 for all user logging: "))
    #while choice == '2':
        global s_date
        global c_date
        sesidlist = [key for (key, value) in myusers.items()]
        f = open("apm.9", "r")
        mysessions={}
        for line in f:
            fields = line.split(" ")
            if 'PPP' in fields[8] and 'tunnel' in fields[9]: #and tid in fields[10]:
                sesid=str(line.split()[7].split(':')[2])
                tid = str(fields[10])
                if sesid not in mysessions:
                    mysessions.update({tid:sesid})
        res= [key for key,val in mysessions.items() if any(y in val for y in sesidlist)]
        counter= len(res)
        print("Month" "\t" "Day" "\t\t" "Time" "\t\t\t" " Tunnel ID" "\t\t\t"" SessionID" "\t\t\t" " Username" "\t\t\t" " Status""\t\t\t" " Duration")
        for x in range(counter):
            f = open("apm.9", "r")
            for line in f:
                fields = line.split(" ")
                if 'PPP' in fields[8] and 'tunnel' in fields[9] and res[x] in fields[10]:
                    print(fields[0] ,end='')
                    print("\t\t",fields[1] ,end='')
                    print("\t\t",fields[2] ,end='')
                    #print("\t\t",fields[7].split(':')[2], end='')
                    r = [val for key, val in myusers.items() if fields[7].split(':')[2] in key]
                    print("\t\t", fields[10], end='')
                    print("\t\t", fields[7].split(':')[2], end='')
                    print("\t\t\t","".join(r),"\t\t\t" +fields[13],end="")
                    #print(fields[13].center(70),end="")
                # to print the time duration for all users
                if 'PPP' in fields[8] and 'tunnel' in fields[9] and res[x] in fields[10] and 'started' in fields[13]:
                     s_date = datetime.strptime(fields[2],'%H:%M:%S')
                if 'PPP' in fields[8] and 'tunnel' in fields[9] and res[x] in fields[10] and 'closed' in fields[13]:
                     c_date = datetime.strptime(fields[2],'%H:%M:%S')
                     print("\t" * 27, c_date - s_date)
        f.close()
        answer = str(input("do you want to continue:"))
        if answer == 'yes':
            user_input()
        if answer == 'no':
            print("you have choose to exit the application!")
            exit()
        else:
            invalid_entry()
        exit()
    #else:
     #   print("please enter a valid option")
      #  answer = str(input("do you wnt to continue:"))
       # if answer == 'yes':
        #    alluser()
        #else:
         #   exit()

f = open("apm.9", "r")
myusers = {}

for line in f:
    fields = line.split(" ")
    if 'sslvpn_access_profile' in fields[7] and 'Username' in fields[8]:
        sesid = str(line.split()[7].split(':')[2])
        uname = str(fields[9]).replace("\n","")
        if sesid not in myusers:
            myusers.update({sesid:uname})

user_input()
