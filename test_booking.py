import pandas as pd #For read/write to the file.
import os

#main program menu
def main():
    print("Welcome to the Ada Booking System")
    print("=================================")
    print("Please select from the following options")
    print("1: View room bookings for Tuesday")
    print("2: View room bookings for Wednesday")
    print("3: View all free rooms")


    mainMenuSelection = int(input("Enter selection: "))
    os.system("cls")  #Only works on Windows machines
    if(mainMenuSelection == 1):
        selectedDay = "Tuesday"
        viewRoomBookings(selectedDay)
    elif(mainMenuSelection == 2):
        selectedDay = "Wednesday"
        viewRoomBookings(selectedDay)
    elif(mainMenuSelection == 3):
        viewFreeRooms()
    else:
        main()





def viewRoomBookings(selectedDay):
    print("VIEW ROOM BOOKINGS FOR:",selectedDay)
    print("=================================")
    print("Please select from the following rooms")
    print("1: SPUTNIK")
    print("2: ENDEAVOUR")
    print("3: VOYAGER")

    viewSelection = int(input("Enter selection: "))
    os.system("cls")  #Only works on Windows machines
    if(viewSelection == 1):
        roomName = "Sputnik"
        displayRoomBookings(roomName,selectedDay)
    elif(viewSelection == 2):
        displayRoomBookings(selectedDay)
    elif(viewSelection == 3):
        print("3")
    else:
        main()

def displayRoomBookings(roomName,selectedDay):
    df = pd.read_csv("room_bookings.csv")

    print(selectedDay +" Bookings")

    #dayDataFrame = df[(df.Room == roomName) & (df.Day == selectedDay)]


    df.set_index("Period", inplace=True)

    #dayDataFrame.set_index("Period")
    #print (dayDataFrame)
    print(df[(df.Room == roomName) & (df.Day == selectedDay)])
    #print(df[(df.Room == roomName) & (df.Day == selectedDay)] )
    print("Enter the period number you wish to book, or enter any other character to go back.")

    try:
        periodNumber = int(input("?"))

    except ValueError:

        #os.system("cls")  #Only works on Windows machines
        main()

    try:
        if(periodNumber == 1 or 2 or 3 or 4 or 5 or 6 or 7):
            bookRoom(roomName, periodNumber, selectedDay)
        else:
            os.system("cls")  #Only works on Windows machines
            main()

    except KeyError:
        main()

def bookRoom(roomName, periodNumber, selectedDay):
    df = pd.read_csv("room_bookings.csv")
    if(roomName == "Sputnik" and selectedDay == "Wednesday"):
        periodNumber += 7
    else:
        periodNumber


    periodNumber -= 1 #to get the right place in the array because counting starts at 0



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
        df.to_csv("room_bookings.csv", index=False)

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
    df = pd.read_csv("room_bookings.csv")
    df.set_index("Period", inplace=True)
    print(df[df.Name == "FREE"] )
    main()


def editRoomBooking():
    #df.at[1, "Name"] = "John"
    df.to_csv("room_bookings.csv", index=False)


#Sequential Code
main()
