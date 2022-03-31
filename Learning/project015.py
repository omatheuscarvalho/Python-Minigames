# https://www.youtube.com/watch?v=I4NYUeetLAc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=23&ab_channel=CursoemV%C3%ADdeo
# car rent

# Price = day rent * 60,00; km driven * 0,15
dr = int(input("How many days you rent the car?"))
km = float(input("And how many km driven?"))
price = (dr * 60) + (km * 0.15)
print(f"The total cost is R${price:.2f}")