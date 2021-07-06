def get_day(day, later):
    days = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    ]
    if not days.index(day.capitalize()):
        return ''

    ind = days.index(day.capitalize()) + 1

    new_ind = (later + ind) % len(days)
    return ' ' + days[new_ind - 1]


print(get_day('tueSday'))
