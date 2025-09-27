#list for jedi matstesr then removes anakin form jedi 
#anakin wants to be jedi masters - on the list but not the rank of master 
#return all jedis
#return all jedis that are jedi masters 
#list of masters 
#list of jedi


listOfJediMasters = [
    "Yoda", "Mace Windu", "Obi-Wan Kenobi", "Anakin Skywalker",
    "Plo Koon", "Kit Fisto", "Ki-Adi-Mundi", "Shaak Ti",
    "Luminara Unduli", "Depa Billaba", "Quinlan Vos", "Jocasta Nu",
    "Qui-Gon Jinn", "Aayla Secura", "Luke Skywalker"
]

#print ("Here is the list of jedi: " + listOfJediMasters)


print ("Which jedi would you like to check the status of?")

jediStatusCheck = str(input())

if jediStatusCheck != "Anakin Skywalker":
    print (jediStatusCheck + " is a Jedi Master!")
else: 
    print ("\nAnakin Skywalker is not a Jedi Master!")

