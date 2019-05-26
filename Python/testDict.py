# Interview

#Data

name=input("Enter your Name ")
year_of_birth=input("Enter the year you're born")
phoneNo=input("Enter your contact Number")
area=input("where do you live-")
details={}

# Processing
name=name.upper()
year_of_birth = int(year_of_birth)
age = 2019-year_of_birth

details["name"]=name
details["birthYear"]=year_of_birth
details["age"]=age
details['phoneNo']=phoneNo
details['area']=area
# display
print("""
Hi,
Below are the details you entered,
Name : %s
Age : %s
PhoneNo : %s
Area : %s """%(details.get(name),details.get(age),details.get(phoneNo),details.get(area).capitalize()))

print("\n\n details are: ",details)
