def html_str_to_board(board_str: str):
    return_board = []
    temp_list = []
    for c in board_str:
        temp_list.append(int(c))
        if len(temp_list) == 3:
            return_board.append(temp_list)
            temp_list = []
    return return_board

