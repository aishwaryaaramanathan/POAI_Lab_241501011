def unify(x, y, theta={}):
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x.islower():
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.islower():
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

def resolution(facts, rules, query):
    if query in facts:
        return True
    for rule in rules:
        premise, conclusion = rule
        theta = unify(conclusion, query, {})
        if theta is not None:
            new_query = substitute(premise, theta)
            if resolution(facts, rules, new_query):
                return True
    return False

def substitute(expr, theta):
    return [theta.get(term, term) for term in expr]

# Facts
facts = [
    ["Human", "John"]
]

# Rules (premise => conclusion)
rules = [
    (["Human", "x"], ["Mortal", "x"])
]

# Query
query = ["Mortal", "John"]

# Run resolution
if resolution(facts, rules, query):
    print("Query is resolved: John is Mortal")
else:
    print("Query could not be resolved")
