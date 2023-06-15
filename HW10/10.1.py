import pandas as pd
import numpy as np


def main():
    file = pd.read_csv("input.csv")

    file.dropna(inplace=True, subset=['name'])
    file.fillna(file["score"].mean(), inplace=True)

    file.to_csv("./output.csv")


if __name__ == "__main__":
    main()