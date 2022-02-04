import arcade

arcade.open_window(600, 600, "Drawing")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

#grass
arcade.draw_lrtb_rectangle_filled(0, 600, 200, 0, arcade.csscolor.GREEN)

#castle Base
arcade.draw_lrtb_rectangle_filled(150, 450, 225, 200, arcade.csscolor.SANDY_BROWN)

#castle pilars
arcade.draw_lrtb_rectangle_filled(150, 200, 400, 225, arcade.csscolor.DARK_GREY)
arcade.draw_lrtb_rectangle_filled(400, 450, 400, 225, arcade.csscolor.DARK_GREY)

#castle middle sec
arcade.draw_lrtb_rectangle_filled(200, 400, 350, 225, arcade.csscolor.DARK_GREY)

#castle roof
arcade.draw_triangle_filled(150, 400, 200, 400, 175, 500, arcade.csscolor.RED)
arcade.draw_triangle_filled(400, 400, 450, 400, 425, 500, arcade.csscolor.RED)

#trees
arcade.draw_rectangle_filled(100, 150, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(100, 200, 60, 80, arcade.csscolor.DARK_GREEN)

arcade.finish_render()

arcade.run()