import os
import time

ROUNDS = 5
ROADS = ["N", "C", "S"]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_lane(player, round_num):
    while True:
        lane = input(f"[Round {round_num}] {player} choose lane (N/C/S): ").upper()
        if lane in ROADS:
            return lane
        print("  -> Invalid. Type N, C, or S.")

def play_game():
    smuggler_score = 0
    customs_score = 0

    smuggler_inputs = []
    customs_inputs = []

    for r in range(1, ROUNDS + 1):
        clear()
        print(f"🚛 SMUGGLER vs CUSTOMS – ROUND {r}/{ROUNDS}\n")
        print("Lanes: N = North, C = Center, S = South\n")
        print(f"Score so far: Smuggler {smuggler_score} – Customs {customs_score}\n")

        s_lane = get_lane("Smuggler", r)
        c_lane = get_lane("Customs ", r)

        smuggler_inputs.append(s_lane)
        customs_inputs.append(c_lane)

        clear()
        print(f"🚛 SMUGGLER vs CUSTOMS – ROUND {r}/{ROUNDS}\n")
        print(f"Smuggler chose: {s_lane}")
        print(f"Customs  chose: {c_lane}\n")

        if s_lane == c_lane:
            print("❌ Smuggler CAUGHT this round! (+1 Customs)")
            customs_score += 1
        else:
            print("✅ Smuggler ESCAPED this round! (+1 Smuggler)")
            smuggler_score += 1

        print(f"\nScore now: Smuggler {smuggler_score} – Customs {customs_score}")
        time.sleep(2)

    clear()
    print("========== FINAL RESULT ==========\n")
    print(f"Smuggler escapes: {smuggler_score}")
    print(f"Customs catches:  {customs_score}\n")

    if smuggler_score > customs_score:
        print("🏆 Overall winner: Smuggler")
    elif customs_score > smuggler_score:
        print("🏆 Overall winner: Customs")
    else:
        print("🤝 Match tied")

    print("\n========== INPUT SUMMARY ==========\n")
    for i in range(ROUNDS):
        print(f"Round {i+1}: Smuggler → {smuggler_inputs[i]},  Customs → {customs_inputs[i]}")

    return smuggler_score, customs_score


def print_game_matrix():
    print("\n========== GAME MATRIX (1 ROUND) ==========\n")
    print("Payoffs shown as (Smuggler, Customs):\n")
    print("""
                 Customs
              N          C          S
Smuggler
   N     [-1, 1]    [ 1,-1]    [ 1,-1]
   C     [ 1,-1]    [-1, 1]    [ 1,-1]
   S     [ 1,-1]    [ 1,-1]    [-1, 1]
""")
    print("Diagonal = same lane → Customs wins")
    print("Off-diagonal = different lanes → Smuggler wins\n")


if __name__ == "__main__":
    play_game()
    print_game_matrix()
