# Description: This file is used to practice regular expressions in Python
# using the formula list from my psy-data-tool project.
import re
import formulas
import psy_regex

formulas = formulas.formulas
suggested_pattern = r"\((.*?)\s*\|\s*(.*?)\)"
pattern = r"\((.*?)\s*\|\s*(.*?)\)"
test_formula = "ladder_score ~ healthy_life_expectancy + regional_indicator + (healthy_life_expectancy + regional_indicator | freedom_to_make_life_choices)"
