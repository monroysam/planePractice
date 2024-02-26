
import PhoneClass as p

def main():

    phone = p.Phone("Apple", "iPhone 15", 999)

    print(f"The phone manufactuer is: {phone.get_manufact()}")
    print(f"The phone model is: {phone.get_model()} ")
    print(f"The phone price is: ${phone.get_price():,.2f}")

main()