name = input("What is your name? ")
print(name)

age = input ("What is your age?")
print(age)

city = input ("What is your city?")
print(city)

love = input ("What you love doing?")

print("=" * 30)

string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, love)

print(output)

