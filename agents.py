import random
import math

BOT_NAME = "WHEEZY"


class RandomAgent:
    """Agent that picks a random available move.  You should be able to beat it."""

    def get_move(self, state, depth=None):
        return random.choice(state.successors())


class HumanAgent:
    """Prompts user to supply a valid move."""

    def get_move(self, state, depth=None):
        move__state = dict(state.successors())
        prompt = "Kindly enter your move {}: ".format(sorted(move__state.keys()))
        move = None
        while move not in move__state:
            try:
                move = int(input(prompt))
            except ValueError:
                continue
        return move, move__state[move]


class MinimaxAgent:
    """Artificially intelligent agent that uses minimax to optimally select the best move."""

    def get_move(self, state, depth=None):
        """Select the best available move, based on minimax value."""
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None

        for move, state in state.successors():
            util = self.minimax(state, depth)
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util, best_move, best_state = util, move, state
        return best_move, best_state

    def minimax(self, state, depth):
        """Determine the minimax utility value of the given state.

        Args:
            state: a connect383.GameState object representing the current board
            depth: for this agent, the depth argument should be ignored!

        Returns: the exact minimax utility value of the state
        """

        if state.is_full():
            return state.score()

        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        for move, state in state.successors():
            util = self.minimax(state, None)
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util = util
        return best_util


class HeuristicAgent(MinimaxAgent):
    """Artificially intelligent agent that uses depth-limited minimax to select the best move."""

    def minimax(self, state, depth):
        return self.minimax_depth(state, depth)

    def minimax_depth(self, state, depth):
        """Determine the heuristically estimated minimax utility value of the given state.

        Args:
            state: a connect383.GameState object representing the current board
            depth: the maximum depth of the game tree that minimax should traverse before
                estimating the utility using the evaluation() function.  If depth is 0, no
                traversal is performed, and minimax returns the results of a call to evaluation().
                If depth is None, the entire game tree is traversed.

        Returns: the minimax utility value of the state
        """
        if state.is_full():
            return state.score()

        if depth == 0 and depth is not None:
            return self.evaluation(state)

        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        for move, state in state.successors():
            if depth is not None:
                util = self.minimax(state, depth - 1)
            else:
                util = self.minimax(state, None)
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util = util
        return best_util

    def evaluation(self, state):
        """Estimate the utility value of the game state based on features.

        N.B.: This method must run in O(1) time!

        Args:
            state: a connect383.GameState object representing the current board

        Returns: a heusristic estimate of the utility value of the state
        """
        #
        # Fill this in!
        #
        p1_score = 0
        p2_score = 0

        # print(state.board)
        row = len(state.board)
        column = len(state.board[0])

        for i in range(row - 1, -1, -1):
            for j in range(column):
                val = state.board[i][j]

                # Check L
                try:
                    LeftVal = state.board[i][j - 1]
                except IndexError:
                    LeftVal = None
                if LeftVal is not None and LeftVal == val:
                    if val == 1:
                        p1_score += 1
                    if val == -1:
                        p2_score += 1

                # Check UL
                try:
                    UpperLeftVal = state.board[i][j - 1]
                except IndexError:
                    UpperLeftVal = None
                if UpperLeftVal is not None and UpperLeftVal == val:
                    if val == 1:
                        p1_score += 1
                    if val == -1:
                        p2_score += 1

                # Check U
                try:
                    UpperVal = state.board[i][j - 1]
                except IndexError:
                    UpperVal = None
                if UpperVal is not None and UpperVal == val:
                    if val == 1:
                        p1_score += 1
                    if val == -1:
                        p2_score += 1

                # Check UR
                try:
                    UpperRightVal = state.board[i][j - 1]
                except IndexError:
                    UpperRightVal = None
                if UpperRightVal is not None and UpperRightVal == val:
                    if val == 1:
                        p1_score += 1
                    if val == -1:
                        p2_score += 1

                # Check R
                try:
                    RightVal = state.board[i][j - 1]
                except IndexError:
                    RightVal = None
                if RightVal is not None and RightVal == val:
                    if val == 1:
                        p1_score += 1
                    if val == -1:
                        p2_score += 1

                # Check BR
                try:
                    BottomRightVal = state.board[i][j - 1]
                except IndexError:
                    BottomRightVal = None
                if BottomRightVal is not None and BottomRightVal == val:
                    if val == 1:
                        p1_score += 1
                    if val == -1:
                        p2_score += 1

                # Check B
                try:
                    BottomVal = state.board[i][j - 1]
                except IndexError:
                    BottomVal = None
                if BottomVal is not None and BottomVal == val:
                    if val == 1:
                        p1_score += 1
                    if val == -1:
                        p2_score += 1

                # Check BL
                try:
                    BottomLeftVal = state.board[i][j - 1]
                except IndexError:
                    BottomLeftVal = None
                if BottomLeftVal is not None and BottomLeftVal == val:
                    if val == 1:
                        p1_score += 1
                    if val == -1:
                        p2_score += 1

        return p1_score - p2_score


class PruneAgent(HeuristicAgent):
    """Smarter computer agent that uses minimax with alpha-beta pruning to select the best move."""

    def minimax(self, state, depth):
        return self.minimax_prune(state, depth)

    def minimax_prune(self, state, depth):
        """Determine the minimax utility value the given state using alpha-beta pruning.

        The value should be equal to the one determined by ComputerAgent.minimax(), but the
        algorithm should do less work.  You can check this by inspecting the class variables
        GameState.p1_state_count and GameState.p2_state_count, which keep track of how many
        GameState objects were created over time.

        N.B.: When exploring the game tree and expanding nodes, you must consider the child nodes
        in the order that they are returned by GameState.successors().  That is, you cannot prune
        the state reached by moving to column 4 before you've explored the state reached by a move
        to to column 1.

        Args: see ComputerDepthLimitAgent.minimax() above

        Returns: the minimax utility value of the state
        """
        a = -math.inf
        b = math.inf



        if state.is_full():
            return state.score()

        if depth == 0 and depth is not None:
            return self.evaluation(state)

        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        for move, state in state.successors():
            if depth is not None:
                util = self.minimax_prune(state, depth - 1)
            else:
                util = self.minimax_prune(state, None)

            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util = util

            if util > b and nextp == 1:  # if maximizer's child value greater than beta, prune
                return util
            if util < a and nextp == -1:  # if minimizer's child value less than alpha, prune
                return util

            if util < b and nextp == 1:  # if maximizer's child value is less than beta, update beta
                b = util
                print("beta", b)
            if util > a and nextp == -1:  # if minimizer's child value is greater than alpha, update alpha
                a = util
                print("alpha", a)

        return best_util


