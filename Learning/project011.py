# https://www.youtube.com/watch?v=mzSJpn9ldt4&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=19&ab_channel=CursoemV%C3%ADdeo
# wall painting

width = float(input("What's the width?"))
height = float(input("Whats the height?"))
area = width * height
# 2m² = 1L paint
paint = area / 2
print(f"Your wall have an dimension of {width}x{height} and it's area is: {area:.3f}m²")
print(f"So, you need {paint:.3f}L of paint.")