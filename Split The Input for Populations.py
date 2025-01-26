# Split The Input
"""
Write a loop that prints each country's population in country_pop.

Sample output with input:
'China:1365830000,India:1247220000,United States:318463000,Indonesia:252164800':

Output:
China has 1365830000 people.
India has 1247220000 people.
United States has 318463000 people.
Indonesia has 252164800 people.
"""

# Get user input
user_input = input("Enter country-population pairs (e.g., 'China:1365830000,India:1247220000'): ")

# Split the input into entries
entries = user_input.split(',')

# Initialize the country_pop dictionary
country_pop = {}

# Process each country-population pair
for pair in entries:
    split_pair = pair.split(':')
    if len(split_pair) == 2:  # Ensure the pair contains both country and population
        country = split_pair[0].strip()  # Remove extra spaces from the country name
        population = split_pair[1].strip()  # Remove extra spaces from the population
        country_pop[country] = population

# Print the population information for each country
for country, population in country_pop.items():
    print(f'{country} has {population} people.')
