# Strings
#    data that falls within " " marks

# Concatenation
#  Put 2 or more strings together

firstName = "Fred"
lastName = "Flinstone"

fullName = firstName + " " + lastName

print(fullName)

# Repetition
#  repetition operator: *

print("Hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row, "*3 + 'your boat')
    print("Gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")

rowYourBoat()

# Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)

middleCharIndex = len(name) // 2
print(middleCharIndex)
print(name[middleCharIndex])

print(name[-3])

for i in range(0, len(name)):
    print(name[i])

# Slicing and dicing

print(name[-4:8])

for i in range(0, len(name)+1):
    print(name[0:i])

# Searching

print("biv" in name)

if "y" not in name:
    print("y is not in name")
else:
    print("y is in name")

    # String Methods to investigate:
    # Method        Use Example         Explanation
    # center        aStr.center(w)      returns a centered string
    # ljust         aStr.ljust(w)       returns a left justified version of the string
    # rjust         aStr.rjust(w)       returns a right justified version of the string
    # upper         aStr.upper()        converts a string into upper case
    # lower         aStr.lower()        converts a string into lower case
    # index         aStr.index(item)        searches the string for a specified value and returns the position of where it was found
    # rindex        aStr.rindex(item)       searches the string for a specified value and returns the last position of where it was found
    # find          aStr.find(item)     searches the string for a specified value and returns the position of where it was found
    # rfind         aStr.rfind(item)        searches the string for a specified value and returns the last position of where it was found
    # replace       aStr.replace(old, new)      returns a string where a specified value is replaced with a specified value

    # Be sure to include multiple examples of all of them in use