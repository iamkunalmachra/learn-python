import random
name = input("Enter your name: ")
question=input("Enter your question :")
if name == "":
  print("Question: "+question)
else:
  print(name+ " asks: " + question)
  
if question == "":
  print("I couldn't read your question")
else:
  answer=""
  print("Magic 8-Ball's answer: "+answer)
  random_number=random.randint(1,10)
  if random_number==1:
    print("Yes - definitely.")
  elif random_number==2:
    print("It is decidedly so.")
  elif random_number==3:
    print("Without a doubt.")
  elif random_number==4:
    print("Reply hazy, try again.")
  elif random_number==5:
    print("Ask again later.")
  elif random_number==6:
    print("Better not tell you now.")
  elif random_number==7:
    print("My sources say no.")
  elif random_number==8:
    print("Outlook not so good.")
  elif random_number==9:
    print("Very doubtful.")
  elif random_number==10:
    print("Signs point to yes")
  else:
    print("Error")
