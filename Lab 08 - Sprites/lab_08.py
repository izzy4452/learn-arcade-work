
import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_GEM = 0.3
GEM_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Gem(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists.
        self.player_list = None
        self.gem_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(GEM_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            gem = Gem(":resources:images/items/gemRed.png", SPRITE_SCALING_GEM)

            # Position the gem
            gem.center_x = random.randrange(SCREEN_WIDTH)
            gem.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.gem_list.append(gem)

    def on_draw(self):
        arcade.start_render()

        # Draw the sprite lists here. Typically sprites are divided into
        # different groups. Other game engines might call these "sprite layers"
        # or "sprite groups." Sprites that don't move should be drawn in their
        # own group for the best performance, as Arcade can tell the graphics
        # card to just redraw them at the same spot.
        # Try to avoid drawing sprites on their own, use a SpriteList
        # because there are many performance improvements in that code.
        self.gem_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.gem_list.update()

        # Generate a list of all sprites that collided with the player.
        gems_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.gem_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for gem in gems_hit_list:
            gem.reset_pos()
            self.score += 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()