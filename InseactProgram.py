import InsectsClass as i

def main():
    mosquito = i.Insect()
    housefly = i.Insect()

    mosquito.flight_calc()
    housefly.flight_calc()

    print(f"The mosquito can fly {mosquito.get_miles()} miles")
    print(f"The housefly can fly {housefly.get_miles()} miles")
    
main()