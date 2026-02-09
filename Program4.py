def take_input_players():
    players = {}
    
    n = int(input(f"\nEnter Number of Players: "))
    
    for i in range(n):
        print(f"\nEnter player Data {i+1}: ")
        name = input("Enter Name: ")
        
        runs = []
        matches_played = int(input("Enter number of Matches Played: "))
        for j in range(matches_played):
            score = int(input(f"\nEnter the Match {j+1} Score: "))
            runs.append(score)
        
        if matches_played > 0:
            avg_runs = sum(runs) / matches_played
        else:
            avg_runs = 0
        
        players[name] = {
            "runs": runs,
            "Avg_Runs": avg_runs
        }
    
    return players


def find_score_extremes(players):
    
    if not players:
        return None
    
    min_avg_score = float('inf')
    max_avg_score = float('-inf')
    
    min_avg_players = []
    max_avg_players = []
    
    for name, data in players.items():
        avg_score = data["Avg_Runs"]
        
        
        if avg_score < min_avg_score:
            min_avg_score = avg_score
            min_avg_players = [name]
        elif avg_score == min_avg_score:
            min_avg_players.append(name)
            
            
        if avg_score > max_avg_score:
            max_avg_score = avg_score
            max_avg_players = [name]
        elif avg_score == max_avg_score:
            max_avg_players.append(name)
        
    return max_avg_score, max_avg_players, min_avg_score, min_avg_players


players = take_input_players()

result = find_score_extremes(players)

if result:
    max_avg_score, max_avg_players, min_avg_score, min_avg_players = result
    
    print("\n-----RESULT-----")
    print("Minimum Average Score:", min_avg_score)
    print("Players:", min_avg_players)
    
    print("Maximum Average Score:", max_avg_score)
    print("Players:", max_avg_players)