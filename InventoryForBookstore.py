import csv

print ("Welcome to Lenny's Bookshop Inventory System", '\n')
print ('Made by: Ahmed Yasser Sayed ','\n')
#The purpose of our program is to create a simple inventory system for a bookshop called Lenny's Bookshop
#Names of the group members who created the program are listed below

#Read Data
def Read_Data():
    csv_file = open('lenny.csv')  # to open csv
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    id = []
    name = []
    author = []
    category = []
    quantity = []
    unit = []
    total = []
    for line in csv_reader:
        id.append(line[0])
        name.append(line[1])
        author.append(line[2])
        category.append(line[3])
        quantity.append(line[4])
        unit.append(line[5])
        total.append(line[6])


#list data in an organized way
def List_Data():
    file = open('lenny.csv')
    csv_data = csv.reader(file)
    next(csv_data)

    print('ID', "\t\t", 'Title', "\t\t", 'Author', "\t\t", 'Category', "\t\t", 'Quantity', "\t\t", 'Unit_Price',
          "\t\t", 'Total_Price')#print the list
    print('------------------------------------------------------------------------')
    for line in csv_data:
        print(line)
        print("--------------------------------------------------------------------------------")


#Search by title or part of it
def Search_Title():
    file= open('lenny.csv', 'r')
    csvreader= csv.reader(file)
    next(csvreader)
    Title= input("Enter the Title Here: ")
    Title=Title.lower()
    for line in csvreader:#if the searche
        if(Title in line[1]):
            print('ID', "\t\t", 'Title', "\t\t", 'Author', "\t\t", 'Category', "\t\t", 'Quantity', "\t\t", 'Unit_Price',
                  "\t\t", 'Total_Price')
            print ("--------------------------------------------------------------------------------")
            print(line[0],"         ", line[1], "         ", line[2], "         ", line[3], "          ",line[4], "          ",line[5], "          ",line[6])
            print ("--------------------------------------------------------------------------------")
            print ('Searching Title successful...')


#Search by Author or part of it
def Search_Author():
    file= open('lenny.csv', 'r')
    csvreader= csv.reader(file)
    next(csvreader)
    author= input("Enter the Name of Author Here: ")
    author=author.lower()
    for line in csvreader:
        if(author in line[2]):
            print('ID', "\t\t", 'Title', "\t\t", 'Author', "\t\t", 'Category', "\t\t", 'Quantity', "\t\t", 'Unit_Price',
                  "\t\t", 'Total_Price')
            print("--------------------------------------------------------------------------------")
            print(line[0], "         ", line[1], "         ", line[2], "         ", line[3], "          ", line[4],
                  "          ", line[5], "          ", line[6])
            print("--------------------------------------------------------------------------------")
            print('Searching Title successful...')




#Add a new book: -
def add_new_book():
  book_id = input("Enter book ID: ")
  title = input("Enter title: ")
  author = input("Enter author: ")
  category = input("Enter category: ")
  quantity = input("Enter quantity: ")
  unit_price = input("Enter unit price: ")
  total_price = float(quantity) * float(unit_price)
  # Append new book to the CSV file
  with open('lenny.csv', 'a',newline='') as f:
    writer = csv.writer(f)
    writer.writerow([book_id, title, author, category, quantity, unit_price, total_price])
  print("Book added successfully")




