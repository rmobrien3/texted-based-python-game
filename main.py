import random

# Define weapons and their damage values
weapons = {
    "sword": 20,
    "dagger": 15,
    "bow": 10,
    "hammer": 13,
    "ar15": 30,
    "chicken": 100,
}

# Define enemy types and their health
enemy_type = {
    "dragon": 250,
    "goblin": 50,
    "knight": 75,
    "frieren": 500, 
}

# Player class
class Player:
    def __init__(self, name, weapon_choice):
        self.name = name
        self.health = 100
        self.weapon = weapon_choice
        self.attack = weapons[self.weapon]

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self):
        return random.randint(self.attack - 10, self.attack + 15)  # Some variation in damage


# Enemy class
class Enemy:
    def __init__(self):
        self.name = random.choice(list(enemy_type.keys()))  # Randomly choose an enemy
        self.health = enemy_type[self.name]  # Assign health based on enemy type
        self.weapon = random.choice(list(weapons.keys()))  # Random weapon choice
        self.attack = weapons[self.weapon]
        self.stuck_in_mimic = False

        if self.name == "frieren":
            print("A Mysterious and powerful elf mage has appeared, prepare for battle")
            self.special_abilities_used = False
    

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def attack_player(self):
        return random.randint(self.attack - 5, self.attack + 10)  # Some variation in enemy damage
    
    def heal(self):
        heal_amount = random.randint(10,100) #frieren heals for random amount
        self.health +=heal_amount
        print(f"{self.name} heals for {heal_amount} HP")
        self.special_abilities_used = True
    
    def increased_power(self):
        damage = random.randint(self.attack + 10, self.attack + 60)
        print(f"{self.name} used power increase and attacks with {damage} damage!")
        return damage
    
    def shield(self):
        print(f"{self.name} used magic shield, damage has now been reduced for the next turn")
        self.special_abilities_used = True
        return True #indicates shield is active
    
    def check_mimic(self): #mimic trap event
        return random.random() < 0.1 #10% chance frieren gets stuck in mimic
    
    #checks if a special ability should be used

    def use_special_ability(self, player):
        if self.name == 'frieren' and not self.special_abilities_used:
            ability_choice = random.choice(["heal", "increased_power", "shield"])
            if ability_choice == "heal":
                self.heal()
            elif ability_choice == "increased_power":
                return self.increased_power()
            elif ability_choice == "shield":
                self.shield()
            return True
        return False
            


# Function to handle the fight
def fight(player, enemy):
    print(f"\n{player.name} vs {enemy.name}")
    print(f"{player.name} uses {player.weapon}, damage: {player.attack}")
    print(f"{enemy.name} uses {enemy.weapon}, damage: {enemy.attack}\n")

    # Fight until someone dies
    while player.is_alive() and enemy.is_alive():

        if enemy.name == "frieren" and enemy.check_mimic():
            print(f"{enemy.name} got stuck in a mimic and loses a turn")
            enemy.stuck_in_mimic = True
        else: 
            enemy.stuck_in_mimic = False

        #checks if frieren used special abilities 
        special_damage = 0 
        if enemy.name == "frieren":
            special_abilities_used = enemy.use_special_ability(player)
            if special_ability_used and isinstance(special_damage, int):
                special_damage = special_abilities_used

        # Player attacks enemy
        damage = player.attack_enemy()
        print(f"{player.name} attacks {enemy.name} for {damage} damage!")
        enemy.take_damage(damage)
        print(f"{enemy.name} has {enemy.health} HP left.\n")

        if enemy.health <= 0:
            print(f"{enemy.name} has died, {player.name} wins!")
            break

        # Enemy attacks player
        damage = enemy.attack_player()
        print(f"{enemy.name} attacks {player.name} for {damage} damage!")
        player.take_damage(damage)
        print(f"{player.name} has {player.health} HP left.\n")

        if player.health <= 0:
            print(f"{player.name} has died, {enemy.name} wins!")
            break


# Main function to start the game
def main():
    player_name = input("Please input your player's name: ")

    # Show the available weapons for the player to choose from
    print("\nPlease pick your weapon:")
    for i, weapon in enumerate(weapons.keys(), 1):
        print(f"{i}. {weapon}")

    # Get the player's weapon choice
    choice = int(input("Please enter the number of the weapon you wish to use: "))
    weapon_choice = list(weapons.keys())[choice - 1]

    # Create the player object
    player = Player(player_name, weapon_choice)

    print("\nWelcome to the game!")
    print(f"{player.name}, you chose the {player.weapon}.\n")

    # Generate a random enemy
    enemy = Enemy()

    print(f"A wild {enemy.name} has appeared!\n")

    # Start the fight
    fight(player, enemy)
#asks the user if they want to play again
    while True:
        restart = input("\nWould you like to play again? ")
        if restart == "yes":
            main()
            break
        elif restart == "no":
            print("Exiting game")
            break
        else:
            print("Please enter yes or no.")


if __name__ == "__main__":
    main()