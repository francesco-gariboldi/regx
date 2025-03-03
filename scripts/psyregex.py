# Regular expression patterns (for raw strings) for miscellaneous tasks

# In a general lmer4 formula structure as:
# response_variable ~ fixed_effects + (random_structure | grouping_variable)

# Matches the random and grouping variables in the formula
find_ranef = r'\(\s*((?:0/1|\w+)(?:\s*\+\s*(?:0/1|\w+))*)\s*\|\s*(\w+)\s*\)$'
