# Interview

#Data

name=input("Enter your Name ")
year_of_birth=input("Enter the year you're born")
phoneNo=input("Enter your contact Number")
area=input("where do you live-")
details=[]

# Processing
name=name.upper()
details.append(name)
year_of_birth = int(year_of_birth)
details.append(year_of_birth)
age = 2019-year_of_birth
details.append(age)

# display
print("""
Hi,
Below are the details you entered,
Name : %s
Age : %s
PhoneNo : %s
Area : %s """%(name,age,phoneNo,area.capitalize()))

print("\n\n details are: ",details)