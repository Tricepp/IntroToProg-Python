# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Isepp Rebane, 5/18/2023, Initial Commit
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"
objFile = () # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    objFile = open(strFile, "r")
    for row in objFile:
        strData = row.split(",")
        dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
        lstTable.append(dicRow)
    objFile.close()
except:
    print("File Not Found")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

# Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for objRow in lstTable:
            print(objRow["Task"] + "," + objRow["Priority"])
        continue

# Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Please Enter Task:")
        strPri = input("Please Enter Priority:")
        dicRow = {"Task": strTask, "Priority": strPri}
        lstTable.append(dicRow)
        print ("Task: ", strTask)
        print ("Task: ", strPri)
        continue

# Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
            taskdel = input("What would you like to delete?")
            for row in lstTable:
                if row["Task"].lower() == taskdel.lower():
                    lstTable.remove(row)
                    print("Data was deleted!")
                continue

# Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for i in lstTable:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        print("Data Saved!")
        continue

# Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exit Program")
        break  # and Exit the program