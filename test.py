import pandas as pd

data = [
    {"name":"Rohit", "age":27, "City":"Navi Mumbai"},
    {"name":"Reshma", "age":29, "City":"Panvel"},
    {"name":"Mummy", "age":51, "City":"Navi Mumbai"},
    ]

df = pd.DataFrame(data)
df.to_csv("data/data.csv", index=False)