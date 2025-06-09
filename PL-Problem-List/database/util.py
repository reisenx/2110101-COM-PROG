PATH = ['/00-Python-Intro/',
        '/01-Data-Type-and-Expression/',
        '/02-Basic-String-and-List/',
        '/03-Selection/',
        '/04-Repetition/',
        '/05-List-Processing/',
        '/06-Function/',
        '/07-String-Processing/',
        '/08-Basic-Dict/',
        '/09-Nested-Structure/',
        '/10-Tuple-Set-Dict/',
        '/11-NumPy/',
        '/12-Class-and-Object/',
        '/P1-Grader-01-Practice/',
        '/P2-Grader-02-Practice/',
        '/P2-Grader-03-Practice/']

FILENAME = ['00-intro',
            '01-expr',
            '02-str-list',
            '03-if',
            '04-loop',
            '05-list',
            '06-func',
            '07-str',
            '08-dict',
            '09-nested',
            '10-tsd',
            '11-numpy',
            '12-class',
            'p1-practice',
            'p2-practice',
            'p3-practice']

# Utility function to get generate file index
def welcome() -> tuple:
    print('Welcome to problem list markdown generator!')
    print('Here is the available files')
    for [i, item] in enumerate(FILENAME):
        print(f"{i} - {item}")
    
    start = int(input(f"Start index (0 - {len(FILENAME) - 1}): "))
    end = int(input(f"End index (0 - {len(FILENAME) - 1}): "))
    return (start, end + 1)

# Utility function to get difficulty text
def get_stars(level:float) -> str:
    if(int(level) == -1):
        return 'N/A'
    return '★' * int(level) + '☆' * int(2 * (level % 1.0))

# Utility function to get full path of a problem
def get_problem_path(unit:int, problem:str) -> str:
    return f"{PATH[unit]}{problem}/README.md"