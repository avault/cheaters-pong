# This "class", or virtual object, describes a paddle.
class Paddle(object):
       
    # Everything inside here (i.e. inside this function __init__), are things that are set
    # when the paddle is first made.
    def __init__(self, x_position, y_position, up_key, down_key):
        
        # Here we set the size of the paddle
        self.width = 20.
        self.height = 100.
        
        # These lines set where the paddle is (i.e. the position of the paddle)
        self.x_position = x_position
        self.y_position = y_position
        
        # This line set how fast the paddle moves
        self.speed = 200.
        
        # These lines set how the paddle is controlled.
        self.up = up_key
        self.down = down_key
        
    # Everything inside here decides what the paddle actually looks like
    def draw_paddle(self):
        
        # This line is where we set say that we want to draw our paddle from the center, not from some the corner (i.e. rectMode(CORNER)), or something of the sort
        rectMode(CENTER)
        
        # This is the line that actually draws the paddle!
        rect(self.x_position, self.y_position, self.width, self.height)
        
    # This is how we move the paddle.
    def move_paddle(self, dt):
        
        # Only move the paddle when a key was pressed
        if keyPressed == True:
        
            # This line checks if the key that was pressed is the key that moves the paddle up.
            if key == self.up:
                # The paddle is moved upwards by the speed of the paddle multiplied by the time a single frame takes
                self.y_position -= self.speed*dt
            # This line checks if the key that was pressed is the key that moves the paddle down.
            elif key == self.down:
                # The paddle is moved downwards by the speed of the paddle multiplied by the time a single frame takes
                self.y_position += self.speed*dt