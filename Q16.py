def silver_medalist(scores):
    highest = float('-inf')
    second_highest = float('-inf')
    for score in scores:
        if score > highest:
            second_highest = highest
            highest = score
        elif score > second_highest and score < highest:
            second_highest = score
    return second_highest if second_highest != float('-inf') else -1