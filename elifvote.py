age=int(input("Enter your age"))

print(f"you are {age} years old")

if age<0:
	print("Age cannot be negative")
elif age<18:
        print("you are under 18. Hence you are not eligible to vote")
elif age>=18 and age<=60:
	print("You are eligible to vote")
else:
	print("You are senior citizen and eligible to vote")
