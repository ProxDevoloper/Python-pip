import random

class Human:
    def __init__(self, name="Survivor"):
        self.name = name
        self.health = 100
        self.hunger = 50
        self.water = 50
        self.morale = 50
        self.supplies = 30  
        self.radiation = 0  
        self.weapon_durability = 50  
        self.shelter_safety = 50  

    def eat(self):
        if self.supplies > 0:
            print(f"{self.name} поел немного запасов.")
            self.hunger += 20
            self.supplies -= 10
        else:
            print(f"{self.name} нет запасов! Нужно искать еду.")

    def drink(self):
        if self.supplies > 0:
            print(f"{self.name} выпил воды из запасов.")
            self.water += 20
            self.supplies -= 10
        else:
            print(f"{self.name} нет воды! Нужно искать запасы.")

    def scavenge(self):
        print(f"{self.name} отправился на поиски ресурсов.")
        found_supplies = random.randint(0, 30)
        found_water = random.randint(0, 20)
        self.supplies += found_supplies
        self.water += found_water
        self.weapon_durability -= 10
        self.radiation += random.randint(5, 15)
        self.morale -= 5
        print(f"{self.name} нашел {found_supplies} еды и {found_water} воды, но увеличил радиацию.")

    def defend(self):
        print(f"{self.name} отбился от мутантов.")
        self.weapon_durability -= random.randint(5, 20)
        self.health -= random.randint(5, 15)
        self.shelter_safety -= random.randint(5, 15)
        self.morale -= 5

    def repair_shelter(self):
        print(f"{self.name} укрепил убежище.")
        self.shelter_safety += 20
        self.morale += 5

    def rest(self):
        print(f"{self.name} отдыхает в убежище.")
        self.health += 15
        self.morale += 10
        self.radiation -= 5

    def status(self, day):
        print(f"\nДень {day}. Состояние {self.name}:")
        print(f"Здоровье: {self.health}, Голод: {self.hunger}, Жажда: {self.water}")
        print(f"Мораль: {self.morale}, Радиоактивность: {self.radiation}")
        print(f"Запасы: {self.supplies}, Прочность оружия: {self.weapon_durability}, Безопасность убежища: {self.shelter_safety}")

    def live(self, day):
        self.status(day)

        if self.hunger < 20:
            self.eat()
        elif self.water < 20:
            self.drink()
        elif self.shelter_safety < 30:
            self.repair_shelter()
        elif self.weapon_durability < 20:
            self.scavenge()
        elif self.radiation > 50:
            print(f"{self.name} подвергся радиационному воздействию! Нужно отдыхать.")
            self.rest()
        else:
            action = random.choice(["scavenge", "rest", "defend", "repair_shelter"])
            if action == "scavenge":
                self.scavenge()
            elif action == "rest":
                self.rest()
            elif action == "defend":
                self.defend()
            elif action == "repair_shelter":
                self.repair_shelter()


        if self.health <= 0 or self.radiation >= 100 or self.hunger <= 0 or self.water <= 0:
            print(f"{self.name} не выжил в пустоши...")
            return False
        return True


survivor = Human(name="Алекс")


for day in range(1, 150):  
    if not survivor.live(day):
        break

print("Конец симуляции.")
