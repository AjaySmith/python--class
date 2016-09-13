print("Please enter the number of ninjas below:")
ui = input()
ninjas = float(ui)

if ninjas > 30 and ninjas <= 50:
    print("That's too many.")

elif ninjas > 10 and ninjas <= 30:
    print("It'll be a struggle, but I can take 'em.")

elif ninjas < 10:
    print("I can fight those ninjas!")
