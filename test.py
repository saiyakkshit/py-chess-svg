import unittest
import os
from my_project import generate_board_image

class TestGenerateBoardImage(unittest.TestCase):
    def test_generate_board_image(self):
        # Define the moves for the test
        moves = ["e4", "e5", "Nf3"]

        # Call the function being tested
        generate_board_image(moves)

        # Verify that the SVG file is generated
        self.assertTrue(os.path.exists("board.svg"))

if __name__ == "__main__":
    unittest.main()
