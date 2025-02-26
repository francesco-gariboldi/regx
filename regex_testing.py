# Description: This file is used to practice regular expressions in Python
# using the formula list from my psy-data-tool project.
import re
import formulas
import psyregex

formulas = formulas.formulas
test_formula = "ladder_score ~ healthy_life_expectancy + regional_indicator + (healthy_life_expectancy + regional_indicator | freedom_to_make_life_choices)"





# Test the function
for formula in formulas:
    random_vars_list, grouping_var = which_ranef(formula)
    print("Formula:", formula)
    print("Random variables:", random_vars_list)
    print("Grouping variable:", grouping_var)