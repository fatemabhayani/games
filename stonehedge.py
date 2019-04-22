"""Stonehedge"""


from typing import Any
from game import Game
from game_state import GameState


class StonehedgeState(GameState):
    """
    The state of a game at a certain point in time
    p1_turn - whether it is p1's turn or not
    """
    p1_turn: bool

    def __init__(self, is_p1_turn: bool, board_size: int,
                 leylines=None, cells=None) -> None:
        """
        Initialize the game state with player and board size.
        Assume board size between 1 and 5
        """
        super().__init__(is_p1_turn)
        self.size = board_size

        if leylines is None:
            self.leylines = []
            num_leylines = [6, 9, 12, 15, 18]
            w = "@"
            for _x in range(num_leylines[board_size - 1]):
                self.leylines.append(w)
        else:
            self.leylines = leylines
        if cells is None:
            self.cells = []
            d = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                 "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]
            num_cells = [3, 7, 12, 18, 25]
            for i in range(num_cells[board_size - 1]):
                self.cells.append(d[i])
        else:
            self.cells = cells

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        if self.size == 1:
            return """      {}   {} \n     /   / \n{} - {} - {} \n     \\ / \\
  {} - {}   {} \n       \\\n        {}""". \
                format(self.leylines[0], self.leylines[1], self.leylines[2],
                       self.cells[0], self.cells[1], self.leylines[3],
                       self.cells[2], self.leylines[4], self.leylines[5])
        elif self.size == 2:
            return """           {}   {}\n          /   / 
     {} - {} - {}   {} \n        / \\ / \\ / \n  {}  - {} - {} - {} 
        \\ / \\ / \\ \n     {} - {} - {}   {} 
          \\   \\\n           {}   {}""". \
                format(self.leylines[0], self.leylines[1], self.leylines[2],
                       self.cells[0], self.cells[1], self.leylines[3],
                       self.leylines[4], self.cells[2], self.cells[3],
                       self.cells[4], self.leylines[5], self.cells[5],
                       self.cells[6], self.leylines[6], self.leylines[7],
                       self.leylines[8])
        elif self.size == 3:
            return """            {}   {}\n            /   / 
      {} - {} - {}   {}\n         / \\ / \\ /
    {} - {} - {} - {}   {}\n       / \\ / \\ / \\ /
  {} - {} - {} - {} - {}\n       \\ / \\ / \\ / \\
    {} - {} - {} - {}   {}\n         \\   \\   \\
         {}   {}   {}""".format(self.leylines[0], self.leylines[1],
                                self.leylines[2], self.cells[0],
                                self.cells[1], self.leylines[3],
                                self.leylines[4], self.cells[2], self.cells[3],
                                self.cells[4], self.leylines[5],
                                self.leylines[6], self.cells[5], self.cells[6],
                                self.cells[7], self.cells[8], self.leylines[7],
                                self.cells[9], self.cells[10], self.cells[11],
                                self.leylines[8], self.leylines[9],
                                self.leylines[10], self.leylines[11])
        elif self.size == 4:
            return """              {}   {}\n             /   /
        {} - {} - {}   {}\n           / \\ / \\ /
      {} - {} - {} - {}   {}
         / \\ / \\ / \\ /\n    {} - {} - {} - {} - {}   {}
       / \\ / \\ / \\ / \\ /\n  {} - {} - {} - {} - {} - {}   
       \\ / \\ / \\ / \\ / \\\n    {} - {} - {} - {} - {}   {}
         \\   \\   \\   \\
          {}   {}   {}   {}""".format(self.leylines[0], self.leylines[1],
                                      self.leylines[2], self.cells[0],
                                      self.cells[1], self.leylines[3],
                                      self.leylines[4], self.cells[2],
                                      self.cells[3], self.cells[4],
                                      self.leylines[5], self.leylines[6],
                                      self.cells[5], self.cells[6],
                                      self.cells[7], self.cells[8],
                                      self.leylines[7], self.leylines[8],
                                      self.cells[9], self.cells[10],
                                      self.cells[11], self.cells[12],
                                      self.cells[13], self.leylines[9],
                                      self.cells[14], self.cells[15],
                                      self.cells[16], self.cells[17],
                                      self.leylines[10], self.leylines[11],
                                      self.leylines[12], self.leylines[13],
                                      self.leylines[14])
        elif self.size == 5:
            return """              {}   {}\n             /   /
        {} - {} - {}   {}\n           / \\ / \\ /
      {} - {} - {} - {}   {}
         / \\ / \\ / \\ /\n    {} - {} - {} - {} - {}   {}
       / \\ / \\ / \\ / \\ /\n  {} - {} - {} - {} - {} - {}   {}
     / \\ / \\ / \\ / \\ / \\ /\n{} - {} - {} - {} - {} - {}   {}
     \\ / \\ / \\ / \\ / \\ / \\\n  {} - {} - {} - {} - {} - {}   {}
       \\   \\   \\   \\   \\
        {}   {}   {}   {}   {}""".format(self.leylines[0], self.leylines[1],
                                         self.leylines[2], self.cells[0],
                                         self.cells[1], self.leylines[3],
                                         self.leylines[4], self.cells[2],
                                         self.cells[3], self.cells[4],
                                         self.leylines[5], self.leylines[6],
                                         self.cells[5], self.cells[6],
                                         self.cells[7], self.cells[8],
                                         self.leylines[7], self.leylines[8],
                                         self.cells[9], self.cells[10],
                                         self.cells[11], self.cells[12],
                                         self.cells[13], self.leylines[9],
                                         self.leylines[10], self.cells[14],
                                         self.cells[15], self.cells[16],
                                         self.cells[17], self.cells[18],
                                         self.cells[19], self.leylines[11],
                                         self.cells[20], self.cells[21],
                                         self.cells[22], self.cells[23],
                                         self.cells[24], self.leylines[12],
                                         self.leylines[13], self.leylines[14],
                                         self.leylines[15], self.leylines[16],
                                         self.leylines[17])
        return ""

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        >>> StonehedgeState(True, 1).get_possible_moves()
        ['A', 'B', 'C']
        """
        moves = []
        for x in self.cells:
            if isinstance(x, str):
                moves.append(x)
        return [] if self.is_over() else moves

    def leyline_to_cell(self) -> dict:
        """
        Return leyline to cell dictionary
        >>> StonehedgeState(True, 1).leyline_to_cell() == {0: ['A'], 1: ['B', \
        'C'], 2: ['A', 'B'], 3: ['C'], 4: ['B'], 5: ['A', 'C']}
        True
        """
        if self.size == 2:
            d = {0: ["A", "C"], 1: ["B", "D", "F"], 2: ["A", "B"],
                 3: ["E", "G"], 4: ["C", "D", "E"], 5: ["F", "G"],
                 6: ["B", "E"], 7: ["C", "F"], 8: ["A", "D", "G"]}
        elif self.size == 1:
            d = {0: ["A"], 1: ["B", "C"], 2: ["A", "B"], 3: ["C"], 4: ["B"],
                 5: ["A", "C"]}
        elif self.size == 3:
            d = {0: ["A", "C", "F"], 1: ["B", "D", "G", "J"], 2: ["A", "B"],
                 3: ["E", "H", "K"], 4: ["C", "D", "E"], 5: ["L", "I"],
                 6: ["F", "G", "H", "I"], 7: ["J", "K", "L"],
                 8: ["B", "E", "I"], 9: ["F", "J"], 10: ["C", "G", "K"],
                 11: ["A", "D", "H", "L"]}
        elif self.size == 4:
            d = {0: ["A", "C", "F", "J"], 1: ["B", "D", "G", "K", "O"],
                 2: ["A", "B"], 3: ["P", "L", "H", "E"], 4: ["C", "D", "E"],
                 5: ["Q", "M", "I"], 8: ['J', "K", "L", "M", "N"],
                 6: ["F", "G", "H", "I"], 7: ["R", "N"],
                 9: ["O", "P", "Q", "R"], 11: ["O", "J"], 12: ["F", "K", "P"],
                 13: ["C", "G", "L", "Q"], 14: ["A", "D", "H", "M", "R"],
                 10: ["B", "E", "I", "N"]}
        elif self.size == 5:
            d = {0: ["A", "C", "F", "J", "O"],
                 1: ["B", "D", "G", "K", "P", "U"], 2: ["A", "B"],
                 3: ["E", "H", "L", "Q", "V"], 4: ["C", "D", "E"],
                 5: ["I", "M", "R", "W"], 6: ["F", "G", "H", "I"],
                 7: ["N", "S", "X"], 8: ["J", "K", "L", "M", "N"],
                 9: ["T", "Y"], 10: ["O", "P", "Q", "R", "S", "T"],
                 12: ["T", "M", "H", "D", "A"], 11: ["U", "V", "X", "W", "Y"],
                 13: ["U", "O"], 14: ["V", "P", "J"], 15: ["W", "Q", "K", "F"],
                 16: ["X", "R", "L", "G", "C"],
                 17: ["Y", "S", "M", "H", "D", "A"]}
        c = self.cells[:]
        ind = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
               "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]
        for v in range(len(ind)):
            for x in range(len(d)):
                for y in range(len(d[x])):
                    if d[x][y] == ind[v]:
                        d[x][y] = c[v]
        return d

    def make_move(self, move: str) -> 'StonehedgeState':
        """
        Return the GameState that results from applying move to this GameState.
        >>> StonehedgeState(True, 1).make_move("A") != StonehedgeState(False,\
        1, [1, '@', 1, '@', '@', 2], [1, 'B', 'C']).__repr__()
        True
        """
        leylines = self.leylines[:]
        cells = self.cells[:]
        c_ind = cells.index(move)
        if self.p1_turn:
            cells[c_ind] = 1
        else:
            cells[c_ind] = 2
        player = not self.p1_turn
        d = StonehedgeState(player, self.size, leylines,
                            cells).leyline_to_cell()
        for i in range(len(d)):
            if len(list(d[i])) % 2 == 0:
                num = len(list(d[i])) // 2
            else:
                num = (len(list(d[i])) + 1) // 2
            cap_1 = 0
            cap_2 = 0
            for x in list(d[i]):
                if x == 1:
                    cap_1 += 1
                elif x == 2:
                    cap_2 += 1
            if cap_1 >= num and not isinstance(leylines[i], int):
                leylines[i] = 1
            if cap_2 >= num and not isinstance(leylines[i], int):
                leylines[i] = 2
        return StonehedgeState(player, self.size, leylines, cells)

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).
        >>> result = "P1 turn: True - Board Size: 1 - Leylines: ['@', '@'," \
        "'@','@', '@','@'] - Cells: ['A', 'B', 'C']"
        >>> StonehedgeState(False, 1). __repr__() != result
        True
        """
        return "P1 turn: {} - Board Size: {} - " \
               "Leylines: {} - Cells: {}".format(self.p1_turn, self.size,
                                                 self.leylines, self.cells)

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        >>> StonehedgeState(False, 1, [1, "@", 1, "@", "@", 1], \
        [1, "B", "C"]).rough_outcome()
        -1
        """
        moves = self.get_possible_moves()[:]
        resulting_states = []
        if self.is_over():
            return self.LOSE
        for move in moves:
            resulting_states.append(self.make_move(move))
            if self.make_move(move).is_over():
                return self.WIN
        for item in resulting_states:
            moves_step = item.get_possible_moves()[:]
            for move in moves_step:
                if item.make_move(move).is_over():
                    return self.LOSE
        return self.DRAW

    def is_over(self) -> bool:
        """
        Return whether or not this game is over at state.
        >>> StonehedgeState(False, 1).is_over()
        False
        """
        capture = len(self.leylines)
        capture = capture + 1 if capture % 2 != 0 else capture
        num_1 = 0
        num_2 = 0
        for x in self.leylines:
            if x == 1:
                num_1 += 1
            elif x == 2:
                num_2 += 1
        return ((2 * num_1) >= capture) or ((2 * num_2) >= capture)


class StonehedgeGame(Game):
    """
    Abstract class for a game to be played with two players.
    """

    def __init__(self, is_p1_turn: bool, current_state=None) -> None:
        """
        Initialize the game
        """
        board_size = int(input("Enter the side length of the board: "))
        if current_state is None:
            self.current_state = StonehedgeState(is_p1_turn, board_size)

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.
        """
        instructions = "Players take turns claiming cells. " \
                       "When a player captures atleast half of the" \
                       " cells in a leyline, then the player captures that " \
                       "leyline."
        return instructions

    def is_over(self, state: StonehedgeState) -> bool:
        """
        Return whether or not this game is over at state.
        """
        capture = len(state.leylines)
        capture = capture + 1 if capture % 2 != 0 else capture
        capture //= 2
        num_1 = 0
        num_2 = 0
        for x in state.leylines:
            if x == 1:
                num_1 += 1
            elif x == 2:
                num_2 += 1
        return num_1 >= capture or num_2 >= capture

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string: str) -> Any:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.
        """
        return string


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
