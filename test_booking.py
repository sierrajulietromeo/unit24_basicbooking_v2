import pandas as pd #For read/write to the file.
import os

#main program menu
def main():
    print("Welcome to the Ada Booking System")
    print("=================================")
    print("Please select from the following options")
    print("1: View room bookings for SPUTNIK")
    print("2: View all free rooms")

    viewSelection = int(input("Enter selection: "))
    os.system("cls")  #Only works on Windows machines
    if(viewSelection == 1):
        roomName = "Sputnik"
        displayRoomBookings(roomName)
    elif(viewSelection == 2):
        print("2")
    elif(viewSelection == 3):
        print("3")
    else:
        main()

def displayRoomBookings(roomName):
    df = pd.read_csv("sputnikbookings.csv")
    print(roomName +" Bookings")
    #dayDataFrame = df[(df.Room == roomName) & (df.Day == selectedDay)]
    df.set_index("Day", inplace=True)
    #dayDataFrame.set_index("Period")
    print (df)
    #print(df[(df.Room == roomName) & (df.Day == selectedDay)])
    #print(df[(df.Room == roomName) & (df.Day == selectedDay)] )
    print("Enter the period number you wish to book, or enter any other character to go back.")
    periodNumber = int(input("?"))
    periodNumber -= 1
    print("Enter the day you wish to book, (Mon,Tue,Wed,Thu,Fri) or enter any other character to go back.")
    selectedDay = input("?")
    stringDay = 0
    if (selectedDay == "Mon"):
        stringDay = 0
    elif (selectedDay == "Tue"):
        stringDay = 1
    elif (selectedDay == "Wed"):
        stringDay = 2
    elif (selectedDay == "Thu"):
        stringDay = 3
    elif (selectedDay == "Fri"):
        stringDay = 4

    else:
        main()

    if(df.iat[stringDay,periodNumber] != "FREE"):
        print ('\a') #Plays a system sound.
        os.system("cls")  #Only works on Windows machines
        print("Sorry, this room is already booked for that period by:", (df.iat[stringDay, periodNumber])  )
        print("                                  ")
        displayRoomBookings(roomName)
    else:
        name = input("Enter name to book room under: ")
        df.iat[stringDay, periodNumber] = name
        df.to_csv("sputnikbookings.csv", index=True)
        print ('\a') #Plays a system sound.
        periodNumber += 1
        print("Room is now booked for you at period:", periodNumber, "on", selectedDay)
        print("                           ")
    main()



def bookRoom(roomName, periodNumber):
    df = pd.read_csv("sputnikbookings.csv")



    # print(df.loc[[1]])
    #if(df.loc[periodNumber] != "FREE"):   #Trying to work out a more elegant solution for selecting.
    if (df.at[periodNumber, "Name"] != "FREE"):
        os.system("cls")  #Only works on Windows machines
        print ('\a')
        print("Sorry, this room is already booked for that period by:", (df.at[periodNumber, "Name"])  )
        print("                                  ")
        displayRoomBookings(roomName, selectedDay)
    else:
        name = input("Enter name to book room under: ")
        df.at[periodNumber, "Name"] = name
        df.to_csv("sputnikbookings.csv", index=False)

        if(roomName == "Sputnik" and selectedDay == "Wednesday"):
            periodNumber -= 7
        else:
            periodNumber

        periodNumber += 1 #to get the right place in the array because counting starts at 0
        #os.system("cls")  #Only works on Windows machines
        print("Room is now booked for you at period:", periodNumber, "on", selectedDay)
        print("                           ")



    #Loopthroughheretoseeifitsfree
    main()


def viewFreeRooms():
    print("FREE ROOMS")
    df = pd.read_csv("sputnikbookings.csv")
    df.set_index("Period", inplace=True)
    print(df[df.Name == "FREE"] )
    main()


def editRoomBooking():
    #df.at[1, "Name"] = "John"
    df.to_csv("sputnikbookings.csv", index=False)


#Sequential Code
main()
