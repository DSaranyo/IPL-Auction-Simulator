import random


players = {
    "Batsman": {
        "Virat Kohli🏏": 15, "Rohit Sharma🏏": 16, "David Warner🏏": 9, "Shubman Gill🏏": 13, "Suryakumar Yadav🏏": 11, "KL Rahul🏏": 14, "Faf du Plessis🏏": 10, "Devdutt Padikkal🏏": 8,"Ruturaj Gaikwad🏏": 9, "Shikhar Dhawan🏏": 10, "Steve Smith🏏": 10, "Jos Buttler🏏": 14, "Rajat Patidar🏏":8, "Fin Allen🏏":9, "Glenn Maxwell🏏":14, "Rishabh Pant🏏":27
    },
    "Bowler": {
        "Jasprit Bumrah": 14, "Rashid Khan": 10, "Yuzvendra Chahal": 8, "Mohammed Shami": 9,"Bhuvneshwar Kumar": 8, "Trent Boult": 9, "Kuldeep Yadav": 8, "Mohammed Siraj": 9, "Mitchell Santner":7, "Prasidh Krishna":9
    },
    "All-Rounder": {
        "Hardik Pandya": 12, "MS Dhoni": 12, "Ravindra Jadeja": 14, "Ben Stokes": 13,"Andre Russell": 12, "Shakib Al Hasan": 10, "Liam Livingstone": 11, "Cameron Green": 10
    }
}


team_name = input("🏏 Enter your team name: ").strip()


user_team = []
cpu_team = []


user_budget = 150
cpu_budget = 150 


MIN_PLAYERS = 11
MAX_PLAYERS = 15

print(f"\n🏏 Welcome to the IPL Auction Simulator, {team_name}!")
print(f"You and the CPU each have ₹{user_budget} crore.")


while len(user_team) < MAX_PLAYERS and len(cpu_team) < MAX_PLAYERS:
    print("\n📜 Available Players:")
    for category, player_list in players.items():
        print(f"\n🔹 {category}:")
        for player, price in player_list.items():
            print(f"   {player} - ₹{price} crore")

    print("\nYour Budget:", user_budget)
    print(f"Your Team ({len(user_team)}/{MAX_PLAYERS}):", user_team)

    choice = input("\nEnter the player's name to bid for (or type 'done' to finish early): ").strip()

    if choice.lower() == "done" and len(user_team) >= MIN_PLAYERS:
        break  

    selected_player = None
    for category in players:
        if choice in players[category]:
            selected_player = choice
            price = players[category][choice]
            break
    
    if not selected_player:
        print("❌ Player not found! Enter a valid name.")
        continue

    cpu_bid = random.choice([True, False]) if cpu_budget >= price else False

    if cpu_bid:
        print(f"🤖 CPU is also interested in {selected_player}!")
        while True:
            bid = input(f"Do you want to bid ₹{price+20} crore for {selected_player}? (yes/no): ").strip().lower()
            if bid == "yes":
                price += 1  
                if cpu_budget >= price + 20 and random.choice([True, False]):
                    price += 20
                    print(f"🤖 CPU raises the bid to ₹{price} crore!")
                else:
                    print(f"✅ You won the bid for {selected_player} at ₹{price} crore!")
                    user_budget -= price
                    user_team.append(selected_player)
                    break
            else:
                print(f"🤖 CPU wins {selected_player} for ₹{price} crore!")
                cpu_budget -= price
                cpu_team.append(selected_player)
                break
    else:
        if user_budget >= price:
            user_budget -= price
            user_team.append(selected_player)
            print(f"✅ You bought {selected_player} for ₹{price} crore!")
        else:
            print("❌ Not enough budget!")

    for category in players:
        if selected_player in players[category]:
            del players[category][selected_player]
            break


print("\n🏏 Auction Over!")




print(f"\n🏏 {team_name}'s Final Team ({len(user_team)} Players):", user_team)
print("\n🤖 CPU's Final Team:", cpu_team)
