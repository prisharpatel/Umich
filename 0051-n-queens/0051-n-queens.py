class Solution:
    size = 0
    columns = {}
    diagDown = {}
    diagUp = {}
    solution = []
    solBuilder = []

    # check only columns, diagonal-1, and diagonal-2 because i am moving by row
    def recurse(self, index: int) -> None:
        if index == self.size:
            self.solution.append(self.solBuilder.copy())
            return
        else:
            for i in range(self.size):
                # prune
                if (
                    self.columns[i]
                    or self.diagUp[index + i]
                    or self.diagDown[index - i]
                ):
                    continue

                # add
                self.columns[i] = True
                self.diagUp[index + i] = True
                self.diagDown[index - i] = True
                row = "." * i + "Q" + "." * (self.size - i - 1)
                self.solBuilder.append(row)

                # recurse
                self.recurse(index + 1)

                # remove
                self.columns[i] = False
                self.diagUp[index + i] = False
                self.diagDown[index - i] = False
                self.solBuilder.pop()


    def solveNQueens(self, n: int) -> List[List[str]]:
        self.size = n
        self.columns = {}
        self.diagDown = {}
        self.diagUp = {}
        self.solution = []
        self.solBuilder = []
        for i in range(n):
            self.columns[i] = False
        for i in range(n * 2 - 1):
            for j in range(n * 2 - 1):
                self.diagDown[i - j] = False
                self.diagUp[i + j] = False
        self.recurse(0)
        return self.solution