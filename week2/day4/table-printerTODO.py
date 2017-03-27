# Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# The frist columns should be automatically as wide as the longest key

ingredients = [
	{ 'vodka': 1, 'needs_cooling': True }
	{ 'coffee_liqueur': 0, 'needs_cooling': True }
	{ 'fresh_cream': 1, 'needs_cooling': True }
	{ 'captain_morgan_rum': 2, 'needs_cooling': True }
	{ 'mint_leaves': 0, 'needs_cooling': False }
	{ 'sugar': 100, 'needs_cooling': False }
	{ 'lime juice': 10, 'needs_cooling': True }
	{ 'soda': 100, 'needs_cooling': True }
]
