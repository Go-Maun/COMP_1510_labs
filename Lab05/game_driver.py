from Lab05.functions_lab05 import shop
from Lab05.functions_lab05 import choose_inventory
from Lab05.functions_lab05 import choose_inventory_messages
from Lab05.functions_lab05 import create_character
from Lab05.functions_lab05 import print_character


def main():
    print("You stroll into a store, blood pumping as the idea of adventure fills your mind.\n")
    print('"Welcome to Orvishs Odds and Ends" cried a voice by the counter.\n')
    bought = int(input('"How many items can I interest you with?" '))
    choose_inventory_messages(shop(), choose_inventory(shop(), bought), bought)
    print("\nAs you walk out of Orvishs Odds and Ends you notice a broken mirror leaning on the building wall.\n")
    print("Looking in the miror at your reflection, a thought crosses your mind. 'I need a name for my self!'\n")
    name = int(input("'Not something terribly long. How many syllables? I know! How about' "))
    print("'", name, "is the perfect amount! Now the letters.'\n")
    print("As you sit there, concentrating really hard you decide on your adventuring name, "
          "as well as calculating your different attributes and items you own.\n")
    print_character(create_character(name, shop(), bought), bought)
    input("Press Enter to Continue")
    if bought <= 0:
        print("Your heart races even more as you step out through the town's gate, "
              "ready to start your first adventure.\nBut as you step through the gate, a Gigantic Ancient White Dragon"
              "flies overhead, breathing intense frost all over the town, including yourself.\nFrozen to death, "
              "your corpse sits there, becoming a decoration for the dragons lair.")
    elif bought > 0:
        print("Your head starts to race with the idea of adventure.'Just through this ally is the front gate of town!'"
              " you think to yourself.\nSuddenly, a sharp pain is felt in the back of your neck as you get jumped "
              "by multiple thiefs.\n'Look at all this loot he has!' is the last thing you hear before you fall to the "
              "dark abyss of death.")


if __name__ == "__main__":
    main()
