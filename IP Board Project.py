import mysql.connector as con
import pandas as pd
import matplotlib.pyplot as pl
import numpy as np
mycon=con.connect(host='localhost', user='root', passwd='rampage', charset='utf8', database='project')
if mycon.is_connected()==False:
    print("Not Connected")

cur=mycon.cursor()
res='y'

while res=='y' or res=='Y':
    print("\n\nMENU \n1.Retrieve \n2.Updation \n3.Insertion \n4.Deletion \n5.Visualization \n6.Exit")
    response=int(input("Enter your choice: "))
    
    #RETRIEVAL OF INFORMATION IN DIFFERENT WAYS
    if response==1:
        print()
        print("\U0001f600 WELCOME TO AIRPORT RETRIEVAL SERVICE \U0001f600")
        print()
        print("SUB-MENU \n 1.Display All \n 2.Filtered Column Display \n 3.Search Name-Wise")
        subch=int(input("ENTER THE SUB-CHOICE: "))
        if subch==1:
            query='select passengerid,passengername,age,gender,p.flightno,airlines,destination from passenger p,flight f where p.flightno=f.flightno'
            cur.execute(query)
            data=cur.fetchall()
            #for row in data:
                #print(row)
            df=pd.DataFrame(data, columns=['PassengerID','Passengername','Age','Gender','Flightno','Airlines','Destination'])
            print(df)
        if subch==2:
            lst=[]
            col=[]
            n=int(input("ENTER THE NUMBER OF COLUMNS YOU WANT IN DISPLAY- "))
            for i in range(0,n):
                ele=input('INPUT: ')
                lst.append(ele)
                col.append(ele)
                lst.append(',')
            lst=lst[:-1]
            print(lst)
            inp=''.join(lst)
            print()
            #print(inp)
            query="select {} from passenger p,flight f where p.flightno=f.flightno".format(inp)
            cur.execute(query)
            data=cur.fetchall()
            #for row in data:
                #print(row)
            df=pd.DataFrame(data,columns=col)
            print(df)
        if subch==3:
            name=input("Enter the name you want in display- ")
            query="select passengerid,passengername,age,gender,p.flightno,airlines,destination from passenger p,flight f where p.flightno=f.flightno and passengername='{}'".format(name)
            cur.execute(query)
            data=cur.fetchall()
            #for row in data:
                #print(row)
            df=pd.DataFrame(data,columns=['PassengerID','Passengername','Age','Gender','Flightno','Airlines','Destination'])
            print(df)
    
    #UPDATION OF DIFFERENT TABLES        
    if response==2:
        print("")
        login=input("ENTER YOUR LOGIN_ID: ")
        if login=='RJ10' or login=='RJ12':
            pswrd=input("ENTER PASSWORD: ")
            print()
            if pswrd=="tiger":    
                print("\U0001f600 WELCOME TO AIRPORT UPDATION SERVICE \U0001f600")
                print()
                print("SUB-MENU \n 1.Passenger Table \n 2.Flight Table")
                subch=int(input("ENTER THE SUB-CHOICE: "))
                if subch==1:
                    name=input("ENTER THE NAME OF THE PASSENGER-")
                    fno=input("ENTER THE CHANGED FLIGHT NUMBER-")
                    st="update passenger set flightno='{}' where passengername='{}'".format(fno,name)
                    cur.execute(st)
                    mycon.commit()
                    cur.execute("select * from passenger")
                    data=cur.fetchall()
                    #for row in data:
                        #print(row)
                    print()
                    print('NEW DATAFRAME FORMED IS:')
                    df=pd.DataFrame(data, columns=['PassengerID','Passengername','Age','Gender','Flightno'])
                    print(df)
                if subch==2:
                    fno=input("ENTER THE FLIGHT NUMBER-")
                    dest=input("ENTER THE NEW DESTINATION-")
                    st="update flight set destination='{}' where flightno='{}'".format(dest,fno)
                    cur.execute(st)
                    mycon.commit()
                    cur.execute("select * from flight")
                    data=cur.fetchall()
                    #for row in data:
                         #print(row)
                    print('NEW DATAFRAME FORMED IS:')
                    df=pd.DataFrame(data, columns=['Flightno','Airlines','Destination'])
                    print(df)
            else:
                print("!!! LOGIN FAILED !!!")
                break
        else:
            print("!!! LOGIN FAILED !!!")
            break
   
    #INSERTION INTO DIFFERENT TABLES
    if response==3:
        print()
        login=input("ENTER YOUR LOGIN_ID: ")
        if login=='RJ10' or login=='RJ12':
            pswrd=input("ENTER PASSWORD: ")
            print()
            if pswrd=="tiger":
                print("\U0001f600 WELCOME TO AIRPORT INSERTION SERVICE \U0001f600")
                print()
                print("SUB-MENU \n 1.Passenger Table \n 2.Flight Table")
                subch=int(input("ENTER THE SUB-CHOICE: "))
                if subch==1:
                    pid=int(input("ENTER PASSENGER_ID-"))
                    name=str(input("ENTER PASSENGERNAME-"))
                    age=input("ENTER THE AGE-")
                    gender=input("ENTER THE GENDER-")
                    fno=input("ENTER THE FLIGHT NUMBER-")
                    query="insert into passenger values({},'{}',{},'{}','{}')".format(pid,name,age,gender,fno)
                    cur.execute(query)
                    mycon.commit()
                    cur.execute("select * from passenger")
                    data=cur.fetchall()
                    #for row in data:
                        #print(row) 
                    print('NEW DATAFRAME FORMED IS:')
                    df=pd.DataFrame(data, columns=['PassengerID','Passengername','Age','Gender','Flightno'])
                    print(df)
                if subch==2:
                    fno=input("ENTER THE FLIGHT NUMBER-")
                    air=str(input("ENTER AIRLINES-"))
                    dest=input("ENTER THE DESTINATION-")
                    query="insert into flight values('{}','{}','{}')".format(fno,air,dest)
                    cur.execute(query)
                    mycon.commit()
                    cur.execute("select * from flight")
                    data=cur.fetchall()
                    #for row in data:
                        #print(row) 
                    print('NEW DATAFRAME FORMED IS:')
                    df=pd.DataFrame(data, columns=['Flightno','Airlines','Destination'])
                    print(df)
            else:
                print("!!! LOGIN FAILED !!!")
                break
        else:
            print("!!! LOGIN FAILED !!!")
            break
            
    #DELETION FROM DIFFERENT TABLES
    if response==4:
        print()
        login=input("ENTER YOUR LOGIN_ID: ")
        if login=='RJ10' or login=='RJ12':
            pswrd=input("ENTER PASSWORD: ")
            print()
            if pswrd=="tiger":
                print("\U0001f600 WELCOME TO AIRPORT DELETION SERVICE \U0001f600")
                print()
                print("SUB-MENU \n 1.Passenger Table \n 2.Flight Table")
                subch=int(input("ENTER THE SUB-CHOICE: "))
                if subch==1:
                    name=input("ENTER THE NAME OF PASSENGER WHOSE RECORD IS TO BE REMOVED-")
                    st="delete from passenger where passengername='{}'".format(name)
                    cur.execute(st) 
                    mycon.commit()
                    cur.execute("select * from passenger")
                    data=cur.fetchall()
                    #for row in data:
                        #print(row)
                    print('NEW DATAFRAME FORMED IS:')
                    df=pd.DataFrame(data, columns=['PassengerID','Passengername','Age','Gender','Flightno'])
                    print(df)
                if subch==2:
                    fno=input("ENTER THE FLIGHT NUMBER-")
                    st="delete from flight where flightno='{}'".format(fno)
                    cur.execute(st) 
                    mycon.commit()
                    cur.execute("select * from flight")
                    data=cur.fetchall()
                    #for row in data:
                    #print(row)
                    print('NEW DATAFRAME FORMED IS:')
                    df=pd.DataFrame(data, columns=['Flightno','Airlines','Destination'])
                    print(df)
            else:
                print("!!! LOGIN FAILED !!!")
                break
        else:
            print("!!! LOGIN FAILED !!!")
            break
            
    #VISUALIZATION IN DIFFERENT WAYS
    if response==5:
        print()
        print("\U0001f600 WELCOME TO AIRPORT VISUALIZATION SERVICE \U0001f600")
        print()
        print("SUB-MENU \n 1.Total Distribution of Flights \n 2.Preferred Place \n 3.Place-Wise Distribution \n 4.Gender Distribution (Place-Wise)")
        subch=int(input("\nENTER SUB-CHOICE: "))
        if subch==1:
            query='select airlines,count(*) from flight group by airlines'
            cur.execute(query)
            data=cur.fetchall()
            #for row in data:
                #print(row)
            print('Table formed is:')
            print()
            df=pd.DataFrame(data, columns=['Airlines','Number'])
            print(df)
            print()
            print('GRAPH CHOICE \n1.Bar Chart \n2.Line Chart \n3.Scatter Chart \n4.Pie Chart')
            pl.title("Total Number of Flights")
            graphch=int(input("Enter Graph Choice: "))
            if graphch==1:
                pl.bar(df['Airlines'],df['Number'])
                pl.xlabel('Airlines Available')
                pl.ylabel('Number of Airlines')
                pl.show()
            if graphch==2:
                pl.plot(df['Airlines'],df['Number'])
                pl.xlabel('Airlines')
                pl.ylabel('Number of Airlines')
                pl.show()
            if graphch==3:
                pl.scatter(df['Airlines'],df['Number'])
                pl.xlabel('Airlines')
                pl.ylabel('Number of Airlines')
                pl.show()
            if graphch==4:
                pl.pie(df['Number'],labels=df['Airlines'],shadow=True)
                pl.show()
        if subch==2:
            query='select destination,count(*) from flight group by destination'
            cur.execute(query)
            data=cur.fetchall()
            #for row in data:
                #print(row)
            print('\n\nTemporary Table:')
            print()
            df=pd.DataFrame(data, columns=['Destination','Number'])
            print(df)
            print()
            print('GRAPH CHOICE \n1.Bar Chart \n2.Line Chart \n3.Scatter Chart \n4.Pie Chart')
            pl.title("Preferred Destination")
            graphch=int(input("ENTER GRAPH CHOICE: "))
            if graphch==1:
                pl.bar(df['Destination'],df['Number'])
                pl.xlabel('Places')
                pl.ylabel('Number of Airlines')
                pl.show()
            if graphch==2:
                pl.plot(df['Destination'],df['Number'])
                pl.xlabel('Places')
                pl.ylabel('Number of Airlines')
                pl.show()
            if graphch==3:
                pl.scatter(df['Destination'],df['Number'])
                pl.xlabel('Places')
                pl.ylabel('Number of Airlines')
                pl.show()
            if graphch==4:
                pl.pie(df['Number'],labels=df['Destination'], shadow=True)
                pl.show()
        if subch==3:
            dest=input("Enter Destination: ")
            query="select airlines,destination,count(airlines) from flight group by destination,airlines having destination='{}'".format(dest)
            cur.execute(query)
            data=cur.fetchall()
            #for row in data:
                #print(row)
            print('Table formed is:')
            print()
            df=pd.DataFrame(data,columns=['Airlines','Destination','Number'])
            del df['Destination']
            print(df)
            print()
            print('GRAPH CHOICE \n1.Bar Chart \n2.Line Chart \n3.Scatter Chart \n4.Pie Chart')
            pl.title("Airline Distribution To Destination")
            graphch=int(input("ENTER GRAPH CHOICE: "))
            if graphch==1:
                pl.bar(df['Airlines'],df['Number'])
                pl.xlabel('Airlines Available')
                pl.ylabel('Number of Airlines')
                pl.show()
            if graphch==2:
                pl.plot(df['Airlines'],df['Number'])
                pl.xlabel('Airlines')
                pl.ylabel('Number of Airlines')
                pl.show()
            if graphch==3:
                pl.scatter(df['Airlines'],df['Number'])
                pl.xlabel('Airlines')
                pl.ylabel('Number of Airlines')
                pl.show()
            if graphch==4:
                pl.pie(df['Number'],labels=df['Airlines'], shadow=True)
                pl.show()
        if subch==4:
            gend='f'
            dest=input("Enter the Destination: ")
            query="select p.gender,f.destination,f.airlines,count(p.gender) from passenger p,flight f where p.flightno=f.flightno group by gender,airlines,destination having gender='f' and destination='{}'".format(dest)
            cur.execute(query)
            data=cur.fetchall()
            #for row in data:
                #print(row)
            print('Table formed (for females is):')
            df=pd.DataFrame(data, columns=['Gender','Destination','Airlines','Number'])
            del df['Destination']
            del df['Gender']
            print(df)
            print()
            gend1='m'
            query1="select p.gender,f.destination,f.airlines,count(p.gender) from passenger p,flight f where p.flightno=f.flightno group by gender,airlines,destination having gender='m' and destination='{}'".format(dest)
            cur.execute(query1)
            data1=cur.fetchall()
            #for row in data:
                #print(row)
            print('Table formed (for males is):')
            df1=pd.DataFrame(data1, columns=['Gender','Destination','Airlines','Number'])
            del df1['Destination']
            del df1['Gender']
            print(df1)
            print()
            print('GRAPH CHOICE \n1.Comparitive Bar Chart \n2.Line Chart \n3.Scatter Chart')
            pl.title("Gender Distribution Of Airlines")
            graphch=int(input("ENTER GRAPH CHOICE: "))
            if graphch==1:
                x=np.arange(3)
                y=['Air India','IndiGo','Vistara']
                pl.bar(x,df['Number'],width=0.3,label='Females')
                pl.bar(x+0.3,df1['Number'],width=0.3,label='Males')
                pl.legend(loc='upper right')
                pl.xticks(x,y)
                pl.xlabel('Airlines Available')
                pl.ylabel('Number of People')
                pl.show()
            if graphch==2:
                pl.plot(df['Airlines'],df['Number'],color='b',marker='x',label='Females')
                pl.plot(df1['Airlines'],df1['Number'],color='r',marker='d',label='Males')
                pl.xlabel('Airlines')
                pl.ylabel('Number of People')
                pl.legend(loc='upper right')
                pl.show()
            if graphch==3:
                pl.scatter(df['Airlines'],df['Number'],color='b',label='Females')
                pl.scatter(df1['Airlines'],df1['Number'],color='r',label='Males')
                pl.xlabel('Airlines')
                pl.ylabel('Number of People')
                pl.legend(loc='upper left')
                pl.show()
                
    #EXITING FROM THE SOFTWARE
    if response==6:
        print("Thank You For Using This Software")
        break
    res=input("Do you want to continue (Y/N)?")
    if res=='y' or res=='Y':
        continue
    else:
        break

mycon.close()