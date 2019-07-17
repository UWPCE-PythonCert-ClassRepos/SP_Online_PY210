def alarm_clock(day, vacation):
    if day > 0 and day < 6: # weekday
        if not vacation:
            return "7:00"
        else:
            return "10:00"
    else: # weekend
        if not vacation:
            return "10:00"
        else:
            return "off"

if __name__ == "__main__":
    # run some tests
    assert alarm_clock(1, False) == "7:00"
    assert alarm_clock(2, True) == "10:00"
    assert alarm_clock(0, False) == "10:00"
    assert alarm_clock(6, True) == "off"