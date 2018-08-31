# Import other files here
# Import the modules we'll use

import announcer
import base_ball
import base_paddle
import collision_handler
import game_parameters
import playing_field
import score_system
import smart_paddle


######################################################################
# Create virtual objects (classes) to be used later
######################################################################

# Set the game parameters
gp = game_parameters.GameParameters()

# Make the playing field
pf = playing_field.PlayingField(gp)

# Make the "watcher" that decides what happens when collisions occur
c = collision_handler.CollisionHandler(gp)

# Make the score system
s = score_system.ScoreSystem(gp)

# Make the announcer
a = announcer.Announcer(gp)

# Make the ball(s)
b = base_ball.Ball(gp.field_width / 2., gp.field_height / 2., 0., 0., gp.system_color)

# Make the player paddle
p1 = base_paddle.Paddle(gp.paddle_default_location, gp.field_height/2., 'w', 's')

# Make the AI paddle
p2 = smart_paddle.SmartPaddle(gp.field_width - gp.paddle_default_location, gp.field_height/2., gp, b)

#####################################################################

# Setup the game window
def setup():
    size(gp.field_width, gp.field_height)
    frameRate(gp.frame_rate)

# Everything inside here is the game itself
def draw():

    # Draw the background
    background(0)

    # This section describes some of what happens when you press a key
    if keyPressed:

        # If we press the right key (and the game isn't already started), start the game!
        if (key == gp.game_start_key) and (not gp.game_started):

            # Launch the ball!
            b.x_velocity = gp.ball_default_speed * cos(gp.ball_default_angle)
            b.y_velocity = gp.ball_default_speed * sin(gp.ball_default_angle)
            
            # Tell the computer that the game started!
            gp.game_started = True
            
    # Have the AI paddle "watch" the ball
    p2.paddle_sight()

    # Test if the different objects collided
    c.paddle_wall_collision(p1)
    c.paddle_wall_collision(p2)
    c.ball_paddle_collision(b, p1)
    c.ball_paddle_collision(b, p2)
    c.ball_vertical_wall_collision(b)
    c.ball_goal_collision(b)
    
    # Move the different objects
    p1.move_paddle(gp.dt)
    p2.move_paddle(gp.dt)
    b.move_ball(gp.dt)

    # Display the score system
    s.display_score()

    # Draw the different objects
    pf.draw_field()
    b.draw_ball()
    p1.draw_paddle()
    p2.draw_paddle()
    a.draw_announcer_messages()
    