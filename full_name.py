first_name = "pEtter"
last_name = "erikSson"
full_name = f"{first_name} {last_name}"
print(full_name.title()) #prints my full name with uppercase first letters and lowercase rest

print(f"Hello, {full_name.title()}!")

message = f"\tHello, {full_name.title()}! ät skit!"
message2 = f"\nHello, \n{full_name.title()}! \nät skit!"
message3 = f"\n\tHello, \n\t\t{full_name.title()}! \n\t\t\tät skit!"
print(message)
print(message2)
print(message3)