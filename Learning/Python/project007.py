# https://www.youtube.com/watch?v=_QfISzy0IKs&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=15&ab_channel=CursoemV%C3%ADdeo
# grade average score

# s = score
from zoneinfo import available_timezones


s1 = float(input("Type the first score"))
s2 = float(input("And the seccound one"))
average = (s1 + s2) / 2

print(f"The average score is {average:.1f}")