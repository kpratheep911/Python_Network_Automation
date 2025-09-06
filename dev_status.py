import os
device=input("enter your ip address")
response=os.system(f"ping -n 1 {device} >nul")
if response==0:
	print(f"{device} is reachable")
else:
	print(f"{device} is not reachable")
