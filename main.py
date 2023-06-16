import chess
import chess.svg

def generate_board_image(moves):
    board = chess.Board()
    
    for move in moves:
        board.push_san(move)
    
    svg = chess.svg.board(board=board)
    
    with open('board.svg', 'w') as file:
        file.write(svg)
    
    print("SVG image generated: board.svg")

# Example usage of moves
moves = ["e4", "e5", "Nf3"]
generate_board_image(moves)
