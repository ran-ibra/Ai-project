import chess

# Create a new chess board
board = chess.Board()

# Main game loop
while not board.is_game_over():
    # Print the current board state
    print(board)
    
    # Prompt the current player for a move
    player_color = "White" if board.turn else "Black"
    
    # Prompt the current player for a move
    move = input(f"{player_color} player, enter your move (in algebraic notation): ")    
    # Try to make the move on the board
    try:
        board.push_san(move)
    except ValueError:
        print("Invalid move! Try again.")
        continue
    
    # Check if the game is over
    if board.is_checkmate():
        print("Checkmate!")
    elif board.is_stalemate():
        print("Stalemate!")
    elif board.is_insufficient_material():
        print("Insufficient material!")
    elif board.is_seventyfive_moves():
        print("Draw due to 75-move rule!")
    elif board.is_fivefold_repetition():
        print("Draw due to fivefold repetition!")
    elif board.is_variant_draw():
        print("Draw due to variant-specific rule!")
    
# Print the final board state
print(board)
