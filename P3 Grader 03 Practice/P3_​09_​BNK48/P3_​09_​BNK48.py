# Create dictionaries that use for various purposes
# 'otaku_details' contaims {Otaku:[List of [Vote,Idol]]}
# Example: {'SOMCHAI':[[10,'CHERPRANG'], [5,'NATHERINE']], 'JESSADA':[[11,'JENNIS']]}
otaku_details = {}
# 'otaku_idol' contains {Otaku:{Set of idol}}
# Example: {'SOMCHAI':{'CHERPRANG','NATHERINE'}, 'JESSADA':{'JENNIS'}}
otaku_idol = {}
# 'idol_total' contains {Idol:Total vote}
# Example: {'CHERPRANG':15, 'JENNIS':3, ...}
idol_total = {}
# 'idol_otaku' contains {Idol:{Set of otaku}}
# Example: {'CHERPRANG':{'SOMCHAI','NATTEE'}, 'JENNIS':{'JESSADA'}, ...}
idol_otaku = {}
# 'idol_kamioshi' contains {Idol:{Set of kamioshi}}
# Example: {'CHERPRANG':{'SOMCHAI'}, 'JENNIS':{'JESSADA'}, ...}
idol_kamioshi = {}
# 'unique_idol' is a set of all input idol
unique_idol = set()

# Input
# Each line contains "[Otaku] [Idol] [Score]"
# - One otaku can vote more than one idol
# - One otaku can vote same idol more than 1 time
# - Kamioshi is the favorite idol of each otaku (highest vote)
while(True):
    data = input().strip().split()
    # Output
    if(len(data) == 1):
        # Command: '1'
        # This output top 3 highest vote idol
        # The test cases guarantee that there're at least 3 idols and have different score

        # == Algorithm ==
        # 1.) Convert from dict {Idol:Total vote, ...} to list [[Total vote, Idol], ...]
        # 2.) Sort the list in descending order
        # 3.) Output top 3 names and break the loop
        if(data[0] == '1'):
            # Convert from dict to list
            idol_vote_list = []
            for idol,score in idol_total.items():
                idol_vote_list.append([score,idol])
            # Sort the list in descending order
            idol_vote_list.sort(reverse = True)
            # Output top 3 names
            top3_idol = []
            for score,idol in idol_vote_list[0:3]:
                top3_idol.append(idol)
            print(", ".join(top3_idol))
            break

        # Command: '2'
        # This output top 3 highest number of otaku voted
        # The test cases guarantee that there're at least 3 idols and have different number of otaku

        # == Algorithm ==
        # 1.) Convert from dict {Idol:{Set of otaku}, ...} to list [[Number of otaku, Idol]]
        # 2.) Sort the list in descending order
        # 3.) Output top 3 names and break the loop
        elif(data[0] == '2'):
            # Convert from dict to list
            idol_otaku_list = []
            for idol,otaku_set in idol_otaku.items():
                idol_otaku_list.append([len(otaku_set),idol])
            # Sort the list in descending order
            idol_otaku_list.sort(reverse = True)
            # Output top 3 names
            top3_idol = []
            for score, idol in idol_otaku_list[0:3]:
                top3_idol.append(idol)
            print(", ".join(top3_idol))
            break

        # Command: '3'
        # This output top 3 highest number of kamioshi
        # The test cases guarantee that there're at least 3 idols and have different number of kamioshi

        # == Data management in 'idol_kamioshi' ==
        # 1.) Sort the 'otaku_details' dictionary value in descending order
        # 2.) Find maximum score in the a list and find a list of name of idol who also have maximum score
        # 3.) Sort that name list in alphabetical order and pick the first one
        # 4.) Put that name from step and put the data in 'idol_kamioshi' (Also the idol that doesn't have kamioshi)

        # == Ranking Algorithm ==
        # 1.) Convert from dict {Idol:{Set of kamioshi}, ...} to list [[Number of kamioshi, Idol]]
        # 2.) Sort the list in descending order
        # 3.) Output top 3 names and break the loop
        elif(data[0] == '3'):
            # == Data management in 'idol_kamioshi =='
            for otaku, vote_list in otaku_details.items():
                # Sort the 'otaku_details' dictionary value in descending order
                sorted_vote_list = sorted(vote_list)[::-1]
                # Find maximum score in the a list
                max_score = sorted_vote_list[0][0]
                # Find a list of name of idol who also have maximum score
                kamioshi = []
                for score,idol in sorted_vote_list:
                    if(score == max_score):
                        kamioshi.append(idol)
                # Sort that name list in alphabetical order and pick the first one
                kamioshi.sort()
                kamioshi = kamioshi[0]
                # Put the name of kamioshi and otaku in 'idol_kamioshi'
                if(kamioshi not in idol_kamioshi):
                    idol_kamioshi[kamioshi] = {otaku}
                else:
                    idol_kamioshi[kamioshi].add(otaku)
            # Put the name of idol that have no kamioshi in 'idol_kamioshi'
            for idol in unique_idol:
                if(idol not in idol_kamioshi):
                    idol_kamioshi[idol] = set()
            
            # == Ranking ==
            # Convert from dict to list
            idol_kamioshi_list = []
            for idol,kamioshi_set in idol_kamioshi.items():
                idol_kamioshi_list.append([len(kamioshi_set),idol])
            # Sort the list in descending order
            idol_kamioshi_list.sort(reverse = True)
            # Output top 3 names
            top3_idol = []
            for score, idol in idol_kamioshi_list[0:3]:
                top3_idol.append(idol)
            print(", ".join(top3_idol))
            break
    
    # Input data
    else:
        otaku, idol, score = data[0], data[1], int(data[2])
        # Add data to 'otaku_detalis'
        # Case 1: That 'otaku' is not exist in 'otaku_details' dictionary
        if(otaku not in otaku_details):
            otaku_details[otaku] = [[score,idol]]
        # Case 2: That 'otaku' is already vote for that 'idol'
        # Example: input "SOMCHAI CHERPRANG 10" and then "SOMCHAI CHERPRANG 10"
        # This must update from {'SOMCHAI':[[10,'CHERPRANG']]} to {'SOMCHAI':[[14,'CHERPRANG']]}
        elif(idol in otaku_idol[otaku]):
            for sublist in otaku_details[otaku]:
                if(sublist[1] == idol):
                    sublist[0] += score
        # Case 3: That 'otaku' vote for a new 'idol'
        else:
            otaku_details[otaku].append([score,idol])

        # Add data to 'idol_total' 
        if(idol not in idol_total):
            idol_total[idol] = score
        else:
            idol_total[idol] += score

        # Add data to 'otaku_idol'
        if(otaku not in otaku_idol):
            otaku_idol[otaku] = {idol}
        else:
            otaku_idol[otaku].add(idol)

        # Add data to 'idol_otaku'
        if(idol not in idol_otaku):
            idol_otaku[idol] = {otaku}
        else:
            idol_otaku[idol].add(otaku)
        
        # Add data to 'unique idol'
        unique_idol.add(idol)