# ask the user to enter any number between 1-5 and print that number
# in words
# if user enters 1 , print One

number=int(input("Enter any number between 1-5 "))


if number==1:
	print("You've entered One")
elif number==2:
	print("You've entered Two")
elif number==3:
	print("You've entered Three")
elif number==4:
	print("You've entered Four")
elif number==5:
	print("You've entered Five")
else:
	print("the number you entered is out of range")
