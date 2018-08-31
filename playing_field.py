# This "class", or virtual object, describes the playing field.
class PlayingField(object):
    
    # Everything inside here (i.e. inside this function __init__), are things that are set
    # when the playing field is first made.
    def __init__(self, game_parameters):
        
        # Record what the game parameters are
        self.game_parameters = game_parameters
        
    # Everything inside here decides what the playing field actually looks like
    def draw_field(self):
        
        # Draw the mid-line
        
        rectMode(CENTER) # Make sure the rectangle's centered
        fill(self.game_parameters.system_color) # Change the color to the system color.
        rect(width/2., height/2., 5., height) # Draw the centerline
        
        # Draw player 1's goal
        fill(self.game_parameters.player1_color) # Change the color to player 1's color.
        rect(self.game_parameters.goal_width/2., height/2., self.game_parameters.goal_width, self.game_parameters.goal_height) # Draw the goal
        
        # Draw player 2's goal
        fill(self.game_parameters.player2_color) # Change the color to player 1's color.
        rect(width - self.game_parameters.goal_width/2., height/2., self.game_parameters.goal_width, self.game_parameters.goal_height) # Draw the goal