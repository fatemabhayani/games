"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
from minimax_iterative import iterative_outcome_tr


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2 # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def _game_is_winner(current_state: Any, player) -> bool:
    """
    Return whether game has winner
    """
    return (current_state.get_current_player_name() != player
            and _game_is_over(current_state))


def _game_is_over(current_state: Any) -> bool:
    """
    Return whether game is over.
    """
    return current_state.get_possible_moves() == []


def minimax_recursive(game: Any) -> Any:
    """
    Return a move for game recursively.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2

    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        guessed_score = _recursive_outcome(new_state) * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best recursive_outcome
    return best_move


def _recursive_outcome(current_state: Any, depth=None) -> int:
    """
    Return similar rough outcome
    """
    player = current_state.get_current_player_name()
    other = 'p2' if current_state.get_current_player_name() == 'p1' else 'p1'
    if depth is None:
        depth = 0
    if _game_is_over(current_state):
        if not (_game_is_winner(current_state, player)
                or _game_is_winner(current_state, other)):
            return 0
        return 1 if depth % 2 == 1 else -1
    state = current_state
    outcomes = []
    moves = state.get_possible_moves()
    for move in moves:
        outcomes.append(_recursive_outcome(state.make_move(move), depth + 1))
    if depth % 2 == 1:
        return min(outcomes)
    return max(outcomes)


def minimax_iterative(game: Any) -> Any:
    """
    Return a move using the minimax algorithm iteratively.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2

    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)
        guessed_score = iterative_outcome_tr(new_state) * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move
    # Return the move that resulted in the best recursive_outcome
    return best_move


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
