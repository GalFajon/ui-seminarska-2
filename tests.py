cases = []

# case 1
cases.append({
    'p': 3,
    'n': 3,
    'start': [ ['A'], ['B'], ['C'] ],
    'end': [ ['B','C','A'], [], [] ]
})

# case 2
cases.append({
    'p': 3,
    'n': 3,
    'start': [ [], ['B','E'], ['A','C','D'] ],
    'end': [ [], ['C','D'], ['B','A','E'] ]
})

# case 3
cases.append({
    'p': 4,
    'n': 4,
    'start': [ ['A','E'], ['C','F'], ['D'], ['B'] ],
    'end': [ ['B','D'], ['A','E'], [], ['F','C'] ]
})

# case 4
cases.append({
    'p': 5,
    'n': 2,
    'start': [ ['A','B'], ['C','D'], ['E','F'], [], [] ],
    'end': [ ['B','A'], ['D','C'], ['F','E'], [], [] ]
})

# case 5
cases.append({
    'p': 5,
    'n': 4,
    'start': [ ['A','B'], ['C'], ['D'], ['E'], ['F'] ],
    'end': [ ['B','F'], ['A','D','E','C'], [], [], [] ]
})