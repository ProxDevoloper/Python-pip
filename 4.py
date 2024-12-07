class Engine:
  def __init__(self, horsepower):
      self.horsepower = horsepower

  def start_engine(self):
      return "Двигатель запустился,всего лошадиных сил: {}".format(self.horsepower)


class Wheels:
  def __init__(self, wheel_count):
      self.wheel_count = wheel_count

  def rotate_wheels(self):
      return f"Всё {self.wheel_count} колёса вращаются."


class Car(Engine, Wheels):
  def __init__(self, horsepower, wheel_count, brand):
    
      Engine.__init__(self, horsepower)
      Wheels.__init__(self, wheel_count)
      self.brand = brand

  def drive(self):
      engine_status = self.start_engine()
      wheel_status = self.rotate_wheels()
      return f"{self.brand} она едет. {engine_status} {wheel_status}"


my_car = Car(150, 4, "Тоёта")
print(my_car.drive())  
