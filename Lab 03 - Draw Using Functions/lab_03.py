import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def draw_grass():
    """Draw the ground"""
    arcade.draw_lrtb_rectangle_filled(0, 600, 200 / 1, 0,  arcade.csscolor.GREEN)

def draw_castle():
    """Draw a castle"""

    #base
    arcade.draw_lrtb_rectangle_filled(150, 450, 225, 200, arcade.csscolor.SANDY_BROWN)

    # castle middle sec
    arcade.draw_lrtb_rectangle_filled(200, 400, 350, 225, arcade.csscolor.DARK_GREY)

def draw_spire(x, y):

    #castle pilars
    arcade.draw_lrtb_rectangle_filled(x, 200, 200 + y, 225, arcade.csscolor.DARK_GREY)

    # castle roof
    arcade.draw_triangle_filled(x, 200 + y, 200, 200 + y, 175, 500, arcade.csscolor.RED)

def draw_spire2(x, y):

    #castle pilar
    arcade.draw_lrtb_rectangle_filled(x, 450 + y, 400, 225, arcade.csscolor.DARK_GREY)

    #castle roof
    arcade.draw_triangle_filled(x, 400 + y, 450, 400, 425, 500, arcade.csscolor.RED)

def draw_tree(x, y):

    # tree trunk
    arcade.draw_rectangle_filled(x, 110 + y, 20, 60, arcade.csscolor.SIENNA)

    #tree leafs
    arcade.draw_ellipse_filled(x, 160 + y, 60, 80, arcade.csscolor.DARK_GREEN)


def on_draw(delta_time):
    """Draw everything"""
    arcade.start_render()

    draw_grass()
    draw_castle()
    draw_spire(on_draw.draw_spire_x, 200)
    draw_spire2(400, 0)
    draw_tree(100, 40)
    draw_tree(300, 30)


    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.draw_spire_x += 0.50

# Create a value that our on_draw.snow_person1_x will start at.
on_draw.draw_spire_x= 150

def main():
    arcade.open_window(600, 600, "Drawing with Functions")
    arcade.set_background_color(arcade.csscolor.SKY_BLUE)

    #Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()

#Call the main function to get the program started.
main()
