import itertools


# フラグ
# お互いに相手を第n希望に書いているペアのみマッチングさせる
MUTUAL_PREF = True
# 同性のマッチングを許さない
AVOID_SAME_GENDER_MATCHING = True
MALE_MAX = int(input("男性の人数を入力してください"))

# preferences.csvの読み込み
lines = open("preferences.csv").readlines()[1:]
all_preferences_unsorted_with_id = [list(map(int, line.split(",")[1:])) for line in lines]
all_preferences_sorted_with_id = sorted(all_preferences_unsorted_with_id, key=lambda x:x[0])

# 人数
human_max = 0
for human_id in all_preferences_sorted_with_id:
    human_max = max(human_max, human_id)

# ポイント数を保存する変数．[ペア，ポイント，相互かどうか]
preference_combination = [[x, 0, 0] for x in itertools.combinations(range(1,human_max+1),2)]

# ポイント計上
for human_id, preferences in enumerate(all_preferences_sorted_with_id):  
    preferences = preferences[1:]
    for rank, preference in enumerate(preferences):
        for comb_id, comb in enumerate(preference_combination):
            if human_id+1 in comb[0] and preference in comb[0]:
                preference_combination[comb_id][1] += len(preferences)-rank
                preference_combination[comb_id][2] += 1
    
# ポイントが高い順にソート
preference_combination.sort(key=lambda x:x[1], reverse=True)

# ポイントが高い順に確定させていく
# 確定したペアと確定した人
fixed_combination = []
fixed_human = []
# 確定
for comb in preference_combination:
    if comb[1]>0 and comb[0][0] not in fixed_human and comb[0][1] not in fixed_human:
        if (not MUTUAL_PREF) or (comb[2]==2):
            if (not AVOID_SAME_GENDER_MATCHING) or ((1 <= comb[0][0] <= MALE_MAX) and (MALE_MAX+1 <= comb[0][1] <= human_max)):
                fixed_combination.append(comb[0])
                fixed_human.append(comb[0][0])
                fixed_human.append(comb[0][1])

print(fixed_human)
print(fixed_combination)