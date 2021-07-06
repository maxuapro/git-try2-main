

def add_time(start, duration, weekday=''):
    list, daytime = start.split(' ')

    time_start_hrs, time_start_mins = list.split(':')
    time_dur_hrs, time_dur_mins = duration.split(':')

    time_start_hrs = int(time_start_hrs) if daytime == 'AM' else int(
        time_start_hrs) + 12
    time_start_mins = int(time_start_mins)
    time_dur_hrs = int(time_dur_hrs)
    time_dur_mins = int(time_dur_mins)

    mins_sum = 0
    hrs_sum = 0

    if (time_dur_mins + time_start_mins) // 60 == 0:
        hrs_sum = time_start_hrs + time_dur_hrs
        mins_sum = time_start_mins + time_dur_mins
    else:
        hrs_sum = time_start_hrs + time_dur_hrs + 1
        mins_sum = (time_start_mins + time_dur_mins) % 60

    # print(hrs_sum, mins_sum)

    number_of_days = hrs_sum // 24
    # print('number_of_days', number_of_days)

    remaining_hrs = hrs_sum - number_of_days * 24
    if remaining_hrs < 12:
        new_daytime = 'AM'
        if remaining_hrs == 0:
            hrs_output = '12'
        else:
            hrs_output = str(remaining_hrs)
    else:
        new_daytime = 'PM'
        if remaining_hrs == 12:
            hrs_output = '12'
        else:
            hrs_output = str(remaining_hrs - 12)


    # mins
    if len(str(mins_sum)) == 1:
        mins_output = '0' + str(mins_sum)
    else:
        mins_output = str(mins_sum)

    output_str = hrs_output + ':' + mins_output + ' ' + new_daytime

    if number_of_days == 1:
        days_specific = ' (next day)'
    elif number_of_days > 1:
        days_specific = ' (' + str(number_of_days) + ' days later)'
    else:
        days_specific = ''


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
        if later == 0:
            return ', ' + day.capitalize()
        if not days.index(day.capitalize()):
            return ''

        ind = days.index(day.capitalize()) + 1

        new_ind = (later + ind) % len(days)
        return ', ' + days[new_ind - 1]
    
    the_day = ''
    if weekday:
        the_day = get_day(weekday, number_of_days)


    output_str += the_day + days_specific

    return output_str


time1, dur1, day1 = "11:30 AM", "2:32", "Monday"  # Returns: 2:02 PM, Monday
# Returns: 12:03 AM, Thursday (2 days later)
time2, dur2, day2 = "11:43 PM", "24:20", "tueSday"

print(add_time(time1, dur1, day1))
print(add_time(time2, dur2, day2))
print(add_time("10:10 PM", "3:30"))
print(add_time("6:30 PM", "205:12"))
