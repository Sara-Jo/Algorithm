def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    dp1 = [0 for _ in range(len(sticker))]  # 첫번째 스티커를 선택한 경우
    dp2 = [0 for _ in range(len(sticker))]  # 첫번째 스티커를 선택하지 않은 경우

    dp1[0] = sticker[0] # 1개 스티커까지의 최댓값(첫번째 스티커)
    dp1[1] = sticker[0] # 2개 스티커까지의 최댓값(두번째 스티커는 선택할 수 없으므로 첫번째 스티커)

    dp2[0] = 0  # 첫번째 스티커는 선택하지 않았으므로 0
    dp2[1] = sticker[1]

    for i in range(2, len(sticker) - 1):    # 첫번째 스티커를 선택했으므로 마지막 스티커는 선택 불가능
        dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 1])

    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 1])

    val_1 = max(dp1)
    val_2 = max(dp2)

    return max(val_1, val_2)