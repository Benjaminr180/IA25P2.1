def is_valid(assignment, var, value, constraints):
    return all(value != assignment.get(neighbor) for neighbor in constraints[var])

def backtracking(variables, domains, constraints, assignment={}):
    if len(assignment) == len(variables):
        return assignment
    
    var = next(v for v in variables if v not in assignment)
    for value in domains[var]:
        if is_valid(assignment, var, value, constraints):
            assignment[var] = value
            result = backtracking(variables, domains, constraints, assignment)
            if result:
                return result
            assignment.pop(var)
    
    return None

# Ejemplo de uso
variables = ['A', 'B', 'C']
domains = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}
constraints = {'A': ['B'], 'B': ['A', 'C'], 'C': ['B']}
print(backtracking(variables, domains, constraints))