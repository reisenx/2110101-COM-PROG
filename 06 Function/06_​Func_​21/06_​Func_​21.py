# read_answers() function description
# This function convert input into a list

# 'N' is a number of students
# 'sid' is a student id
# 'ans' is a student answer

# Example Input:
# 3
# 0011 ABBBB
# 2222 AAAAB
# 3333 AAABB
# This function returns a list: 
# [["0011","ABBBB"], ["2222","AAAAB"], ["3333","AAABB"]]
def read_answers():
    N = int(input())
    answers = []
    for k in range(N):
        sid, ans = input().split()
        answers.append([sid, ans])
    return answers

# marking(answer, solution) function description
# This function can return a score

# Example Input:
# answer = "AAABB"
# solution = "AAAAA"
# This function returns an integer: 3
def marking(answer, solution):
    score = 0
    for i in range(len(answer)):
        if(answer[i] == solution[i]):
            score += 1
    return score

# grading(score) function description
# This function can grade by using score in percentage

# Example: 81
# This function return "A"
def grading(score):
    grades = [[80,"A"], [70,"B"], [60,"C"], [50,"D"]]
    for g_score,g_letter in grades:
        if score >= g_score:
            return g_letter
    return "F"

# scoring(answer, solution) function description
# This function can grade multiple students and return as a list
# [[sid1, score1, grade1], [sid2, score2, grade2], ...]

# "answers" is a list [[sid1, ans1], [sid2, ans2], ...]
# "score" is a score in percentage 

# Example Input:
# answers = [["0011","ABBBB"], ["2222","AAAAB"], ["3333","AAABB"]]
# solution = "AAAAA"
# This function returns a list:
# [["0011", 20.0, "F"], ["2222", 80.0, "A"], ["3333", 60.0, "C"]]
def scoring(answers, solution):
    scores = []
    for sid, ans in answers:
        score = marking(ans, solution) / len(solution) * 100
        grade = grading(score)
        scores.append([sid, score, grade])
    return scores

# report(scores) function description
# This function can report a score in the specified format

# "scores" is a list [[sid1, score1, grade1], [sid2, score2, grade2], ...]

# Example Input:
# scores = [["2222", 80.0, "A"], ["3333", 60.0, "C"], ["0011", 20.0, "F"]]
# This function output:
# 2222 80.0 A
# 3333 60.0 C
# 0011 20.0 F
def report(scores):
    for sid,sc,grade in scores:
        print(sid, sc, grade)

# sort(scores) function description
# This function can sort a score list and return them

# "scores" is a list [[sid1, score1, grade1], [sid2, score2, grade2], ...]

# Example Input:
# scores = [["0011", 20.0, "F"], ["2222", 80.0, "A"], ["3333", 60.0, "C"]]
# This function returns:
# [["2222", 80.0, "A"], ["3333", 60.0, "C"], ["0011", 20.0, "F"]]
def sort(scores):
    x = []
    for sid,score,grade in scores:
        x.append([score, sid, grade])
    x.sort(reverse = True)
    for i in range(len(x)):
        scores[i] = [x[i][1], x[i][0], x[i][2]]

# == The solution of this problem starts here ==
# Input a solution string
solution = str(input())

# Input a score using a read_answers() function
answers = read_answers()

# Now we've got a list in [[sid1, ans1], [sid2, ans2], ...] format
# We need to score them using scoring(answers, solution) function
scores = scoring(answers, solution)

# Now we've got a list in [[sid1, score1, grade1], [sid2, score2, grade2], ...] format
# We need to sort them using sort(scores) function
sort(scores)

# After sorting we need to output them in specified format
# Use report(scores) function to output them
report(scores)