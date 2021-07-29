# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 10000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    # Read teams from file. tems = [{'team': 'Uruguay', 'rating':976}, {'team': 'Portugal', 'rating':1306},.....]
    teams = []
    with open(sys.argv[1], newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            teams.append({'team': row['team'], 'rating': int(row['rating'])})

    # Simulate N tournaments and keep track of win counts. counts = {'Urugvay': 32, 'Portugal': 76, ......}
    counts = {}
    # initial 0 winns for every team
    for t in teams:
        counts.update({t['team']: 0})

    for i in range(N):
        winner_name = simulate_tournament(teams)
        winner_count = counts.get(winner_name)
        counts.update({winner_name: winner_count + 1})

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    winners = simulate_round(teams)
    while len(winners) > 1:
        winners = simulate_round(winners)
    return winners[0]['team']


if __name__ == "__main__":
    main()
