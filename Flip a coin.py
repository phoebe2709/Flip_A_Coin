import random

def flip_coin():
    random_number = random.randint(1,2)
    if random_number == 1:
        side = "heads"
    else:
        side = "tails"
    return side

choice = input("heads or tails:")
result = flip_coin()

print("The coin landed on {}".format(result))

if choice == result:
    print("You won")
else:
    print("You loss")