qualifiers = 0
winner_name = ""
winner_time = 0
first_runner = True

name = input("Enter athlete name (or x to finish): ")

while name.lower() != "x":

    time_str = input("Enter time (mm:ss): ")

    # Validate format
    if ":" in time_str:
        parts = time_str.split(":")

        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():

            minutes = int(parts[0])
            seconds = int(parts[1])

            if 0 <= seconds < 60:

                total_seconds = minutes * 60 + seconds

                # Check qualification
                if total_seconds <= 25 * 60:
                    qualifiers += 1

                # Find winner
                if first_runner:
                    winner_name = name
                    winner_time = total_seconds
                    first_runner = False
                elif total_seconds < winner_time:
                    winner_name = name
                    winner_time = total_seconds

            else:
                print("Invalid time ignored.")

        else:
            print("Invalid time ignored.")

    else:
        print("Invalid time ignored.")

    name = input("Enter athlete name (or x to finish): ")

# Report
if first_runner:
    print("Nobody entered.")
else:
    minutes = winner_time // 60
    seconds = winner_time % 60

    print("\n--- RACE REPORT ---")
    print(f"Winner: {winner_name} ({minutes:02d}:{seconds:02d})")
    print(f"Qualified athletes: {qualifiers}")
        
        
        

