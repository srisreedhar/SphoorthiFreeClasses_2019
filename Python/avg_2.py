# collecting inputs and finding avg

# Data

maths=input("Enter your Maths marks- ")
sci=input("Your Science Marks ")
social=input(" your social marks ")
english=input('your Engish marks ')

# Processing
maths=int(maths)
sci=int(sci)
social=int(social)
english=int(english)
total=maths+sci+social+english
print("total ",total)
avg=total/4

# Display

print("Your avg is",avg)