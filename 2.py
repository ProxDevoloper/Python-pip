class cat:
  def __init__(self,name,age):
    self.name = name
    self.age = age
    self.is_hungry = True
    self.is_sleeping = False

    def eat(self):
        print(f"{self.name} кушает")
        self.is_hungry = False

    def sleep(self):
        print(f"{self.name} Спит..(не будите его)")
        self.is_sleeping = True

    def wake_up(self):
        print(f"{self.name} Проснулся,хороший котик!")
        self.is_sleeping = False

    def play(self):
        print(f"{self.name} играет,какая прелесть!")

