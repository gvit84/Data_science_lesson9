#Task_1
class Car:
    def __init__(self, model, color, engine_capacity):
        self.model = model
        self.color = color
        self.engine_capacity = engine_capacity
        self.drive_direction = None

    def drive_forward(self):
        if self.model != 'BMW' and self.engine_capacity >= 2 and self.color != 'grey':
            self.drive_direction = "Go forward"
        else:
            self.drive_direction = "Stop"

    def drive_back(self):
        if 1.0 <= self.engine_capacity <= 1.3:
            self.drive_direction = "Go back"



class Car2(Car):
    def __init__(self, model, color, engine_capacity):
        Car.__init__(self, model, color, engine_capacity)

    def drive_left(self):
        if self.color == 'white':
            self.drive_direction = "Turn left"

    def drive_right(self):
        if self.color == 'green':
            self.drive_direction = "Turn right"


car2 = Car2('Audi', 'black', 1.3)
print(car2.model, car2.color, car2.engine_capacity)
car2.drive_forward()
car2.drive_back()
car2.drive_left()
car2.drive_right()
print(car2.drive_direction)



