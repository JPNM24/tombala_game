import random
import time

NUMBER_RANGE = list(range(1, 51))
MIN_PLAYERS = 2
MAX_PLAYERS = 10
WIN_CONDITION = 5

def main():
    print("TERMINAL TOMBOLA -- CORE ALGORITHM")
    print("====================================")

    players = []
    result_numbers = set()
    winner = None

    while True:
        try:
            num_input = input(f"Enter number of players ({MIN_PLAYERS}-{MAX_PLAYERS}): ")
            number_of_players = int(num_input)
            if MIN_PLAYERS <= number_of_players <= MAX_PLAYERS:
                break
            print(f"Please enter a number between {MIN_PLAYERS} and {MAX_PLAYERS}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print(f"\nSetting up for {number_of_players} players...")

    for i in range(number_of_players):
        player_name = input(f"Enter name for Player {i+1} (default P{i+1}): ").strip()
        if not player_name:
            player_name = f"P{i+1}"
        
        ticket_size = random.choice([5, 6])
        
        ticket_numbers = sorted(random.sample(NUMBER_RANGE, ticket_size))
        
        players.append({
            "id": player_name,
            "ticket": ticket_numbers,
            "matched_count": 0
        })

    print("\nGenerating Tickets:")
    for player in players:
        print(f"  {player['id']} (Size {len(player['ticket'])}): {player['ticket']}")
    
    print("\nGame Starting! Drawing numbers...")
    time.sleep(1)

    draw_pile = list(NUMBER_RANGE)
    random.shuffle(draw_pile)

    while winner is None and draw_pile:
        drawn_number = draw_pile.pop(0)
        result_numbers.add(drawn_number)
        
        print(f"Host drew: {drawn_number}")
        
        round_winners = []
        
        for player in players:
            if drawn_number in player['ticket']:
                player['matched_count'] += 1
            
            if player['matched_count'] >= WIN_CONDITION:
                round_winners.append(player)
        
        if round_winners:
            winner = round_winners[0]
            print("\nWE HAVE A WINNER!")
            print(f"Winner is: {winner['id']}")
            print(f"Winning ticket: {winner['ticket']}")
            matched_nums = set(winner['ticket']).intersection(result_numbers)
            print(f"Matched numbers: {sorted(list(matched_nums))}")
            print(f"Total numbers drawn: {len(result_numbers)}")
            break

    if winner is None:
        print("\nAll numbers drawn. No winner?")

if __name__ == "__main__":
    main()
