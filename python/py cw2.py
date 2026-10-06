header = """BOOKSTORE RECEIPT
------------------"""

book1 = "Python Basics"
price1 = 450

book2 = "Data Science Intro"
price2 = 600

total = price1 + price2

line1 = "\t{} \t₹{}".format(book1, price1)
line2 = "\t{} \t₹{}".format(book2, price2)
total_line = "\tTOTAL \t₹{}".format(total)

thank_you = "\nThank you for shopping with us!"

receipt = header + "\n" + line1 + "\n" + line2 + "\n" + total_line + thank_you

print(receipt.upper())