import random


class Matrix:

    def __init__(self, row=0, col=0, own=None):
        """
        Initilize matrix size and values.
        """

        self.row = row
        self.col = col
        if not own:
            self.matrix = self.load_from_file()
        else:
            self.matrix = own
            self.row = len(self.matrix)
            self.col = len(self.matrix[0])

    def __str__(self):
        """
        Print matrix in human readable format.
        :return string
        """

        result = ""
        for x in range(self.row):
            result += "["
            for y in range(self.col):
                if self.matrix[x][y] < 10:
                    result += " "
                result += str(self.matrix[x][y])
                if y != (self.col-1):
                    result += " "
            result += "]\n"

        return result

    def load_from_file(self):
        """
        Load values from a file.
        :return: 2D list
        """

        file = open('input.txt', 'r')
        numbers = file.readlines(random.randint(0, 700))
        file.close()

        values = [[int(numbers[idx]) for idx in range(self.col*offset, self.col*(offset+1))]
                  for offset in range(self.row)]

        return values

    def return_dimension(self, dim):
        """
        Return dimensions of a matrix.
        :return: array
        """

        if dim == "row":
            return self.row
        elif dim == "col":
            return self.col

    def __add__(self, other):
        """
        Add two matrices together.
        :return: 2D array
        """

        if self.row != other.row and self.col != other.col:
            return "Matice musejí být stejného typu"

        result = [[0 for _ in range(self.col)]for _ in range(self.row)]
        for x in range(self.row):
            for y in range(self.col):
                result[x][y] = self.matrix[x][y] + other.matrix[x][y]
        return result

    def __sub__(self, other):
        """
        Subtract two matrices.
        :return: 2D array
        """

        if self.row != other.row and self.col != other.col:
            return "Matice musejí být stejného typu"

        result = [[0 for _ in range(self.col)]for _ in range(self.row)]
        for x in range(self.row):
            for y in range(self.col):
                result[x][y] = self.matrix[x][y] - other.matrix[x][y]
        return result

    def __mul__(self, other):
        """
        Multiply two matrices together.
        :return: 2D array
        """

        if self.col != other.row:
            return "První matice musí mít stejný počet sloupců jako je počet řádků druhé matice"

        result = [[0 for _ in range(other.col)]for _ in range(self.row)]
        for row in range(self.row):
            for col in range(other.col):
                num_value = 0
                for p in range(self.col):
                    num_value += self.matrix[row][p] * other.matrix[p][col]
                result[row][col] = num_value

        return result

    def scalar_multiplication(self, scal):
        """
        multiply matrix by scalar.
        :return: 2D array
        """

        result = self.matrix.copy()
        for x in range(self.row):
            for y in range(self.col):
                result[x][y] *= scal

        return result

    def transpose(self):
        """
        Transpose matrix.
        :return: 2D array
        """

        result = [[0 for _ in range(self.row)] for _ in range(self.col)]

        for row in range(self.row):
            for col in range(self.col):
                result[col][row] = self.matrix[row][col]

        return result
