# Input number of movies
n = int(input())

# Input movie with its actors
# Movie name is in index 0 and the rest are actors
# Contains movies name to a list to make sure that the output arrange in input order
# Contains actors name to a set to prevent duplication of a name
# Contains data in a dictionary with
# > Keys: Movie name
# > Value: List of actors
movies = {}
movies_name = []
actors_name = []
for i in range(n):
    data = input().strip().split(", ")
    movies[data[0]] = data[1:]
    movies_name.append(data[0])
    for name in data[1:]:
        actors_name.append(name)
actors_name = set(actors_name)

# Reconstruct a dictionary with
# > Keys: Actors
# > Value: List of movies
actors = {}
for name in actors_name:
    movies_list = []
    for movie in movies_name:
        if(name in movies[movie]):
            movies_list.append(movie)
    actors[name] = movies_list

# Input actors that are interested
actors_output = [name.strip() for name in input().split(", ")]

# Output
# Search each name in actors_output in actors dictionary
for name in actors_output:
    if(name in actors):
        print(name, "->", ", ".join(actors[name]))
    else:
        print(name, "-> Not found")