output_file_name = "output.csv"

amount, period, rate = map(lambda i: float(i), input().split())
amount = int(amount)
period = int(period)

rate /= 100
month_rate = rate / 12

with open(output_file_name, 'w') as file_csv:

    print("Месяц,Сумма на вкладе,Начисление", file=file_csv)
    for month in range(1, period * 12 + 1):
        month_charge = amount * month_rate
        amount *= month_rate + 1
        print(f"{month:.0f},{amount:.2f},{month_charge:.2f}", file=file_csv)