# pylint: disable=missing-docstring, missing-module-docstring, invalid-name, undefined-variable
# pylint: disable=too-few-public-methods, redefined-outer-name, comparison-with-itself, misplaced-comparison-constant
# pylint: disable=line-too-long
# https://github.com/PyCQA/pylint/issues/4774

def github_issue_4774():
    # Test litearls
    # https://github.com/PyCQA/pylint/issues/4774
    good_list = []
    if not good_list:
        pass

    bad_list = []
    if bad_list == []: # [use-implicit-booleaness-not-comparison]
        pass

# Testing for empty literals
empty_tuple = ()
empty_list = []
empty_dict = {}

if empty_tuple == (): # [use-implicit-booleaness-not-comparison]
    pass

if empty_list == []: # [use-implicit-booleaness-not-comparison]
    pass

if empty_dict == {}: # [use-implicit-booleaness-not-comparison]
    pass

if () == empty_tuple: # [use-implicit-booleaness-not-comparison]
    pass

if [] == empty_list: # [use-implicit-booleaness-not-comparison]
    pass

if {} == empty_dict: # [use-implicit-booleaness-not-comparison]
    pass

def bad_tuple_return():
    a = (1, )
    return a == () # [use-implicit-booleaness-not-comparison]

def bad_list_return():
    a = [1]
    return a == [] # [use-implicit-booleaness-not-comparison]

def bad_dict_return():
    a = {1: 1}
    return a == {} # [use-implicit-booleaness-not-comparison]

assert () <= empty_tuple # [use-implicit-booleaness-not-comparison]
assert [] >= empty_list # [use-implicit-booleaness-not-comparison]
assert {} != empty_dict # [use-implicit-booleaness-not-comparison]

assert [] >= []
assert {} != {}
assert () <= ()

a = "a"
if a in {}:
    pass

class NoBool:
    def __init__(self):
        self.a = 2

class YesBool:
    def __init__(self):
        self.a = True

    def __bool__(self):
        return self.a


# Shouldn't be triggered
a = NoBool()
if [] == NoBool():
    pass

a = YesBool()
if [] == YesBool: # [use-implicit-booleaness-not-comparison]
    pass

# compound test cases

a = []
b = {}

if a == [] and b == {}: # [use-implicit-booleaness-not-comparison, use-implicit-booleaness-not-comparison]
    pass

a, b, c = 1, None, [1,2,3]

def test(a):
    print(a == {})
