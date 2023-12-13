from function_library import FunctionLibraryTrie, Function
def test_FunctionLibraryTrie():
    # Create a FunctionLibraryTrie instance
    trie = FunctionLibraryTrie()

    # Create some Function objects
    funcA = Function("FuncA", ["String", "Integer", "Integer"], False)
    funcB = Function("FuncB", ["String", "Integer"], True)
    funcC = Function("FuncC", ["Integer"], True)
    funcD = Function("FuncD", ["Integer", "Integer"], True)
    funcE = Function("FuncE", ["Integer", "Integer", "Integer"], False)
    funcF = Function("FuncF", ["String"], False)
    funcG = Function("FuncG", ["Integer"], False)

    # Register the functions in the trie
    trie.register({funcA, funcB, funcC, funcD, funcE, funcF, funcG})

    # Test case 1: Find matches for argument types ["String"]
    matches1 = trie.find_matches(["String"])
    assert len(matches1) == 1
    assert matches1[0].name == "FuncF"

    # Test case 2: Find matches for argument types ["Integer"]
    matches2 = trie.find_matches(["Integer"])
    assert len(matches2) == 2
    assert matches2[0].name == "FuncC" or matches2[0].name == "FuncG"
    assert matches2[1].name == "FuncC" or matches2[1].name == "FuncG"

    # Test case 3: Find matches for argument types ["Integer", "Integer", "Integer", "Integer"]
    matches3 = trie.find_matches(["Integer", "Integer", "Integer", "Integer"])
    assert len(matches3) == 2
    # Fix this assert statement the order of the matches is not guaranteed
    assert matches3[0].name == "FuncC" or matches3[0].name == "FuncD"
    assert matches3[1].name == "FuncC" or matches3[1].name == "FuncD"

    # Test case 4: Find matches for argument types ["Integer", "Integer", "Integer"]
    matches4 = trie.find_matches(["Integer", "Integer", "Integer"])
    assert len(matches4) == 3
    # Fix this assert statement the order of the matches is not guaranteed
    assert matches4[0].name == "FuncC" or matches4[0].name == "FuncD" or matches4[0].name == "FuncE"
    assert matches4[1].name == "FuncC" or matches4[1].name == "FuncD" or matches4[1].name == "FuncE"
    assert matches4[2].name == "FuncC" or matches4[2].name == "FuncD" or matches4[2].name == "FuncE"

    # Test case 5: Find matches for argument types ["String", "Integer", "Integer", "Integer"]
    matches5 = trie.find_matches(["String", "Integer", "Integer", "Integer"])
    assert len(matches5) == 1
    assert matches5[0].name == "FuncB"

    # Test case 6: Find matches for argument types ["String", "Integer", "Integer"]
    matches6 = trie.find_matches(["String", "Integer", "Integer"])
    assert len(matches6) == 2
    # Fix this assert statement the order of the matches is not guaranteed
    assert matches6[0].name == "FuncA" or matches6[0].name == "FuncB"
    assert matches6[1].name == "FuncA" or matches6[1].name == "FuncB"


    print("All test cases pass")

# Run the test cases
test_FunctionLibraryTrie()