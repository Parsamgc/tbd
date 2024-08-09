def add_user_profile_to_list(user_profiles, name, age, gender, location, interests):
    user_profile = (name, age, gender, location, interests)
    user_profiles.append(user_profile)


#List of user data to be added
users_to_add = [
    ('Alice', 25, 'F', 'NY', ['music', 'hiking', 'movies']),
    ('Bob', 27, 'M', 'TOR', ['sport', 'movie', 'game']),
    ('John', 35, 'F', 'VAN', ['cook', 'sleep', 'book'])
]

# Step 1: Create list of user profiles
user_profiles = []

# Step 2: Add user profiles to list
for user in users_to_add:
    name,age,gender,location,interests = user
    add_user_profile_to_list(user_profiles, name,age,gender,location,interests)

# Step 3 print the profiles

print("List of User profiles")
for profile in user_profiles:
    print(profile)