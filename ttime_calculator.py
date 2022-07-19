def add_time(start, duration, week_day=False):
    days_of_the_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6} #dictionary datatypes with {}
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#duration
    duration_tuple = duration.partition(":") #Split the string at the first occurrence of sep(the delimiter). Then return the tuple(store multiple items in a single variable.): the 'character befor the sep' 'sep' 'leftover'
    hour  = int(duration_tuple[0])
    minute = int(duration_tuple[2])
#start
    start_tuple = start.partition(":") 
    hour_start  = int(start_tuple[0])
    minute_tuple = start_tuple[2]
    minute_list = minute_tuple.partition(" ")
    minute_start = int(minute_list[0])
    am_or_pm = minute_list[2]
    ampm_flip = {"AM": "PM", "PM": "AM"}

#result
    end_minute = minute_start + minute
    if end_minute >= 60:
        hour_start += 1
        end_minute = end_minute % 60 # to make sure this end_minute does not surpass 60 => has been transferred into hour by the previous line
    end_hour = (hour_start + hour) % 12 # to make sure this end_hour won't surpass 12 => this is the 12-hour clock(not the 24-hour clock)
#Format for the minutes and hours (7:09) instead of (7:9) | (12:76) instead of (0:76)
    end_minute = "0" + str(end_minute) if end_minute <= 9 else end_minute
    end_hour = 12 if end_hour == 0 else end_hour
#days
    days = int(int(hour) / 24)
    if am_or_pm == "PM" and hour_start + (hour % 12) >= 12:
        days +=1
#Switch to AM or PM
    amount_of_am_or_pm_flips = int((hour_start + hour) / 12)
    am_or_pm = ampm_flip[am_or_pm] if amount_of_am_or_pm_flips % 2 == 1 else am_or_pm

    Time = str(end_hour) + ":" + str(end_minute) + " " + am_or_pm

#day of the week
    if week_day:
        week_day = week_day.lower()
        index = int((days_of_the_week_index[week_day]) + days) % 7
        new_day = days_of_the_week[index]
        Time +=", " + str(new_day)
    
    if days == 1:
        return Time + " " + "(next day)"
    elif days > 1:
        return Time + " (" + str(days) + " days later)"
    return Time
print(add_time("11:59 PM", "24:05"))