# JavaScript way 
# create variable 
# let, var or const
# let name = "brandon";

name = "brandon"
last_name = "bennington"
age = 37
found = False
print(name)

# if / else statements
# if (found==False)
# {
# console.log("Hello world!")
# }else if(found==True){}

if age < 100:
    print("great youre not that old")
    print("im inside of the if statement")
elif age >100:
    print("you are old")
else:
    print("i dont know how you get here")
print("im outside of the if statement")

# function doSomething() {
#
#}

def sayHello():
    print("Hello there")

sayHello()

#list ... this are the arrays 
colors = ["black","blue","red","yellow"]
#add
colors.append("pink")
# get any element
print(colors[1])

# travel the list - for loop
# for(i=0; i<colors.length; i++)
# {
    # let tmp = colors[i]
    # console.log(tmp)
# }

for x in colors:
    print(x)
          


print(colors)


# dictionary 
me = {
    "firstName": "Brandon",
    "lastName": "Bennington",
    "age": 37, 
}
print(me)
# modify
me["age"]=99
# get the value 
print(me["firstName"])

