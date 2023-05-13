from datetime import datetime, timedelta

# Тестовий список колег

users = [
    {'name': 'John', 'birthday': datetime(1990, 5, 13).date()},
    {'name': 'Jane', 'birthday': datetime(1995, 5, 14).date()},
    {'name': 'Alice', 'birthday': datetime(1987, 5, 15).date()},
    {'name': 'Bob', 'birthday': datetime(2000, 5, 16).date()},
    {'name': 'Eva', 'birthday': datetime(1998, 5, 17).date()},
    {'name':'Rock', 'birthday': datetime(2001, 5, 18).date()},
    {'name':'Patrick', 'birthday': datetime(1996, 5, 19).date()},
    {'name':'Sandy', 'birthday': datetime(1993, 5, 20).date()},
    {'name':'Karen', 'birthday': datetime(1997, 5, 21).date()},
    {'name': 'Mark', 'birthday': datetime(2002, 5, 22).date()},
    {'name': 'Betty', 'birthday': datetime(1985, 5, 23).date()}]

def get_birthdays_per_week(users):

    birthdays_per_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': [],
    }

    day_number = {  0:'Monday',
                    1:'Tuesday',
                    2:'Wednesday',
                    3:'Thursday',
                    4:'Friday',
                    5:'Saturday',
                    6:'Sunday' }

    date_now=datetime.now().date()
    one_week=timedelta(weeks=1)
    future_week=date_now+one_week

    for user in users:

        name = user['name']
        birthday = user['birthday']
        birthday_this_year=datetime(year=date_now.year,month=birthday.month,day=birthday.day).date()

        # Якщо сьогодні понеділок, то перевіряємо чи було у когось з колег день народження у вихідні, щоб привітати їх сьогодні

        if birthday_this_year < date_now and date_now.weekday()==0:

            check_holiday=timedelta(days=2)
            last_date=date_now-check_holiday

            if last_date<= birthday_this_year < date_now:
                day_of_week=0
                full_weekday_name=day_number[day_of_week]

            birthdays_per_week[full_weekday_name].append(name)
        
        # Якщо сьогодні понеділок, то перевіряємо день народження колег на тиждень вперед так, щоб ті які будуть в найближчі вихідні не рахувалися до цього понеділка

        elif date_now <= birthday_this_year < future_week and date_now.weekday()==0:

            day_of_week = birthday_this_year.weekday()

            if 0 <= day_of_week < 5:
                full_weekday_name=day_number[day_of_week]
                birthdays_per_week[full_weekday_name].append(name)

        # Звичайна перевірка при умові, що сьогодні не понеділок

        elif date_now <= birthday_this_year < future_week:

            day_of_week = birthday_this_year.weekday()

            if 0 <= day_of_week < 5:
                full_weekday_name=day_number[day_of_week]
            else:
                day_of_week=0
                full_weekday_name=day_number[day_of_week]

            birthdays_per_week[full_weekday_name].append(name)

    # Вивід списку днів народжень колег у консоль, якщо такі є

    for iterator in range(date_now.weekday(),date_now.weekday()+7):

        edit_iterator=iterator % 7

        if edit_iterator==0:
            pass

        current_day= day_number[edit_iterator]
        list_full_weekday_name=birthdays_per_week[current_day]
        print(f"{current_day}: {', '.join(list_full_weekday_name)}")

get_birthdays_per_week(users)