import json
import time
import random
import difflib

def load_mobs(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def get_closest_match(user_input, mob_keys):
    return difflib.get_close_matches(user_input, mob_keys, n=1, cutoff=0.6)

def main():
    mobs = load_mobs('..//dataFiles//minecraft_mobs.json')
    random_mob = random.choice(list(mobs.keys()))
    mob = mobs[random_mob]
    mob_keys = list(mobs.keys())

    print("Guess the Minecraft mob!")
    score = 0
    hints_used = 0
    hint_index = 0
    start_time = time.time()

    while hint_index < len(mob["hints"]):
        user_input = input("Do you want a hint or make a guess? (hint/guess): ")
        if user_input.lower() == 'hint':
            print(f"Hint {hint_index + 1}: {mob['hints'][hint_index]['text']}")
            hints_used += 1
            hint_index += 1
        elif user_input.lower() == 'guess':
            guess = input("Your guess: ").lower()
            closest_match = get_closest_match(guess, mob_keys)

            if closest_match and closest_match[0] == random_mob:
                end_time = time.time()
                time_taken = end_time - start_time
                score = max(100 - (hints_used * 10 + int(time_taken)), 0)
                print(f"Correct! The mob is {random_mob}.")
                print(f"You used {hints_used} hints and took {int(time_taken)} seconds. Your score is {score}.")
                return
            else:
                print("Incorrect. Try again.")
                if closest_match:
                    print(f"Did you mean: {closest_match[0]}?")
        else:
            print("Please type 'hint' to get a hint or 'guess' to make a guess.")

    print(f"You used all hints. The mob was {random_mob}.")

if __name__ == "__main__":
    main()
