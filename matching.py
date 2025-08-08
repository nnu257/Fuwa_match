import itertools

# preferences.csvの読み込み
with open("preferences.csv") as f:
    lines = f.readlines()
    all_preferences_unsorted_with_id = [list(map(int, line.split(","))) for line in lines]
    all_preferences_sorted_with_id = sorted(all_preferences_unsorted_with_id, key=lambda x:x[0])
    all_preferences_sorted = [x[1:] for x in all_preferences_sorted_with_id]

# 人数
human_max = len(all_preferences_sorted)

# ポイント数を保存する変数
preference_combination = [[x, 0] for x in itertools.combinations(range(1,human_max+1),2)]

# ポイント計上
for human_id, preferences in enumerate(all_preferences_sorted):    
    for rank, preference in enumerate(preferences):
        for comb_id, comb in enumerate(preference_combination):
            if human_id+1 in comb[0] and preference in comb[0]:
                preference_combination[comb_id][1] += len(preferences)-rank
    
# ポイントが高い順にソート
preference_combination.sort(key=lambda x:x[1], reverse=True)

# ポイントが高い順に確定させていく
# 確定したペアと確定した人
fixed_combination = []
fixed_human = []
# 確定
for comb in preference_combination:
    if comb[1]>0 and comb[0][0] not in fixed_human and comb[0][1] not in fixed_human:
        fixed_combination.append(comb[0])
        fixed_human.append(comb[0][0])
        fixed_human.append(comb[0][1])

print(fixed_human)
print(fixed_combination)