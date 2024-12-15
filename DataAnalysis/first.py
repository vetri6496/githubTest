import csv


# def cal_rating(data, industry= None):

#     ratings = []

#     for i in data:
#         if i[3] != 'NULL' and (not industry or i[1] == industry):
#             ratings.append(float(i[3]))
    

#     MinRating = min(ratings)
#     MaxRating = max(ratings)
#     AvgRating = sum(ratings)/len(ratings)


#     return MinRating, MaxRating, AvgRating



# with open ("DataAnalysis\Intro_to_pandas_resources\movies.csv") as f:
#     data = list(csv.reader(f))

#     header = data[0]
#     file = data[1:]

#     minA, MaxA, avgA = cal_rating(file)
#     minB, MaxB, avgB = cal_rating(file, industry='Bollywood')
#     minC, MaxC, avgC = cal_rating(file, industry='Hollywood')

#     print(f"All file data min = {minA}, Max = {MaxA}, Avg={avgA}")
#     print(f"All Bolywood data min = {minB}, Max = {MaxB}, Avg={avgB}")
#     print(f"All Hoolywood data min = {minC}, Max = {MaxC}, Avg={avgC}")



#Pandas


import pandas as pd

df = pd.read_csv("DataAnalysis\Intro_to_pandas_resources\movies.csv")

print(df)

print(f"\n\n\n\nThe header: \n{df.head(1)}")

print(f"\n\n\n{df.imdb_rating}")