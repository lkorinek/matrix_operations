from matrix_class import Matrix


class MatrixInterface:

    def __init__(self):
        # List of all matrices
        self.matrices = []
        self.exit = False

        self.run()

    def save_to_file(self, idx):
        """
        Save values to a file.
        """
        file = open("matice_"+str(idx)+".txt", "w")

        result = ""
        matrix = self.matrices[idx]
        for x in range(matrix.row):
            for y in range(matrix.col):
                if matrix.matrix[x][y] < 10:
                    result += " "
                result += str(matrix.matrix[x][y])
                if y != (matrix.col-1):
                    result += " "
            result += "\n"

        file.write(result)
        file.close()

    def create_matrix(self):
        """
        Create a new matrix and add it to class list of matrices.
        Values are loaded from a file if not inserted.
        """

        rows = self.get_int("Počet řádků: ")[0]
        columns = self.get_int("Počet sloupců: ")[0]
        own_values = self.get_input("Vlastní hodnoty? (Ano) ")[0]

        matrix_values = None
        if own_values == "ano":
            prompt_txt = "Zadejte prosím hodnoty matice oddělené mezerou:\n"
            matrix_values = []
            while True:
                numbers = self.get_int(prompt_txt)
                if len(numbers) == (rows*columns):
                    for row in range(rows):
                        matrix_values.append(numbers[row*columns:(row+1)*columns])
                    break
                prompt_txt = "Chybně zadané hodnoty. Zkuste to prosím znovu:\n"

        # Save the matrix in class list and print info about the matrix
        self.matrices.append(Matrix(rows, columns, matrix_values))
        self.show_matrix_info(len(self.matrices)-1)

    def show_matrices(self):
        """
        Show all saved matrices.
        """

        print("Seznam všech matic:")
        if not self.matrices:
            print("Žádné")
        for idx, matrix in enumerate(self.matrices):
            print("matice_"+str(idx)+" "+str(matrix.row)+" x "+str(matrix.col))

    def show_matrix_info(self, idx):
        """
        Show info (values, possible operations) about matrix, when its name is called.
        """

        print("\nHodnoty matice 'matice_"+str(idx)+"':")
        print(self.matrices[idx])
        print("Možné operace:")
        self.get_possible_operations(idx)
        print("")

    def get_possible_operations(self, given_idx):
        """
        Print possible operations of given matrix
        """

        given_matrix = self.matrices[given_idx]
        # addition = 0, multiply = 1
        operations = [[] for _ in range(2)]

        # Check and save operations which are valid
        for idx, matrix in enumerate(self.matrices):
            if given_matrix.row == matrix.row and given_matrix.col == matrix.col and idx != given_idx:
                operations[0].append(idx)
            if given_matrix.col == matrix.row and idx != given_idx:
                operations[1].append(idx)

        # Print possible operations
        if operations[0]:
            print("Sčítání a odčítání:")
            for idx in operations[0]:
                print("matice_"+str(idx))
        if operations[1]:
            print("Násobení:")
            for idx in operations[1]:
                print("matice_"+str(idx))
        if not operations[0] and not operations[1]:
            print('Žádné')

    def execute_operation(self, operation):
        """
        Execute given operation
        """

        matrix_1 = self.matrices[int(operation[0][-1])]
        # Check whether operation is scalar multiplication
        if operation[2][0] != 'm':
            self.matrices.append(Matrix(own=matrix_1.scalar_multiplication(int(operation[2][0]))))

        # Operations between two matrices
        else:
            matrix_2 = self.matrices[int(operation[2][-1])]
            if operation[1] == "+":
                self.matrices.append(Matrix(own=matrix_1 + matrix_2))
            elif operation[1] == "-":
                self.matrices.append(Matrix(own=matrix_1 - matrix_2))
            elif operation[1] == "*":
                self.matrices.append(Matrix(own=matrix_1 * matrix_2))
            elif operation[1] == "/":
                self.matrices.append(Matrix(own=matrix_1 / matrix_2))
        self.show_matrix_info(len(self.matrices)-1)

    def help_funtion(self):
        """
        Print possible commands.
        """
        txt = "Seznam všech možných příkazů\n\n" \
              "exit - vypnutí programu\n" \
              "create matrix - vytvoření nové matice\n" \
              "list - seznam všech matic\n" \
              "execute - provedení operace př. 'execute matice_0 + matice_1'\n" \
              "          násobení skalárem možné následnovně 'execute matice_0 * 3'\n" \
              "transpose - vytvoření transponované matice př. 'transpose matice_0'\n" \
              "show - vypsání hodnot matice a možných operací s ostatními maticemi př. 'show matice_0'\n" \
              "save - uložení matice do souboru př. 'save matice_0' uloží matici do souboru matice_0.txt\n" \

        print(txt)

    def get_int(self, txt=""):
        """
        Check if input is an integer.
        :return: list
        """

        val = []
        while True:
            try:
                tmp = input(txt).split()
                for x in tmp:
                    val.append(int(x))
                break
            except ValueError:
                print("Vstup musí být typu Integer")

        return val

    def get_input(self, txt=""):
        """
        Split input on whitespace and convert all letters to lowercase.
        :return: list
        """

        val = input(txt)
        result = [elem.lower() for elem in val.split()]
        result.append(val)
        return result

    def run(self):
        """
        Run the program in a loop. Exit when "exit" is called.
        """

        first = True
        while not self.exit:
            # Check if program runs the first time
            if first:
                print("Program matice")
                first = False

            command = self.get_input("Příkaz: ")

            if command[0] == "exit":
                if self.get_input("Opravdu si přejete ukončit program? (Ano) ")[0] == "ano":
                    self.exit = True
            elif command[-1] == "create matrix":
                self.create_matrix()
            elif command[0] == "list":
                self.show_matrices()
            elif command[0] == "execute":
                self.execute_operation(command[1:-1])
            elif command[0] == "transpose":
                self.matrices.append(Matrix(own=self.matrices[int(command[1][-1])].transpose()))
                self.show_matrix_info(len(self.matrices) - 1)
            elif command[0] == "show":
                self.show_matrix_info(int(command[1][-1]))
            elif command[0] == "save":
                self.save_to_file(int(command[1][-1]))
            elif command[0] == "help":
                self.help_funtion()
        print("Naviděnou! :)")


if __name__ == "__main__":
    # MatrixInterface()

    numbers = []
    result = []
    for x in range(1,501,2):
        numbers.append(x)
    for x in numbers:
        if x % 3 == 1 and x % 4 == 1 and x % 5 == 1 and x % 6 == 1 and x % 7 == 0:
            result.append(x)
    print(result)