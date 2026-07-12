# # print("hamed-dev")

# # full_name = "  hamed aghajanpoor  "
# # full_name = full_name.rstrip()
# # print(full_name)


# city = "vienna"
# temperature = 23.7


# print( 'weather in %s: %f°C' % (city, temperature))

# 'weather in {0}: {1}°C'.format(city, temperature)
# 'weather in {}: {}°C'.format(city, temperature)
# 'weather in {c}: {t}°C'.format(c=city, t=temperature)

# print(f'weather in {city}: {temperature}°C')

# import math

# print(f"Pi is {math.pi:.4f}")
# # Pi is 3.1416
# print(f"Pi is {math.pi:.4g}")
# # Pi is 3.142

# first_name= "Hamed"
# last_name = "Aghajanpoor"

# print(f"{first_name:^20}")


# menu_item = "burger"
# price = 11.5

# print(f"{menu_item:<12} {price:>5.2f}$")


# users = ['mike', 'tim' , 'theresa']

# for user in users:
#     print(user.upper())

person = {
    "first_name": "John",
    "last_name": "Doe",
    "nationality": "canada",
    "birth_year": 1980,
}

for k, v in person.item():
    print(k + " " + str(v))
