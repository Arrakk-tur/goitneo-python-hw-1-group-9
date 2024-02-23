from collections import defaultdict
from datetime import datetime

test_users = [
    {"name": "John Doe", "birthday": datetime(1990, 2, 23)},
    {"name": "Jane Smith", "birthday": datetime(1984, 8, 22)},
    {"name": "Michael Johnson", "birthday": datetime(1977, 3, 11)},
    {"name": "Emily Davis", "birthday": datetime(1995, 11, 7)},
    {"name": "James Brown", "birthday": datetime(1988, 2, 18)},
    {"name": "Sarah Miller", "birthday": datetime(1992, 6, 30)},
    {"name": "Robert Clark", "birthday": datetime(1980, 9, 25)},
    {"name": "Jennifer Taylor", "birthday": datetime(1973, 12, 14)},
    {"name": "Daniel Wilson", "birthday": datetime(1998, 2, 18)},
    {"name": "Laura Martinez", "birthday": datetime(1982, 1, 9)},
]


def get_birthdays_per_week(users):
    today = datetime.today().date()
    res = defaultdict(list)
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year > today:
            birthday_this_year.replace(year=today.year + 1)
            delta_days = (birthday_this_year - today).days
            if delta_days < 7:
                birthday_week_day = birthday_this_year.strftime("%A")
                if birthday_week_day == ("Sunday" or "Saturday"):
                    res["Monday"].append(name)
                else:
                    res[birthday_week_day].append(name)

    for key, value in res.items():
        birth_name = ", ".join(value)
        print(f"{key}: {birth_name}")
