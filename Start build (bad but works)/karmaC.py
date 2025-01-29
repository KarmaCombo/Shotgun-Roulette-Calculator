import time
def main():
    print("Welcome to karma's Calculator!")
    print("loading...")
    time.sleep(3)
    
    while True:
        lives = get_integer_input("Number of live rounds: ")
        blanks = get_integer_input("Number of blank rounds: ")
        
        while lives > 0 or blanks > 0:
            total = lives + blanks
            live_percent = (lives / total) * 100 if total > 0 else 0
            blank_percent = (blanks / total) * 100 if total > 0 else 0
            
            print(f"\n{lives} Lives ({live_percent:.2f}%)")
            print(f"{blanks} Blanks ({blank_percent:.2f}%)")
            
            shot = input("What was shot (L for Live, B for Blank, R to Restart, I to Invert): ").strip().upper()
            
            if shot == "L" and lives > 0:
                lives -= 1
                print("A live round was shot!")
            elif shot == "B" and blanks > 0:
                blanks -= 1
                print("A blank round was shot!")
            elif shot == "R":
                break
            elif shot == "I":
                lives, blanks = invert(lives, blanks)
            else:
                continue
            print("loading")
            time.sleep(2)
            if lives == 0 and blanks == 0:
                print("Game Over! Restarting...")
                break

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a non-negative number.")

def invert(lives, blanks):
    print("A polarizer was used.")
    while True:
        pol = input("After polarization, what was shot? (L for Live, B for Blank, C to Cancel): ").strip().upper()
        if pol == "L" and blanks > 0:
            blanks -= 1
            break
        elif pol == "B" and lives > 0:
            lives -= 1
            break
        elif pol == "C":
            break
        else:
            print("Invalid input or no rounds left in selected category.")
    return lives, blanks

if __name__ == "__main__":
    main()