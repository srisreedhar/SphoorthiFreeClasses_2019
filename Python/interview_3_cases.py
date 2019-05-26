# Interview

#Data

name=input("Enter your Name ")
year_of_birth=input("Enter the year you're born")
phoneNo=input("Enter your contact Number")
area=input("where do you live-")

# Processing
name=name.upper()
year_of_birth = int(year_of_birth)
age = 2019-year_of_birth

# display
print("""
Hi,
Below are the details you entered,
Name : %s
Age : %s
PhoneNo : %s
Area : %s """%(name,age,phoneNo,area.capitalize()))