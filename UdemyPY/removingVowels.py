vowels = ("a", "e", "i", "o", "u")
#input from the user
message = raw_input("Enter your message: ")
#variable with empty string
new_message = ""

for letter in message:
	if letter not in vowels:
		# add each letter not in vowel to the variable 'new_message'
		new_message += letter
	# prints letters matches in tupple 'vowels'
	if letter in vowels:
		print(letter, "I am a vowel.")
# prints new_message
print(new_message)