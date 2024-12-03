newphrase = "rainstorm"
            # 012345678
            # 123456789 --> Collegeboard version 
# Create a new variable called shortphrase and assign it a value by slicing
# the new phrase variable by removing the first 3 characters and the last 3 characters
# The first 3 characters are "rai"
# The last 3 characters are "orm"
# substring(string, start, end)
shortphrase = newphrase[3:-3]
print(shortphrase) # Output = nst
# OR
shortphrase2 = newphrase[3:len(newphrase)-3]
# Collegeborad version --> [4:len(newphrase)-6]
# Explain len(newphrase)-3 = 9-3 = 6
# Why does it end with 6?
# Because the last index is not included 
print(shortphrase2) # Output = nst

age = 20 
fun = False
likes_to_dance = False

if (age < 30 or fun) and likes_to_dance:
    print("You're invited!")
else:
    print("Get awat you freakbag")

if (age < 30 or fun):
    if likes_to_dance:
        print("You're invited!")
    else:
        print("Oh no, you can't dance")
else:
    print("You're not invited... sorry!")
