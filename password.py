import random

## characters to generate password from

print("Welcome to your password generator")


characters = list("/nd/safldkdfmkgk.jgunflfjnui,jp.9q3/8i0-2[woi/3pqp;.sp;ldsxz/ld;")

def generate_random_password():
	## length of password from the user
	length = int(input("Enter password length: "))
	

	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## shuffling password
	random.shuffle(password)

	## printing the list
	print("".join(password))


## calling the function
generate_random_password()


	
	

