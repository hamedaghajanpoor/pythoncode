my_list = [{"First_name" : "hamed ", "Last_name" : "Aghajanpoor", "Birth_year": 1990} ,{"First-name":"ali ", "Last_name": "ahmadi", "Berth_year": 1994}]
current_year = 2025

#مشخصات اولین نفر
Number1 = (my_list[0]["First_name"] + my_list[0]["Last_name"]).upper()
age1 = current_year - my_list[0]["Birth_year"]
print("Number1:" , Number1)

#مشخصات دومین نفر
Number2 = (my_list[1]["First_name"] + my_list[1]["Last_name"]).upper()
age2 = current_year - my_list[1]["Birth_year"]
print("Number2:" , Number2)

#محاسبه سن
average_age = (age1 + age2)/2 
print("Average_Age :" , average_age) 
