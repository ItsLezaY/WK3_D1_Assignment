# Exercise #1
# Filter out all of the empty strings from the list below

# Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

filtered_list = list(filter(lambda places: True if len(places) >= 3 else False, places))

print(filtered_list)





# Exercise #2
# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"

# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]


author.sort(key=lambda name: name.split()[-1].lower()) 

print(author)




# Exercise #3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)] 

# F = (9/5)*C + 32

def celsius_to_fahrenheit(place):
    city, celsius_temp = place
    fahrenheit_temp = (9/5)*celsius_temp + 32
    return city, fahrenheit_temp

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

converted_temps = list(map(celsius_to_fahrenheit, places))

print(converted_temps)





# Exercise #4
# Create a generator function that individually returns each movie genre back from the list

genres = ["adventure", "drama", "horror", "comedy", "action", "romance"]

def movie_genres(genres):
    for genre in genres:
        yield genre
        
generator = movie_genres(genres)

for genre in generator:
    print(genre)