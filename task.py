class Car:
    def __init__(self, model, speed, type, color):
        self.model = model
        self.speed = speed
        self.type = type
        self.color = color

    def print_info(self):
        print(f"Model: {self.model}, Speed: {self.speed}, Type: {self.type}, Color: {self.color}")
        
        
        if self.car_type != "diesel" and self.car_type != "benzene":
            print("خطأ: يجب أن يكون نوع السيارة 'diesel' أو 'benzene'.")


car1 = Car("Toyota", 200, "diesel", "blue")
car2 = Car("BMW", 250, "benzene", "black")
car3 = Car("Ford", 180, "electric", "red")

car_list = [car1, car2, car3]


for car in car_list:
    car.print_info()
