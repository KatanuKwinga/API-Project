from abc import ABC, abstractmethod
import random

# Abstract Character Class
class Character(ABC):
    def __init__(self, name, health):
        self._name = name
        self._health = health

    # Abstract methods where characters either attack or take damage
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def take_damage(self, amount):
        pass
    # Concrete method to see if character is alive or not
    def is_alive(self):
        return self._health > 0

# Player Class 
class Player(Character):
    # Constructor for the player class
    def __init__(self, name, health=100):
        super().__init__(name, health)
        self.inventory = []
    # Overridden method for when player makes an attack move
    def attack(self):
        print(f"{self._name} attacks!")
        return random.randint(5, 25)  # Randomized power of player attack
    
    # Overridden method for when player gets hit by enemy
    def take_damage(self, amount):
        self._health -= amount
        print(f"{self._name} takes {amount} damage! Health is now {self._health}")
    # Method for when a player picks up an item
    def pick_item(self, item):
        self.inventory.append(item)
        print(f"{self._name} picked up {item}")

# Base class descirbing enemies
class Enemy(Character):
    # Constructor
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength
    # Overriden damage method
    def take_damage(self, amount):
        self._health -= amount
        print(f"{self._name} takes {amount} damage! Health is now {self._health}")

# Goomba Subclass extending Enemy class
class Goomba(Enemy):
    def __init__(self):
        super().__init__("Goomba", health=50, strength=15)

    def attack(self):
        print("Goomba runs towards you to attack!")
        return random.randint(5, 15) # Randomized power of attack

# Koopa subclass extending enemy class
class Koopa(Enemy):
    # Constructor
    def __init__(self):
        super().__init__("Koopa", health=100, strength=25)
    # Overridden attack method
    def attack(self):
        print("Koopa throws a shell!")
        return random.randint(20, 35)

# Class describing the working of the game
class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.enemies = [Goomba(), Koopa()]  # List of enemy types

    def play_turn(self):
        enemy = random.choice(self.enemies)
        print(f"You come across a {enemy._name} ")

        # Loop explaining the fight between the player and enemy
        while enemy.is_alive() and self.player.is_alive():
            action = input("Select what you'd like to do: (1) Attack (2) Heal: ")
            if action == "1":
                damage = self.player.attack()
                enemy.take_damage(damage)
                if not enemy.is_alive():
                    print(f"Congrats! You have killed the {enemy._name} ")
                    break
            elif action == "2":
                self.player.pick_item("Health Potion")
                print("You drank potion and your health is up by 20!")
                self.player._health += 20

            # Enemy attacks back if it's still alive
            if enemy.is_alive():
                damage = enemy.attack()
                self.player.take_damage(damage)

        if not self.player.is_alive():
            print("Oh no! Game Over!")
        else:
            print("Well done pooks, you survived! For now...")
            

# Example Usage
if __name__ == "__main__":
    game = Game("Hero")
    game.play_turn()
