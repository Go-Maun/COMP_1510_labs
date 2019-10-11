from Lab05.functions_lab05 import shop
from Lab05.functions_lab05 import choose_inventory
from Lab05.functions_lab05 import choose_inventory_messages
from Lab05.functions_lab05 import create_character
from Lab05.functions_lab05 import print_character
from Lab05.functions_lab05 import add_items_to_character
from Lab05.functions_lab05 import print_items


def main():
    print("\nYou stroll into a store, blood pumping as the idea of adventure fills your mind.\n")
    print('"Welcome to Orvishs Odds and Ends" calls a voice by the counter.\n')
    bought = int(input('"How many items can I interest you with?" '))
    inventory_chosen = choose_inventory(shop(), bought)
    choose_inventory_messages(shop(), inventory_chosen, bought)
    print("\nAs you walk out of Orvishs Odds and Ends you notice a broken mirror leaning on the building wall.\n")
    print("Looking in the miror at your reflection, a thought crosses your mind. 'I need a name for myself!'\n")
    name = int(input("'Not something terribly long. How many syllables? I know! How about' "))
    character = create_character(name)
    print("'", name, "is the perfect amount! Now the letters.'\n")
    print("As you sit there, concentrating really hard you decide on your adventuring name, "
          "as well as calculating your different attributes and items you own.\n")
    print_character(character)
    add_items_to_character(character, inventory_chosen)
    print_items(character, shop(), bought)
    input("Press Enter to Continue")
    if bought <= 0:
        print("\nYour heart races even more as you step out through the town's gate, "
              "ready to start your first adventure.\nBut as you step through the gate, a Gigantic Ancient White Dragon"
              " flies overhead, breathing intense frost all over the town, including yourself.\nFrozen to death, "
              "your corpse sits there, becoming a decoration for the dragons lair.")
    elif bought > 0:
        print("\nYour head starts to race with the idea of adventure.'Just through this ally is the front gate of town!"
              "' you think to yourself.\nSuddenly, a sharp pain is felt in the back of your neck as you get jumped "
              "by multiple thiefs.\n'Look at all this loot he has!' is the last thing you hear before you fall to the "
              "dark abyss of death.")


if __name__ == "__main__":
    main()
