import pandas as pd

squirrel_df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = squirrel_df['Primary Fur Color'].unique().tolist()[1:]
fur_color_count = []

for color in fur_color:
    count = len(squirrel_df[squirrel_df['Primary Fur Color']==color])
    print(f"{color}: {count}")
    fur_color_count.append(count)

fur_analysis = {
    'Fur Color': fur_color,
    'Count': fur_color_count
}

fur_df = pd.DataFrame(fur_analysis)
fur_df.to_csv("fur_count.csv")