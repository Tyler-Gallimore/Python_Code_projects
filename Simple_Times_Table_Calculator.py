def times_table(multi_number, time_table):
    try:
        multi_number = int(multi_number)
        time_table = int(time_table)

        for i in range(1, time_table + 1):
            print(f"{multi_number} x {i} = {multi_number * i}")
    except:
        if TypeError:
            print("Input a number not a word")