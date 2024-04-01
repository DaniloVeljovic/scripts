# Structure: black_player_id, white_player_id, winner_id, match_date
from typing import List
import csv
from datetime import datetime as dt
import random

NUMBER_OF_RECORDS: int = 10_000

class Record:
    def __init__(self, black_player_id, white_player_id, winner_id, match_date):
        self.black_player_id = black_player_id
        self.white_player_id = white_player_id
        self.winner_id = winner_id
        self.match_date = match_date

def create_record(transaction_id: int) -> Record:
    black = random.randint(0, 1000)
    white = random.randint(0, 1000)
    return Record(
        black_player_id=black,
        white_player_id=white,
        match_date=dt.today().strftime('%Y-%m-%d'),
        winner_id=random.choice([black, white]),
    )

if __name__ == "__main__":
    transactions: List = []

    for i in range(NUMBER_OF_RECORDS):
        record: Record = create_record(i)
        transactions.append([record.black_player_id, record.white_player_id, record.winner_id, record.match_date])

    with open(f'chess-matches-{dt.today().strftime('%Y-%m-%d')}.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(['black_player_id', 'white_player_id', 'winner_id', 'match_date'])
        writer.writerows(transactions)
