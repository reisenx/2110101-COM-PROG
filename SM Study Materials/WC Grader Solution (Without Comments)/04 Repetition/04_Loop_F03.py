def grade_mcq(sol,ans):
    score = 0
    if(len(sol) != len(ans)):
        return -1

    else:
        for i in range(0,len(sol)):
            if(ans[i] == sol[i]):
                score += 1
        return score

exec(input())