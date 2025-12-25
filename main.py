print("simple calculator")

while True:
  print("/nchoose an option:")
  print("1.addition")
  print("2.subtraction")
  print("3.multiplication")
  print("4.division")
  print("5.exit")

  choice=input("enter choice(1-5):")

  if choice=="5":
      print("exiting calculator.bye")
      break

  if choice not in ["1","2","3","4","5"]:
      print("invalid option.please select from 1 to 5")
      continue

  a=int(input("enter first number"))
  b=int(input("enter second number"))

  if choice=="1":
      print(a+b)
  elif choice=="2":
      print(a-b)
  elif choice=="3":
      print(a*b)
  elif choice=="4":
     if b==0:
        print("cannot divide by zero")
     else:
         print(a/b)

