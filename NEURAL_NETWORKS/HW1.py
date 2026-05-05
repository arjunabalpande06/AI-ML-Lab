# # Stored contacts using dictionary
# contacts = {
#     "9876543210": "Ravi",
#     "9123456789": "Neha"
# }

# # Take phone number input
# number = input("Enter phone number: ")

# # Check if number exists
# if number in contacts:
#     print("Contact Name:", contacts[number])
# else:
#     print("Contact Not Found")



# Stored user preferences
user_preferences = {
    "A": "Action",
    "B": "Comedy",
    "C": "Action"
}

# Sample movies watched by users
user_movies = {
    "A": ["Avengers", "John Wick"],
    "B": ["Hangover", "Superbad"],
    "C": ["Mad Max", "Mission Impossible"]
}

# Take input from user
favorite_genre = input("Enter your favorite genre: ")

# Find users with same preference
recommended_movies = []

for user, genre in user_preferences.items():
    if genre.lower() == favorite_genre.lower():
        recommended_movies.extend(user_movies[user])

# Show recommendation
if recommended_movies:
    print("Recommended Movies:")
    for movie in recommended_movies:
        print("-", movie)
else:
    print("No recommendations found for this genre.")


