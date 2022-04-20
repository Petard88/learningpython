favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#language = favorite_languages['sarah'].title()
#print(f"Sarah's favorite language is {language}.") #old solution

#for name, language in favorite_languages.items(): #loops through the dictionary
    #print(f"{name.title()}'s favorite language is {language.title()}") #prints the keys and values as formatted

#for name in favorite_languages.keys(): # pulls all the keys
    #print(name.title()) #prints all the keys

#friends = ['phil', 'sarah']
#for name in favorite_languages.keys(): #för varje key printas meddelandet. name blir lika med key-namnet
#    print(f"Hi {name.title()}.")

#    if name in friends: #om namnet finns i friends listan printas ett extra meddelande
#        language = favorite_languages[name].title()
#        print(f"\t{name.title()}, I see you love {language}.")
#if 'erin' not in favorite_languages.keys(): #om erin inte finns i keys så printas meddelandet.
#    print("Erin, please take our poll!")

#for name in sorted(favorite_languages.keys()): #sorterar i alfabetisk ordning i keys.
#    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
#for language in favorite_languages.values(): #för varje key-value, lagra i variabeln language
#    print(language.title()) #printa variabeln language med stor bokstav
for language in set(favorite_languages.values()): #set kollar efter unika values och ignorerar duplicates
    print(language.title())