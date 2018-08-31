# This "class", or virtual object, describes the score system.
class ScoreSystem(object):
    
    # Everything inside here (i.e. inside this function __init__), are things that are set
    # when the paddle is first made.
    def __init__(self, game_parameters):
        
        # Record the game's parameters
        self.game_parameters = game_parameters
        
        # Set how large the score icons are
        self.score_icon_size = 15
        
        # Set the vertical height of the scores
        self.y_position = self.game_parameters.field_height*1./16.
        
        # Set where the scorest start off horizontally
        self.x_offset = self.score_icon_size*1.5
        
    # Everything inside here decides how we display the score.
    def display_score(self):
        
        # Place the score icons for player 1
        # We loop over the number of lives this player has and display and icon for each life.
        fill(self.game_parameters.player1_color) # But before that, make sure we display the right color
        for i in range(self.game_parameters.player1_lives):
            
            # The x position of the current icon is set to the middle of the playing field, and then shifted over a bit.
            icon_x_position = width/2. - (float(i) + 1)*self.x_offset
            
            # Actually draw the icon
            ellipse(icon_x_position, self.y_position, self.score_icon_size, self.score_icon_size)
            
        # Place the score icons for player 2
        # We loop over the number of lives this player has and display and icon for each life.
        fill(self.game_parameters.player2_color) # But before that, make sure we display the right color
        for i in range(self.game_parameters.player2_lives):
            
            # The x position of the current icon is set to the middle of the playing field, and then shifted over a bit.
            icon_x_position = width/2. + (float(i) + 1)*self.x_offset
            
            # Actually draw the icon
            ellipse(icon_x_position, self.y_position, self.score_icon_size, self.score_icon_size)