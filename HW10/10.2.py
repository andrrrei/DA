import pandas as pd
import numpy as np


def faren(t):
    return round((9 / 5) * t + 32)


def main():
    file = pd.read_csv("input.csv")

    file['temperature_f'] = file['temperature_c'].apply(func=faren)

    file.to_csv("./output.csv")


if __name__ == "__main__":
    main()