# Build a function library using Trie data structure, and define two functions: register() and search().
# If a function is marked as isVariadic=true, then the last argument can occur one or more number of times.
# These are a few function examples:
# 
"""
FuncA: [String, Integer, Integer]; isVariadic = false
FuncB: [String, Integer]; isVariadic = true
FuncC: [Integer]; isVariadic = true
FuncD: [Integer, Integer]; isVariadic = true
FuncE: [Integer, Integer, Integer]; isVariadic = false
FuncF: [String]; isVariadic = false
FuncG: [Integer]; isVariadic = false
"""

"""
findMatches({String}) -> [FuncF]
findMatches({Integer}) -> [FuncC, FuncG]
findMatches({Integer, Integer, Integer, Integer}) -> [FuncC, FuncD]
findMatches({Integer, Integer, Integer}) -> [FuncC, FuncD, FuncE]
findMatches({String, Integer, Integer, Integer}) -> [FuncB]
findMatches({String, Integer, Integer}) -> [FuncA, FuncB]
"""


class Function:
    
    def __init__(self, name, argument_types, is_variadic):
        self.name = name
        self.argument_types = argument_types
        self.is_variadic = is_variadic
    
    def __repr__(self):
        return self.name

class FunctionLibrary:
    def __init__(self):
        self.functions = defaultdict(list)
        self.variadic_functions = defaultdict(list)
        
    def register(self, functions : set[Function]) -> None:
        for function in functions:
            if not function.is_variadic:
                self.functions[tuple(function.argument_types)].append(function)
            else:
                self.variadic_functions[tuple(function.argument_types)].append(function)
    
    def find_matches(self, argument_types: list[str]) -> list[Function]:
        non_variadic = self.functions.get(tuple(argument_types), [])
        variadic = self._get_variadic_matches(argument_types)
        
        return non_variadic + variadic
    
    def _get_variadic_matches(self, argument_types):
        matches = []
        matches.extend(self.variadic_functions[tuple(argument_types)])
        i = 0
        for i in range(len(argument_types)-2, -1, -1):
            if argument_types[i] != argument_types[i+1]:
                break
            matches.extend(self.variadic_functions[tuple(argument_types[:i+1])])
        return matches

class FunctionLibraryTrie:
    def __init__(self):
        self.root = {}

    def register(self, functions : set[Function]) -> None:
        for function in functions:
            node = self.root
            for argument_type in function.argument_types:
                if argument_type not in node:
                    node[argument_type] = {}
                node = node[argument_type]
            if function.is_variadic: # Use key '*' to store the variadic functions
                node['*'] = function
            else:
                node['$'] = function

    def find_matches(self, argument_types: list[str]) -> list[Function]:
        cur = self.root
        functions = []
        functions.extend(self.find_non_variadic_matches(argument_types))
        functions.extend(self.find_variadic_matches(argument_types))
        for idx in range(len(argument_types)-2, -1, -1):
            if argument_types[idx] != argument_types[idx+1]:
                break
            functions.extend(self.find_variadic_matches(argument_types[0:idx+1]))
        return functions
    
    def find_non_variadic_matches(self, argument_types: list[str]) -> list[Function]:
        cur = self.root
        functions = []
        for type in argument_types:
            if not cur or type not in cur:
                return functions
            cur = cur[type]
        if cur and '$' in cur:
            functions.append(cur['$'])
        return functions

    
    def find_variadic_matches(self, argument_types: list[str]) -> list[Function]:
        cur = self.root
        functions = []
        for argument_type in argument_types:
            if not cur or argument_type not in cur:
                break
            cur = cur[argument_type]
        if cur:
            if '*' in cur:
                functions.append(cur['*'])
        return functions
    
