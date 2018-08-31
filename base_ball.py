# This "class", or virtual object, describes a ball.
class Ball(object):
    
    # Everything inside here (i.e. inside this function __init__), are things that are set
    # when the ball is first made.
    def __init__(self, x_position, y_position, x_velocity, y_velocity, ball_color):
        
        # This line sets how big the ball is
        self.radius = 12.
        
        # These lines set where the ball starts out (i.e. the position of the ball)
        self.x_position = x_position
        self.y_position = y_position
        
        # These lines set how fast the ball is moving (i.e. the velocity of the ball)
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        
        # What color is the ball?
        self.ball_color = ball_color
        
        # This line says how fast the ball moves
        self.speed = 5
        
    # Everything inside here decides what the ball actually looks like
    def draw_ball(self):
        
        # Make sure the ball is the right color
        fill(self.ball_color)
        
        # This line actually draws the ball!
        ellipse(self.x_position, self.y_position, self.radius*2., self.radius*2.)
        
    # Everything inside here describes how we move the ball
    def move_ball(self, dt):
        
        # The ball is moved horizontally by the horizontal speed of the paddle multiplied by the time a single frame takes
        self.x_position += self.x_velocity*dt
        
        # Move the ball vertically by the vertical speed of the paddle multiplied by the time a single frame takes
        self.y_position += self.y_velocity*dt
        
        
        
    