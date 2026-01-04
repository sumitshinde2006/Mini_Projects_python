import sys
import random
print("welcome to chapter 1 in which we are making random names\n")
first=["John", "Jane", "Sam", "Sara", "Alex", "Alice", "Mike", "Mia", "Tom", "Tina", "Chris", "Cathy", "David", "Diana", "Evan", "Eva", "Frank", "Fiona", "George", "Grace", "Harry", "Hannah", "Ian", "Ivy", "Jack", "Jill", "Kevin", "Kara", "Liam", "Luna", "Matt", "Molly", "Nate", "Nina", "Owen", "Olivia", "Paul", "Paula", "Quinn", "Queen", "Ryan", "Rita", "Sammy", "Sophie", "Tommy", "Tara", "Umar", "Uma", "Vince", "Vera", "Will", "Wendy", "Xander", "Xena", "Yusuf", "Yara", "Zack", "Zoe", "Adam", "Ava", "Ben", "Bella", "Caleb", "Chloe", "Dylan", "Daisy", "Ethan", "Ella", "Finn", "Faye", "Gavin", "Gina", "Hugo", "Hazel", "Isaac", "Isla", "Jake", "Jade", "Kyle", "Kira", "Luca", "Lily", "Mason", "Maya", "Nolan", "Nora", "Omar", "Opal", "Parker", "Penny", "Quentin", "Queenie", "Riley", "Rosa", "Sean", "Sally", "Tyler", "Tessa", "Ulysses", "Ursula", "Violet", "Victor", "Wade", "Willa", "Ximena", "Xavier", "Yvonne", "Yosef", "Zane", "Zara"]
last=["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson", "Baker", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins",  "Perry",  "Powell","Long","Patterson","Hughes","Flores","Washington","Butler","Simmons","Foster","Gonzales","Bryant","Alexander","Russell","Griffin","Diaz","Hayes"]
while True:
    first=random.choice(first)
    last=random.choice(last)
    print("{} {}".format(first,last),file=sys.stderr)
    print("\n\n")
    try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
    if try_again.lower() == "n":
        break    

    input("\npress enter to exit") 
