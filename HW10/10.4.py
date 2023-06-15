import pandas as pd


def main():

    file = pd.read_csv("input.csv", index_col='ID')

    if file.empty:
        with open("output.csv", 'w') as output_file:
            print("Фамилия водителя,Объем груза", file=output_file)
            return 0

    file.loc[file["Тип операции"] == "Вывоз", "Объем груза"] *= -1
    file.drop(columns=["Тип операции"], inplace=True)
    file = file.groupby(['Фамилия водителя']).sum()

    file.sort_values(by="Объем груза", ascending=False, inplace=True)

    file.to_csv("output.csv", encoding="utf8")


if __name__ == "__main__":
    main()