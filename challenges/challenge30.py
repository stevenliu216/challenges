def runner_up_score(scores):
    unique_scores = set(scores)
    sorted_scores = sorted(unique_scores, reverse=True)
    return sorted_scores[1]


if __name__ == '__main__':
    num = int(input(f"Enter the number of scores: "))
    arr = [int(input(f"Enter score {score + 1}: ")) for score in range(num)]
    print(runner_up_score(arr))
