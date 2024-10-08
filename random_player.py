import random


class RandomPlayer:
    def __init__(self, turn: int) -> None:
        self.turn = turn

    def get_legal_moves(self, board) -> list:
        return_list = []
        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if item == 0:
                    return_list.append(i * 3 + j + 1)
        return return_list

    def generate_move(self, board) -> int:
        legal_moves = self.get_legal_moves(board)
        return random.choice(legal_moves)


if __name__ == "__main__":
    p = RandomPlayer(0)
    legal_moves = p.get_legal_moves([[1, 2, 0], [0, 0, 0], [1, 2, 0]])
    print(p.generate_move([[1, 2, 0], [0, 0, 0], [1, 2, 0]]))
    print(legal_moves)