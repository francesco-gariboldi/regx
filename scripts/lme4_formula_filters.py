# Miscellaneous functions to filter out models based on their lme4 R formulas
import re
import psyregex

# Tested and working
def split_sides(formula):
    '''Split a single R formula string into response variables (list) and
    predictors (list).'''
    # Split the formula into the two main terms around the "~" symbol
    try:
        pattern = r"~"
        match = re.split(pattern, formula)
        if match:
            # Split left-hand side (lhs) and right-hand side (rhs) of the formula
            lhs, rhs = match[0], match[1]
            
            return lhs, rhs
        
        else:
            return "Splitting the formula in lhs and rhs\
                    failed."
    except Exception as e:
        return f"Error: {e}"

# Non-tested
def split_predictors(predictors):
    '''Split the predictors of a formula into a list of individual predictors.'''
    try:
        pattern = r"\+"
        match = re.split(pattern, predictors)
        if match:
            return match
        else:
            return "Splitting the predictors failed."
    except Exception as e:
        return f"Error: {e}"

# non-tested
def split_response(response):
    '''Split the response variables of a formula into a list of individual
    response variables.'''
    try:
        pattern = r"\+"
        match = re.split(pattern, response)
        if match:
            return match
        else:
            return "Splitting the response variables failed."
    except Exception as e:
        return f"Error: {e}"


# Tested and working
# Find the random effects in an R lmer4 styled mixed effect formula
def which_ranef(formula):
    '''Find the random effects in an R formula.'''
    pattern = psyregex.find_ranef
    
    # Default values in case there's no match or an error
    random_vars_list = None
    grouping_var = None
    
    try:
        match = re.search(pattern, formula)
        if match:
            random_vars_part = match.group(1)  # e.g., "0/1 + var1 + var2"
            grouping_var = match.group(2)     # e.g., "grouping_var"

            random_vars_list = [
                tok.strip() for tok in random_vars_part.split('+')
            ]
        else:
            print("No match found")
    except Exception as e:
        print("Error:", e)

    return random_vars_list, grouping_var


class RlmsFilter:
    '''A class of regex functions to find matches in the models formulas list
    for R style linear models formulas.

    Crtiteria for filtering out models:
    - number of unique observations in the non-grouping variables involved in
    the formula/number of unique levels in the grouping variable > threshold.


    Attributes:
        
        pattern (str): A regular expression pattern to match random-effects
        terms.

        df (pd.DataFrame): The dataset to compute the threshold for the ratio
        between the number of different observations in the variables
        (predictors) involved in a certain formula and the unique levels in
        the grouping variable.
    '''
    def __init__(self, pattern, df, threshold, accepted_formulas=[]):
        self.pattern = pattern
        self.df = df
        self.threshold = threshold
        self.accepted_formulas = accepted_formulas

    def find_matches(self, formulas):
        for formula in formulas:
            match_group = re.search(self.pattern, formula)
            if match_group:
                for match in match_group:
                    print(match) 
            else:
                print("No matches found.")
        
        # Count unique levels
        unique_levels = df[grouping_var].nunique()
    
    def build_accepted_formulas_list(self, formulas):
        pass