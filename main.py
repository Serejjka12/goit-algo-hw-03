from datetime import datetime
import random
import re


# Задание номер 1

def get_days_from_today(date):
    str_date = datetime.strptime(date, "%Y.%m.%d").date()
    now_date = datetime.today().date()
    different = (now_date - str_date).days
    return different

