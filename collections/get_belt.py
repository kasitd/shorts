from collections import OrderedDict

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()


def get_belt(user_score, scores=scores, belts=belts):
    belt_dict = OrderedDict(zip(scores,belts))

    for i in range(len(belt_dict)):
        less = (list(belt_dict.items())[0][0])
        min_value = (list(belt_dict.items())[i][0])
        max_value = (list(belt_dict.items())[i+1][0])
        more = (list(belt_dict.items())[(len(belt_dict)-1)][0])
        if user_score< less:
            return None
        if user_score>=min_value and user_score<max_value:
            return list(belt_dict.items())[i][1]
        if user_score >= more:
            return list(belt_dict.items())[(len(belt_dict)-1)][1]