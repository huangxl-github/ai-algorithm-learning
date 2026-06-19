"""
W1 周六项目：猜数字游戏
运行：python guess_number.py
"""

import random


def guess_number_game(min_num: int = 1, max_num: int = 100, max_attempts: int = 7) -> None:
    """让用户在限定次数内猜中随机数。"""
    secret = random.randint(min_num, max_num)
    print(f"欢迎来到猜数字游戏！范围 {min_num}～{max_num}，你有 {max_attempts} 次机会。")

    for attempt in range(1, max_attempts + 1):
        raw = input(f"第 {attempt} 次猜测，请输入数字：").strip()
        if not raw.isdigit():
            print("请输入有效整数。")
            continue

        guess = int(raw)
        if guess < min_num or guess > max_num:
            print(f"数字应在 {min_num}～{max_num} 之间。")
            continue

        if guess == secret:
            print(f"恭喜！你用了 {attempt} 次猜中了 {secret}！")
            return
        if guess < secret:
            print("太小了，再大一点。")
        else:
            print("太大了，再小一点。")

    print(f"次数用完了，正确答案是 {secret}。")


if __name__ == "__main__":
    guess_number_game()
