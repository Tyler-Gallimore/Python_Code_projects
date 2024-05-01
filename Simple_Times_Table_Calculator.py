table_input = int(input("Enter the number to multiply: "))
time_table = int(input("Enter the times table amount: "))

for i in range(1, time_table + 1):
    print(f"{table_input} x {i} = {table_input * i}")