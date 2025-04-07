import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2025, 3, 17)

days_away = (next_birthday - today).days

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f'My nest birthday is {days_away} days away! ')

