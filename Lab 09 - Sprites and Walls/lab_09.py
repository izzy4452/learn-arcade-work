import arcade
import random

# --- Constants ---
SPRITE_SIZE = 0.3
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_GEM = 0.5
GEM_COUNT = 5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite and Walls")

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.gem_list = None

        # Set up the player
        self.player_sprite = None

        #physics engine variable
        self.physics_engine = None

        self.set_mouse_visible(False)

        # One GUI camera and one sprite
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):

        # Background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        # Reset the score
        self.score = 0

        # Create the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 90
        self.player_list.append(self.player_sprite)


        # --- Manually place walls
        wall = arcade.Sprite(":resources:images/tiles/stoneHalf_mid.png", SPRITE_SCALING_BOX)
        wall.center_x = 0
        wall.center_y = 50
        self.wall_list.append(wall)

        wall = arcade.Sprite(":resources:images/tiles/stoneHalf_right.png", SPRITE_SCALING_BOX)
        wall.center_x = 50
        wall.center_y = 50
        self.wall_list.append(wall)

        wall = arcade.Sprite(":resources:images/tiles/stoneHalf_left.png", SPRITE_SCALING_BOX)
        wall.center_x = 775
        wall.center_y = 175
        self.wall_list.append(wall)

        wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png")
        wall.center_x = 500
        wall.center_y = -5
        self.wall_list.append(wall)

        # --- Boxes inside a loop
        for x in range(173, 700, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassHalf_mid.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 50
            self.wall_list.append(wall)

        for x in range(0, 650, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassHalf_mid.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 175
            self.wall_list.append(wall)

        for x in range(0, 500, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassHalf_mid.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 300
            self.wall_list.append(wall)

        for x in range(0, 550, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassHalf_mid.png", SPRITE_SCALING_BOX)
            wall.center_x = 600
            wall.center_y = 300
            self.wall_list.append(wall)

        # --- Walls with a list
        coordinate_list = [[400, 400],
                           [470, 400],
                           [540, 400],
                           [470, 470]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite(":resources:images/tiles/grassHalf_mid.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # horizontal walls
        for y in (-100, SCREEN_HEIGHT - SPRITE_SIZE):
            for x in range(0, SCREEN_WIDTH):
                wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", SPRITE_SCALING_BOX)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)

        #vertical walls
        for x in (-100, SCREEN_WIDTH - SPRITE_SIZE):
            for y in range(-100, SCREEN_HEIGHT):
                wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", SPRITE_SCALING_BOX)
                wall.left = x
                wall.bottom = y
                self.wall_list.append(wall)

            #create gems
            for i in range(GEM_COUNT):

                gem = arcade.Sprite(":resources:images/items/gemRed.png", SPRITE_SCALING_GEM)

                gem.center_x = random.randrange(SCREEN_WIDTH)
                gem.center_y = random.randrange(SCREEN_HEIGHT)

                gem_placed_successfully = False

                while not gem_placed_successfully:

                    gem.center_x = random.randrange(SCREEN_WIDTH)
                    gem.center_y = random.randrange(SCREEN_HEIGHT)

                    # See if the coin is hitting a wall
                    wall_hit_list = arcade.check_for_collision_with_list(gem, self.wall_list)

                    # See if the coin is hitting another coin
                    gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)

                    if len(wall_hit_list) == 0 and len(gem_hit_list) == 0:

                        gem_placed_successfully = True

                self.gem_list.append(gem)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()

        self.camera_for_sprites.use()

        # Draw the sprites
        self.wall_list.draw()
        self.player_list.draw()
        self.gem_list.draw()

        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.physics_engine.update()

        # Scroll the screen to the player
        #self.scroll_to_player()

        # Scroll the window to the player.
        CAMERA_SPEED = 1
        lower_left_corner = (self.player_sprite.center_x - self.width / 2,
                             self.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)


        # Call update on all sprites
        self.gem_list.update()

        # list of all sprites that collided with the player.
        gems_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.gem_list)

        for gem in gems_hit_list:
            gem.remove_from_sprite_lists()
            self.score += 1

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()