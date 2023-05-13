from PIL import ImageGrab
import pyautogui

# YOU MAY NEED TO CHANGE THESE VALUES BASED ON YOUR SCREEN SIZE
LEFT = 570
TOP = 200
RIGHT = 1350
BOTTOM = 875

EMPTY = 0
RED = 1
BLUE = 2


class Board:
    def __init__(self) -> None:
        self.board = [[EMPTY for i in range(7)] for j in range(6)]
        self.columns = 7
        self.board = [[EMPTY for _ in range(self.columns)] for _ in range(6)]
        self.rows = 7
        self.board = [[EMPTY for _ in range(self.rows)] for _ in range(6)]

    def get_window(self):
        return pyautogui.screenshot(region=(LEFT, TOP, RIGHT - LEFT, BOTTOM - TOP))
    def get_window(self):
        return pyautogui.screenshot(region=(LEFT, TOP, BOTTOM, RIGHT))

    def get_window(self, left, top, width, height):
        return pyautogui.screenshot(region=(left, top, width, height))

    def print_grid(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY:
                    print("*", end=" \t")
                elif grid[i][j] == RED:
                    print("R", end=" \t")
                elif grid[i][j] == BLUE:
                    print("B", end=" \t")
            print("\n")

    def _convert_grid_to_color(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == (255, 255, 255):
                    grid[i][j] = EMPTY
                elif grid[i][j][0] > 200:
                    grid[i][j] = RED
                elif grid[i][j][0] > 50:
                    grid[i][j] = BLUE
        return grid

    def _get_grid_cordinates(self):
        startCord = (50, 55)
        cordArr = []
        for i in range(0, 7):
            for j in range(0, 6):
                x = startCord[0] + i * 115
                y = startCord[1] + j * 112
                cordArr.append((x, y))
        return cordArr

    def _transpose_grid(self, grid):
        return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

    def _capture_image(self, left, top, right, bottom):
        image = pyautogui.screenshot()
        cropedImage = image.crop((left, top, right, bottom))
        return cropedImage

    def _convert_image_to_grid(self, image):
        pixels = [[] for i in range(7)]
        i = 0
        for index, cord in enumerate(self._get_grid_cordinates()):
            pixel = image.getpixel(cord)
            if index % 6 == 0 and index != 0:
                i += 1
            pixels[i].append(pixel)
        return pixels

    def _get_grid(self):
        cropedImage = self._capture_image()
        pixels = self._convert_image_to_grid(cropedImage)
        # cropedImage.show()
        grid = self._transpose_grid(pixels)
        return grid

    def _check_if_game_end(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY and self.board[i][j] != EMPTY:
                    return True
        return False

    def get_game_grid(self):
        game_grid = self._get_grid()
        new_grid = self._convert_grid_to_color(game_grid)
        is_game_end = self._check_if_game_end(new_grid)
        self.board = new_grid
        return (self.board, is_game_end)

    def select_column(self, column):
        pyautogui.click(
            self._get_grid_cordinates()[column][0] + LEFT,
            self._get_grid_cordinates()[column][1] + TOP,
        )

    def is_game_over(self):
        # Check for a win
        if self.check_for_win(RED):
            print("Red wins!")
            return True
        elif self.check_for_win(BLUE):
            print("Blue wins!")
            return True

        # Check for a draw
        if self.is_board_full():
            print("It's a draw!")
            return True

        return False

    def check_for_win(self, player):
        # Check horizontally
        for row in range(6):
            for col in range(4):
                if self.board[row][col] == player and self.board[row][col + 1] == player and \
                        self.board[row][col + 2] == player and self.board[row][col + 3] == player:
                    return True

        # Check vertically
        for row in range(3):
            for col in range(7):
                if self.board[row][col] == player and self.board[row + 1][col] == player and \
                        self.board[row + 2][col] == player and self.board[row + 3][col] == player:
                    return True

        # Check diagonally (from top left to bottom right)
        for row in range(3):
            for col in range(4):
                if self.board[row][col] == player and self.board[row + 1][col + 1] == player and \
                        self.board[row + 2][col + 2] == player and self.board[row + 3][col + 3] == player:
                    return True

        # Check diagonally (from top right to bottom left)
        for row in range(3):
            for col in range(3, 7):
                if self.board[row][col] == player and self.board[row + 1][col - 1] == player and \
                        self.board[row + 2][col - 2] == player and self.board[row + 3][col - 3] == player:
                    return True

        return False

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == EMPTY:
                    return False
        return True

    def get_game_grid(self, left, top, right, bottom):
        cropedImage = self._capture_image(left, top, right, bottom)
        pixels = self._convert_image_to_grid(cropedImage)
        grid = self._transpose_grid(pixels)
        new_grid = self._convert_grid_to_color(grid)
        is_game_end = self._check_if_game_end(new_grid)
        self.board = new_grid
        return self.board, is_game_end
