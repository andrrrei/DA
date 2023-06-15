import pandas as pd


def main():
    file = pd.read_csv("input.csv", index_col="ID")

    if file.empty:
        with open("output.csv", 'w') as output_file:
            print("Номер борта,Уникальных маршрутов", file=output_file)
            return 0

    file["Уникальных маршрутов"] = file.apply(lambda row: row["Город отправления"] + row["Город прибытия"], axis=1)

    file = file.groupby(['Номер борта'])["Уникальных маршрутов"].nunique()

    res = pd.DataFrame({"Уникальных маршрутов": file.values}, index=list(file.index))
    res.index.name = "Номер борта"
    res.sort_values(ascending=[False, True], inplace=True, by=["Уникальных маршрутов", "Номер борта"])
    res.to_csv("./output.csv")


if __name__ == "__main__":
    main()