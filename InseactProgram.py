import InsectsClass as i

def main():
    mosquito = i.Insect(2,4,"Mosquito") #instance of mosquito
    housefly = i.Insect(2,4,"Housefly") #instance of housefly

    mosquito.flight_calc()
    housefly.flight_calc()

    print(f"The {mosquito.get_name()} can fly {mosquito.get_miles()} miles")
    print(f"The {housefly.get_name()} can fly {housefly.get_miles()} miles")
    
main()