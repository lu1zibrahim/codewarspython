print("///////////////////////////DICE ROLLER///////////////////////////")
print("Please select an option for the desired dice")
print("For d4 type '4'")
print("For d8 type '8'")
print("For d10 type '10'")
print("For d12 type '12'")
print("For d20 type '20'")
print("For d100 type '100'")

dice_value = int(input("What is the dice that you want? "))

from random import randint

def diceRoller(dice):
    mylist = [4,8,10,12,20,100]
    if dice in mylist:
        print("\n")
        print(f"You rolled: {randint(1,dice)}")
    else:
        print("\n")
        print("Please type a valid value of the dice")
        

diceRoller(dice_value)