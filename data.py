# Data around us favorites books
favorites_books = [
   {
        "title": "One Piece",
        "author":"Eiichiro Oda",
        "year": 1997,
        "is_Newer_Than_2000": False,
        "age": 27,
        "characters": ["luffy", "Zoro", "Ussop", "Chopper"]
   },
   {
        "title": "Naruto",
        "author":"Masashi Kishimoto",
        "year": 1999,
        "is_Newer_Than_2000": False,
        "age": 25,
        "characters": ["Naruto", "Saske", "Itachi", "Shino"]
   }
]
# My top 4 movies 
favourite_movies = [
    {
        "title": "Kill Bill",
        "year": 2003,
        "rating": 8.2,
        "directors": ["Quentin Tarantino"],
        "writers": ["Quentin Tarantino"],
        "actors": ["Uma Thurman", "Lucy Liu", "David Carradine"],
        "genres": ["Action", "Comedy", "Drama"],
        "description": "A pregnant assassin, code-named The Bride, goes into a coma for four years after her ex-boss Bill brutally attacks her. When she wakes up, she sets out to seek revenge on him and his associates."
    },
    {
        "title": "Matrix",
        "year": 1999,
        "rating": 8.7,
        "directors": ["Lana Wachowski", "Lilly Wachowski"],
        "writers": ["Lana Wachowski", "Lilly Wachowski"],
        "actors": ["Keanu Reeves", "Carrie-Anne Moss", "Laurence Fishburne"],
        "genres": ["Action", "Noir", "Drama"],
        "description": "Neo, a computer programmer and hacker, has always questioned the reality of the world around him. His suspicions are confirmed when Morpheus, a rebel leader, contacts him and reveals the truth to him."
    },
    {
        "title": "Madagascar",
        "year": 2005,
        "rating": 6.9,
        "directors": ["Simon J. Smith", "David Soren"],
        "writers": ["Tom McGrath", "Eric Darnell"],
        "actors": ["Chris Rock", "Chris Miller"],
        "genres": ["comedy"],
        "description": "Four spoiled animals from the New York Central Zoo escape with the unintentional help of four fugitive penguins. They subsequently find themselves in Madagascar amidst happy lemurs."
    },
    {
        "title": "Dumb and Dumber",
        "year": 1994,
        "rating": 7.3,
        "directors": ["Peter Farrelly"],
        "writers": ["Peter Farrelly"],
        "actors": ["Jim Carry"],
        "genres": ["comedy"],
        "description": "Lloyd and Harry stumble upon a suitcase full of money left behind by Mary. Unaware that the money is connected to a kidnapping case, they try to return it only to be pursued by killers and the police."
    }
]
# Best selling albums 
bestSellingAlbums = [
    {
        "artist": "Michael Jackson",
        "title": "Thriller",
        "year": 1982,
        "genres": ["pop", "post-disco", "funk", "rock"],
        "sale": 70000000,
    },
    {
        "artist": "AC/DC",
        "title": "Back in Black",
        "year": 1980,
        "genres": ["hard rock"],
        "sale": 50000000,
    },
    {
        "artist": "Whitney Houston",
        "title": "The Bodyguard",
        "year": 1992,
        "genres": ["r&b", "soul", "pop", "soundtrack"],
        "sale": 45000000,
    },
    {
        "artist": "Pink Floyd",
        "title": "The Dark Side of the Moon",
        "year": 1973,
        "genres": ["progressive rock"],
        "sale": 45000000,
    },
    {
        "artist": "Eagles",
        "title": "Their Greatest Hits (1971 - 1975)",
        "year": 1976,
        "genres": ["country rock", "soft rock", "folk rock"],
        "sale": 44000000,
    },
    {
        "artist": "Eagles",
        "title": "Hotel California",
        "year": 1976,
        "genres": ["soft rock"],
        "sale": 42000000,
    },
    {
        "artist": "Shania Twain",
        "title": "Come On Over",
        "year": 1997,
        "genres": ["country", "pop"],
        "sale": 40000000,
    },
    {
        "artist": "Fleetwood Mac",
        "title": "Rumours",
        "year": 1977,
        "genres": ["soft rock"],
        "sale": 40000000,
    },
]
# Show the average age of objects

def average_age(data_list, current_year):
    total_age = 0
    count = 0 

    for item in data_list:
        if "year" in item:
            age = current_year - item["year"]
            total_age += age
            count += 1

    return total_age / count if count > 0 else 0

current_year = 2024

print("Average year of favorite books:", average_age(favorites_books, current_year))
print("Average age of favorite movies:", average_age(favourite_movies, current_year))
print("Average age of best-selling albums:", average_age(bestSellingAlbums, current_year))    

# Show the average of different properties

def average(data_list, key):
    total_num = 0
    count = 0

    for item in data_list:
        if key in item:
            total_num += item[key]
            count += 1

    return total_num / count if count > 0 else 0

print("Average rating in fav movies:", average(favourite_movies, "rating"))
print("Average sales in best selling albums:", average(bestSellingAlbums, "sale"))   

# Show the latest and the oldest objects

def latest_or_oldest(data_list, find_latest):
    if not data_list:
        return None
    
    result = data_list[0]
    
    for item in data_list:
        if "year" in item:
            if find_latest and item["year"] > result["year"]:  
                result = item
            elif not find_latest and item["year"] < result["year"]:  
                result = item
    
    return result["title"]

print("Latest book:", latest_or_oldest(favorites_books, True))
print("Oldest movie:", latest_or_oldest(favourite_movies, False))
print("Latest album:", latest_or_oldest(bestSellingAlbums, True))

# both 

def latest_and_oldest(data_list):
    if not data_list:
        return None, None
    
    oldest = data_list[0]
    latest = data_list[0]
    
    for item in data_list:
        if "year" in item:
            if item["year"] > latest["year"]:
                latest = item
            elif item["year"] < oldest["year"]:
                oldest = item

    return latest["title"], oldest["title"]

latest_book, oldest_book = latest_and_oldest(favorites_books)
latest_movie, oldest_movie = latest_and_oldest(favourite_movies)
latest_album, oldest_album = latest_and_oldest(bestSellingAlbums)

print("Latest book:", latest_book)
print("Oldest book:", oldest_book)
print("Latest movie:", latest_movie)
print("Oldest movie:", oldest_movie)
print("Latest album:", latest_album)
print("Oldest album:", oldest_album)