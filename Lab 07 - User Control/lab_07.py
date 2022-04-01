""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hits the edge of the screen
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

        # ball hits edges of window, sound effect is trigged
        if self.position_x < self.radius:
            self.position_x = self.radius

        #if self.position_x > self.hit_sound - self.radius:
            #self.position_x = self.hit_sound - self.radius

class Square:
    def __init__(self, position_x, position_y, change_x, change_y, width, height, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x,
                                     self.position_y,
                                     self.width,
                                     self.height,
                                     self.color)

    def update(self):

        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hits the edge of the screen
        if self.position_x < self.width:
            self.position_x = self.width

        if self.position_x > SCREEN_WIDTH - self.width:
            self.position_x = SCREEN_WIDTH - self.width

        if self.position_y < self.width:
            self.position_y = self.width

        if self.position_y > SCREEN_HEIGHT - self.width:
            self.position_y = SCREEN_HEIGHT - self.width

        if self.position_x < self.height:
            self.position_x = self.height

        if self.position_x > SCREEN_WIDTH - self.height:
            self.position_x = SCREEN_WIDTH - self.height

        if self.position_y < self.height:
            self.position_y = self.height

        if self.position_y > SCREEN_HEIGHT - self.height:
            self.position_y = SCREEN_HEIGHT - self.height

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.explosion_sound = arcade.load_sound(":resources:sounds/explosion1.wav")
        self.explosion_sound_player = None

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.csscolor.SKY_BLUE)

        self.ball = Ball(50, 50, 0, 0, 15, arcade.csscolor.BLACK)

        self.square = Square(80, 80, 0, 0, 50, 50, arcade.csscolor.RED)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(100, 500, 50, arcade.csscolor.GHOST_WHITE)
        arcade.draw_ellipse_filled(100, 475, 200, 70, arcade.csscolor.GHOST_WHITE)

        #ball
        self.ball.draw()

        #square
        self.square.draw()

    def update(self, delta_time):

        self.ball.update()

        self.square.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses the key"""
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

        if not self.explosion_sound_player or not self.explosion_sound_player.playing:
            self.explosion_sound_player = arcade.play_sound(self.explosion_sound)


    def on_key_release(self, key, modifiers):
        """ Called when user releases key"""
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.square.position_x = x
        self.square.position_y = y

        if not self.explosion_sound_player or not self.explosion_sound_player.playing:
            self.explosion_sound_player = arcade.play_sound(self.explosion_sound)


def main():
    window = MyGame()
    arcade.run()


main()