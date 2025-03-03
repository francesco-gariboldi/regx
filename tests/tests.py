# Description: This file is used to test regular expressions in Python
from scripts import formulas
from scripts import lme4_formula_filters as lff

formulas = formulas.formulas

# Test the function
for formula in formulas:
    random_vars_list, grouping_var = lff.which_ranef(formula)
    print("Formula:", formula)
    print("Random variables:", random_vars_list)
    print("Grouping variable:", grouping_var)