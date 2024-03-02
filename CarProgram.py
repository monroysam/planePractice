import CarClass as c

def main():
    car = c.Car("2024", "Tesla")

    #accelerate
    car.accelerate()
    print(f"Current speed is: {car.get_speed()}")

    car.accelerate()
    print(f"Current speed is: {car.get_speed()}")

    car.accelerate()
    print(f"Current speed is: {car.get_speed()}")

    car.accelerate()
    print(f"Current speed is: {car.get_speed()}")
    
    car.accelerate()
    print(f"Current speed is: {car.get_speed()}")

    #brake
    car.brake()
    print(f"Current speed is: {car.get_speed()}")

    car.brake()
    print(f"Current speed is: {car.get_speed()}")

    car.brake()
    print(f"Current speed is: {car.get_speed()}")

    car.brake()
    print(f"Current speed is: {car.get_speed()}")

    car.brake()
    print(f"Current speed is: {car.get_speed()}")

main()