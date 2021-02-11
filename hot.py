import csv
import matplotlib.pyplot as plt
import pandas as pd


#Check In
def chechin():
    inp = []
    cusid = int(input("Enter Customer ID:"))
    inp.append(cusid)
    name  = input("Enter Customer Name: ")
    inp.append(name)
    add   = input("Enter Customer Address:")
    inp.append(add)
    email = input("Enter Customer Email:")
    inp.append(email)
    phone = input("Enter Customer Phone:")
    inp.append(phone)
    print("1)Dulex Room : 1500/-\t 2)Dulex Room (AC) : 2000/- \n3)Regular Room : 800/-\t 4)Regular Room (AC) : 1100/-")
    r  = int(input("Choose Type of Room:"))
    room = ""
    price = 0
    if(r == 1):
        room = "Dulex"
        price = 1500
    else:
        if(r == 2):
            room = "Dulex AC"
            price = 2000
        else:
            if(r == 3):
                room = "Regular"
                price = 800
            else:
                if(r == 4):
                    room = "Regular AC"
                    price = 1100    
    print(room)
    inp.append(room)
    print(price)
    inp.append(price)
    days = int(input("Enter Number of days : "))
    inp.append(days)
    tot=price*days
    inp.append(tot)
    inp.append('')
    
    with open('cus.csv', 'a+', newline='') as f:
        write = csv.writer(f)
        write.writerow([cusid,name,add,email,phone,room,price,days,tot,''])
        f.close()
    
    print("\n\n\n")
    input("Press Any Key To Continue ..........")
    print("\n\n\n")
    
#Customer Details
def customer_detail():
    print("\n\n\n")
    cus_id = input("Enter Customer ID : ")
    data = []
    with open('cus.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if(row[0] == cus_id):
                data = row
    #print(data)
    print("\n\t\tCustomer ID : "+data[0])
    print("\t\tCustomer Name : "+data[1])
    print("\t\tCustomer Address : "+data[2])
    print("\t\tCustomer Email : "+data[3])
    print("\t\tCustomer Phone : "+data[4])
    print("\t\tCustomer Room : "+data[5])
    print("\t\tCustomer Charge : "+data[6])
    print("\t\tNumber of Days Stayed : "+data[7])
    print("\t\tTotal Charge : "+data[8])
    print("\t\tCheck Out : "+data[9])
    print("\n\n\n")
    input("Press Any Key To Continue ..........")
    print("\n\n\n")


#Check Out
def checkout():
    cus_id = input("Enter Customer ID : ")
    i = 0
    r = csv.reader(open('cus.csv'))
    lines = list(r)
    for n, line in enumerate(lines):
        if(line[0] == cus_id):
            line[9] = "YES"
    lines[n] = line
    
    with open('cus.csv', 'w', newline='') as f:
        write = csv.writer(f)
        for line in lines:
            write.writerow(line)
    f.close()
    input("Press Any Key To Continue ..........")
            
#Data visualition
def vis():
    data = pd.read_csv('cus.csv')
    x = data['cus_room'].unique()
    y = data.groupby('cus_room')['Num_days'].count()

    plt.bar(x,y)
    plt.xlabel('Types of Rooms')
    plt.ylabel('Total Number of Days Occupied')
    plt.show()

    y = data.groupby("cus_room")['Num_days'].mean()
    plt.bar(x,y)
    plt.xlabel('Types of Rooms')
    plt.ylabel('Average Number of Days Room Occupied')
    plt.show()
            
        
    
#Mail
print("Dulex Room : 1500/-\t Dulex Room (AC) : 2000/- \nRegular Room : 800/-\t Regular Room (AC) : 1100/-")
print("1) CheckIn.")
print("2) Customer Details")
print("3) CheckOut")
print("4) Data Visualization")
print("5) Exit")

ch = int(input("  select your choice  :  "))
while(ch!=5):
    if(ch == 1):
        chechin()
    else:
        if(ch == 2):
            customer_detail()
        else:
            if(ch == 3):
                checkout()
            else:
                if(ch == 4):
                    vis()
                else:
                    print("Invalid Input")
                
    print("1) CheckIn.")
    print("2) Customer Details")
    print("3) CheckOut")
    print("4) Data visualization")
    print("5) Exit")
    ch = int(input("  Select Your Choice  :  "))
