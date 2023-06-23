#Let's start a Coffee Shop together

#Let's build Robot Barista

print("Hello, welcome to JackTomo Coffee\n")

name = input("What is your name?\n")

#print("Hello " + name + ", thank you so much for coming in today!\nHere is our menu.\n")

menu = "Black Coffee, Latte, Flat White, Green Tea"

print(
  "Nice to meet you " + name +
  ", what will you be having from our menu today? These are our current options.\n\n\n"
  + menu)

order = input()

print("No problem " + name + ", you have chosen " + order +
      ". Excellent choice, your oder will be with you in just a few moments. ")
