#data
plr=[
    #players team
    [
        [
            "Jack", #name
            6, #defense treshold
            0,0, #x, y
            True, #has ball
            False #down
        ],
        [
            "Col", #name
            4, #defense treshold
            0,4, #x, y
            False, #has ball
            False #down
        ],
        [
            "Beth", #name
            7, #defense treshold
            0,8, #x, y
            False, #has ball
            False #down
        ],
        [
            "Jen", #name
            6, #defense treshold
            0,12, #x, y
            False, #has ball
            False #down
        ]
    ],
    #enemies team
    [
        [
            "Jesse", #name
            6, #defense treshold
            15,0, #x, y
            False, #has ball
            False #down
        ],
        [
            "Mel", #name
            3, #defense treshold
            15,4, #x, y
            False, #has ball
            False #down
        ],
        [
            "Sam", #name
            7, #defense treshold
            15,8, #x, y
            False, #has ball
            False #down
        ],
        [
            "Mike", #name
            6, #defense treshold
            15,12, #x, y
            False, #has ball
            False #down
        ]
    ]
]

game=[
    ["X","X","X","-","-","-","x","x","x","-","-","-","x","x","x","X","X","X",],
    ["X","X","X","-","-","-","x","x","x","-","-","-","x","x","x","X","X","X",],
    ["X","X","X","-","-","-","x","x","x","-","-","-","x","x","x","X","X","X",],
    ["X","X","X","-","-","-","x","x","x","-","-","-","x","x","x","X","X","X",],
    ["X","X","X","-","-","-","x","x","x","-","-","-","x","x","x","X","X","X",],
    ["X","X","X","-","-","-","x","x","x","-","-","-","x","x","x","X","X","X",],
    ["X","X","X","-","-","-","x","x","x","-","-","-","x","x","x","X","X","X",],
    ["X","X","X","-","-","-","x","x","x","-","-","-","x","x","x","X","X","X",],
    ["X","X","X","-","-","-","x","x","x","-","-","-","x","x","x","X","X","X",],
    ["X","X","X","-","-","-","x","x","x","-","-","-","x","x","x","X","X","X",],
    ["X","X","X","-","-","-","x","x","x","-","-","-","x","x","x","X","X","X",],
    ["X","X","X","-","-","-","x","x","x","-","-","-","x","x","x","X","X","X",],
]

for i, line in enumerate(game):
    for char in line:
        print(char,end="")
    print()