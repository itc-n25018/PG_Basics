import csv

movies = [
    ["トップガン", "卒業白書", "マイノリティ・リポート"],
    ["タイタニック", "レヴェナント", "インセプション"],
    ["トレーニング デイ", "ボディガード", "フライト"]
]

with open("movies.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    
    for movie_list in movies:
        writer.writerow(movie_list)

