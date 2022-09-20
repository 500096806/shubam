# Write a progam to fill in a letter template given below with name and date.
# letter = '''Dear <|NAME|>,
#                 YOu are selected!!
#                 <|DATE|>'''



letter ="Dear <|NAME|>,\nYOu are selected!!\n<|DATE|>"

name = (input("Enter name_____\n"))
date = (input("Enter Todays Date_____\n"))
letter=letter.replace("NAME",name)
letter=letter.replace("DATE",date)
print(letter)
