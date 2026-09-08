import pandas as pd 
data = {
    "name" : ["Kimi","lewis","george"],
    "points" : [225,185,185]
}
df = pd.DataFrame(data,index=[["1st","2nd","3rd"]])
df["wins"] = [5,1,2]
new_driver = pd.DataFrame([{"name" : "Lando","points" : 151,"wins" : 2}],index=["4th"])
df = pd.concat([df,new_driver])
print(df)