# Delete an existing book in our data
def delete_book(book_id):
  # Read the data from the CSV file
  with open('lenny.csv', 'r') as f:
    reader = csv.reader(f)
    # Store the data in a list
    data = list(reader)
  # Find the index of the book to be deleted
  delete_index = -1
  for i, row in enumerate(data):
    if row[0] == book_id:
      delete_index = i
      break
  # Delete the book from the list
  if delete_index != -1:
    del data[delete_index]
    print("Book deleted successfully")
  else:
    print("Book not found")
  # Write the updated data to the CSV file
  with open('lenny.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
      writer.writerow(row)




#Add to current stock
def update_stock(bookid, quant):
    csv_file = open('lenny.csv')  # to open csv
    csv_reader = csv.reader(csv_file)
    id = []
    name = []
    author = []
    category = []
    quantity = []
    unit = []
    total = []

    for line in csv_reader:
        id.append(line[0])
        name.append(line[1])
        author.append(line[2])
        category.append(line[3])
        quantity.append(line[4])
        unit.append(line[5])
        total.append(line[6])
    # add book data to current stock
    for i in id:
        if (str(bookid) == i):
            index = id.index(str(bookid))
            quantity[index] = str(int(quantity[index]) + quant)
            total[index] = str(int(quantity[index]) * float(unit[index]))

    csv_file = open('lenny.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file)
    for i in range(len(id)):
        csv_writer.writerow([id[i], name[i], author[i], category[i], quantity[i], unit[i], total[i]])





# Remove from current stock
def Remove_stock(bookid, quant):
    csv_file = open('lenny.csv')  # to open csv
    csv_reader = csv.reader(csv_file)
    id = []
    name = []
    author = []
    category = []
    quantity = []
    unit = []
    total = []

    for line in csv_reader:
        id.append(line[0])
        name.append(line[1])
        author.append(line[2])
        category.append(line[3])
        quantity.append(line[4])
        unit.append(line[5])
        total.append(line[6])
    # remove book from current stock
    for i in id:
        if (str(bookid) == i):
            index = id.index(str(bookid))
            quantity[index] = str(int(quantity[index]) - quant)
            total[index] = str(int(quantity[index]) * float(unit[index]))

    csv_file = open('lenny.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file)
    for i in range(len(id)):
        csv_writer.writerow([id[i], name[i], author[i], category[i], quantity[i], unit[i], total[i]])






#To get total value of books
def total():
    file = open('lenny.csv', 'r')
    csvreader = csv.reader(file)
    next(csvreader)
    llist=[]
    for line in csvreader:
        llist.append(float(line[6].replace('$',"")))
    print("Total Value of Books is:",round(sum(llist),3))





#Save to Updated.csv
def save():
    csv_file = open('lenny.csv')
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    id = []
    name = []
    author = []
    category = []
    quantity = []
    unit = []
    total = []
    for line in csv_reader:
        id.append(line[0])
        name.append(line[1])
        author.append(line[2])
        category.append(line[3])
        quantity.append(line[4])
        unit.append(line[5])
        total.append(line[6])

    filename = open("updated.csv", "w", newline='')  # to make an updated database
    csv_writer = csv.writer(filename)

    newlist = list(zip(id, name, author, category, quantity, unit, total))
    for row in range(len(newlist)):
        csv_writer.writerow(newlist[row])

    filename.close()


#Main Screen

ans = True
while ans: #what appears to the system user
    print(""" 
    -----------------------
    1.Read data
    2.list data
    3.Search by Title
    4.Search by Author
    5.Add a New Book
    6.Delete a Book
    7.Add to Current Stock
    8.Delete from Current Stock
    9.Total Value of Books
    10.save
    11.Exit

    ----------------------
    """)
    #Work out all steps of the system process
    ans = input("What would you like to do? ")
    if ans == "1":
        Read_Data()
        #Counting number of rows without counting the header
        rowcount = -1
        for row in open("lenny.csv"):
            rowcount += 1
        print("Number of books present:-", rowcount)
        print("Reading Data is successful...")
    elif ans=="2":
        List_Data()
    elif ans=="3":
     Search_Title()
    elif ans=="4":
        Search_Author()
    elif ans=="5":
        add_new_book()
    elif ans=="6":
        book_id = input("Enter book ID: ")#user input id of the book to be deleted from our data
        delete_book(book_id)
    elif ans=="7":
        ID = input("Enter Book id : ")#user input id of the book to increase its cuurent stock
        quant = input("Enter quantity to add : ")#user input quantity to be added to current stock
        update_stock(ID, int(quant))
    elif ans=="8":
        ID = input("Enter Book id : ")#user input id of the book to decrease its current stock
        quant = input("Enter quantity to subtract : ")#user input quantity to be removed from current stock
        Remove_stock(ID, int(quant))
    elif ans=="9":
        total()
    elif ans=="10":
        save()
    elif ans=="11": #exit the inventory system process
        print ('Thank you for using our inventory system. Goodbye')
        exit()


