def main():
    print("Find the time x minutes before and after the input time")
    current_time = input("Enter the current time (HH:MM): ")
    time_shift_str = input("Enter the time shift (in minutes): ")

    # Parse input times
    hours = int(current_time.split(":")[0])
    minutes = int(current_time.split(":")[1])
    time_shift = int(time_shift_str)

    # Convert current time to total minutes
    total_minutes = hours * 60 + minutes

    # Calculate time after the shift
    total_minutes_after = total_minutes + time_shift
    hours_after = (total_minutes_after // 60) % 24
    minutes_after = total_minutes_after % 60

    # Calculate time before the shift
    total_minutes_before = total_minutes - time_shift
    hours_before = (total_minutes_before // 60) % 24
    minutes_before = total_minutes_before % 60

    # Handle negative minutes by adjusting the hours and minutes
    if minutes_before < 0:
        minutes_before += 60
        hours_before -= 1

    # Ensure hours_before is in the range 0-23
    hours_before = hours_before % 24

    print("You have entered= {:02d}:{:02d}".format(hours, minutes))
    print("Time after {} minutes is {:02d}:{:02d}".format(time_shift, hours_after, minutes_after))
    print("Time before {} minutes is {:02d}:{:02d}".format(time_shift, hours_before, minutes_before))

if __name__ == "__main__":
    main()
