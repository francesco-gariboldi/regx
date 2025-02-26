# Miscellanous regular expressions for psychology and data analysis.

# In a general formula structure as:
# response_variable ~ fixed_effects + (random_structure | grouping_variable)
# Find the random intercepts based on the pattern:

find_ranef = r'\(\s*((?:0/1|\w+)(?:\s*\+\s*(?:0/1|\w+))*)\s*\|\s*(\w+)\s*\)$'

