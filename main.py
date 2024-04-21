from datetime import datetime
import random
import re


# Задание номер 1

def get_days_from_today(date):
    str_date = datetime.strptime(date, "%Y-%m-%d").date()
    now_date = datetime.today().date()
    different = (now_date - str_date).days
    return different


# Задание номер 2

def get_numbers_ticket(min, max, quantity):
    final_set = set()
    different = max - min
    if min >= 1 and max <= 1000 and max > min and quantity <= different:
        while len(final_set) <= quantity - 1:
            final_set.add(random.randint(min, max))
    else:
        return list(final_set)
    return list(sorted(final_set))


#Задание номер 3

def normalize_phone(phone_number):
    pattern = r"\d"
    matches = re.findall(pattern, phone_number)
    if matches[0] != "+":
        matches.insert(0, "+")
    if matches[1] != "3":
        matches.insert(1, "3")
    if matches[2] != "8":
        matches.insert(2, "8")
    if matches[3] != "0":
        matches.insert(3, "0")
    return ("".join(matches))





