"""
Iterative
"""
from typing import Any
from stonehedge import StonehedgeState
from subtract_square_state import SubtractSquareState
from stack_sol import Stack


class IterState:
    """
    A Current State Tree with children as the states arising from making each
    move in get_possible_moves.
    """

    def __init__(self, state: Any, children=None, score=None):
        self.state = state
        self.children = children
        self.score = score


def game_is_over(current_state: Any) -> bool:
    """
    Return whether game is over.
    """
    return current_state.get_possible_moves() == []


def game_is_winner(current_state: Any, player) -> bool:
    """
    Return whether game has winner
    """
    return (current_state.get_current_player_name() != player
            and game_is_over(current_state))


def check_score(state: Any):
    """Checks score
    """
    other_player = 'p1' if state.get_current_player_name() == 'p2' else 'p2'
    if game_is_winner(state, state.get_current_player_name()):
        return 1
    elif game_is_winner(state, other_player):
        return -1
    return 0


def add_children(current: IterState):
    """
    Return list of current's children
    """
    new_items = []
    for move in current.state.get_possible_moves():
        new_state = IterState(current.state.make_move(move))
        new_items.append(new_state)
        if current.children is None:
            current.children = [new_state]
        else:
            current.children.append(new_state)
    return new_items


def set_parent_score(current: IterState):
    """
    Return current.score if any
    """
    check_if_none = False
    for child in current.children:
        if child.score is None:
            check_if_none = True
    if not check_if_none:
        score_list = []
        for child in current.children:
            score_list.append(child.score * -1)
        return max(score_list)
    return None


def iterative_outcome_tr(current_state: StonehedgeState or SubtractSquareState):
    """
    Returns minimax move iteratively
    """
    # initialize an instance of a stack
    act_up = Stack()
    current_item = IterState(current_state)
    act_up.add(current_item)
    while not act_up.is_empty():
        current = act_up.remove()
        # set the score
        if game_is_over(current.state):
            current.score = check_score(current.state)
        # make a list of the children of current item from Stack
        new_items = []
        if current.children is None:
            new_items = add_children(current)
        # if already children exist, check child's score to set score for parent
        else:
            current.score = set_parent_score(current)
        # if score not analysed put current back into stack for later
        if current.score is None:
            act_up.add(current)
        # add all children into the stack
        for item in new_items:
            act_up.add(item)
    # end of loop i.e. stack is empty; find move that corresponds to score for
    # original state and return it
    return current_item.score


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
