# This "class", or virtual object, creates an "announcer" that communicates messages to the character
class Announcer(object):
    
    # Everything inside here (i.e. inside this function __init__), are things that are set
    # when the announcer is first made.
    def __init__(self, game_parameters):
        
        # Record the game's parameters
        self.game_parameters = game_parameters
        
    # Everything inside here describes what announcement we make
    def draw_announcer_messages(self):
        
        # Align the text properly
        textAlign(CENTER, CENTER)
        
        # Make the text bigger
        textSize(24)
        
        # Make the textcolor white
        fill(255)
        
        # If the game hasn't started yet, say so.
        if not self.game_parameters.game_started:
            
            # Print the starting message
            text("Press 'p' to start!", width/2., height/4.)
            
        # If the game is over, declare the winner
        if self.game_parameters.game_finished:
            
            # Print the ending message
            text(self.game_parameters.winner + " wins!", width/2., height/4.)
        
        
        
        