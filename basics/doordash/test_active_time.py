from active_time import get_mins, get_active_time

def test_get_mins():
    # Test case 1: time in the morning
    assert get_mins("09:30am") == 570

    # Test case 2: time in the afternoon
    assert get_mins("03:45pm") == 945

    # Test case 3: time at midnight
    assert get_mins("12:00am") == 0

    # Test case 4: time at noon
    assert get_mins("12:30pm") == 750

    # Test case 5: time with leading zeros
    assert get_mins("08:05am") == 485

    # Test case 6: time with single-digit hour
    assert get_mins("3:15pm") == 915

    # Test case 7: time with single-digit minute
    assert get_mins("11:05am") == 665

    # Test case 8: time in the afternoon
    assert get_mins("12:05am") == 5

    print("All test cases pass")


def test_get_active_time():
    # Test case 1: Single pickup and dropoff event
    events = ["09:30am|pickup", "10:00am|dropoff"]
    assert get_active_time(events) == 30

    # Test case 2: Multiple pickup and dropoff events
    events = ["09:30am|pickup", "10:00am|dropoff", "10:15am|pickup", "11:00am|dropoff"]
    assert get_active_time(events) == 75

    print("All test cases pass")

def strTest(time):
    print(time[::-1]) # reverse string

#test_get_active_time()

strTest("10:20am")
strTest("11:00pm")