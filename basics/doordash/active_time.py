# Given a sequence of timestamps & actions of a dasher's activity within a day, we would like to know the 
# active time of the dasher. Idle time is defined as the dasher has NO delivery at hand. (That means all 
# items have been dropped off at this moment and the dasher is just waiting for another pickup) Active time equals
# total time minus idle time.

# Ref: https://leetcode.com/discuss/interview-question/1302606/DoorDash-onsite-interview-(new-question!)

# Refactor below code to apply the best practices of Python

# the input it like '10:20am', '11:00pm', '12:00am', '12:00pm'

# get active time with a list of events, one event is of type pickup or dropoff, 
# examples are: '8:30am | pickup', '9:00am | dropoff', '10:00am | pickup', '10:30am | pickup',
# '11:00am | dropoff', '11:30am | dropoff', '12:00pm | pickup', '12:30pm | dropoff' 

def get_active_time(events):
    pickup, dropoff = [], []
    for e in events:
        time, type = e.split('|')
        if type.strip() == 'pickup':
            pickup.append(get_mins(time.strip()))
        else:
            dropoff.append(get_mins(time.strip()))
    pickup.sort()
    dropoff.sort()
    total = dropoff[-1] - pickup[0]
    idle = 0
    cur = dropoff[0]
    for i in range(1, len(pickup)):
        if pickup[i] > cur:
            idle += pickup[i] - cur
        cur = dropoff[i]
    return total - idle

def get_mins(time):
    split = time.split(':')
    hour = int(split[0])
    minute = int(split[1][:-2])
    if split[1][-2:] == 'pm':
        if hour < 12:
            hour += 12
    else:
        if hour == 12:
            hour = 0
    return hour*60 + minute

if __name__ == "__main__":
    print(get_mins("10:20am"))