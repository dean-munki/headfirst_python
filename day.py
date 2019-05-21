from datetime import date

today = date.today().strftime('%A')
print(today)
if today == 'Saturday':
    print('Party!')
elif today == 'Sunday':
    print('Recover, then rest.')
else:
    print('Work, Work, Work!')
