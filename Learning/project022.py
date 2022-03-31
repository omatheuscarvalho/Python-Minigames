# https://www.youtube.com/watch?v=EQQt-6QqXOs&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=32&ab_channel=CursoemV%C3%ADdeo
# Name counting

name = str(input("What's your name?")).strip()
print(f"Your name in upper is: {name.upper()}")
print(f"Your name in lower is: {name.lower()}")
print(f"Your name has {len(name) - name.count(' ')} letters.")
print(f"Your first name has {name.find(' ')} letters.")

