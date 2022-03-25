""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

    def on_draw(self):
        arcade.start_render()
        #wall
        arcade.draw_lrtb_rectangle_filled(0, 600, 200 / 1, 0, arcade.csscolor.DIM_GRAY)
        arcade.set_background_color(arcade.csscolor.SKY_BLUE)

def main():
    window = MyGame()
    arcade.run()


main()