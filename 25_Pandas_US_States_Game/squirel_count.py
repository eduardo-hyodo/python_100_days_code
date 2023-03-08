import pandas as pd

data = pd.read_csv("./squirel_count.csv")
# print(data.columns)
black_count = len(data.groupby("Primary Fur Color").get_group("Black"))
grey_count = len(data.groupby("Primary Fur Color").get_group("Gray"))
cinnamon_count = len(data.groupby("Primary Fur Color").get_group("Cinnamon"))

result = pd.DataFrame(
        [
            ("black",black_count),
            ("grey", grey_count),
            ("red", cinnamon_count),
        ],
            index=[0,1,2],
            columns=["Fur Color","Count"],
        )
print(result)
result.to_csv("teste.csv")
