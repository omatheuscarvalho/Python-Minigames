# https://www.youtube.com/watch?v=_Nk02-mfB5I&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=28&ab_channel=CursoemV%C3%ADdeo
# sort a list
import random

s1 = input("First student")
s2 = input("Seccound student")
s3 = input("Third student")
list = [s1, s2, s3]

choosen = random.choice(list) 
print(f"The choosed student was: {choosen}.")
random.shuffle(list)
print(f"The order o appresentation will be: \n{lis}")