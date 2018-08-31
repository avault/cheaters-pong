# This "class", or virtual object, describes the parameters of the game. These are where options are set, in other words
class GameParameters(object):
    
    # Everything inside here (i.e. inside this function __init__), are things that are set
    # when the game is first made.
    def __init__(self):

        ######################################################
        # Controls
        ######################################################
        
        # What key do you press to start the game?
        self.game_start_key = 'p'
        
        #####################################################
        # Aesthetic Customization
        #####################################################
        
        # What are the names of the players?
        self.player1_name = 'Player 1'
        self.player2_name = 'Player 2'
                
        # What colors are the players?
        self.player1_color = color(79, 77, 255)
        self.player2_color = color(204, 84, 21)
        
        # What is the color for the system?
        self.system_color = color(53, 178, 18)

        ########################################################
        # Playing field options
        ########################################################
        
        # What frame rate do we want to use?
        self.frame_rate = 60.
        # Using the set frame rate, how long does a single frame last?
        self.dt = 1./self.frame_rate
        
        # How wide do we want the game field to be?
        self.field_width = 640
        self.field_height = 320

        # How wide and tall are the goals?
        self.goal_width = self.field_width/32.
        self.goal_height = self.field_height
        
        ########################################################
        # Game options
        ########################################################
        
        # How does the ball move when it's launched?
        self.ball_default_speed = 300.
        self.ball_default_angle = random(TWO_PI)
        
        # How does the ball move when it's hit by each player?
        self.ball_player1_speed = 300.
        self.ball_player2_speed = 300.      
        
        # Where do the paddles start out? Distance is mirrored
        self.paddle_default_location = self.field_width/8.
        
        # How many lives does player 1 have?
        self.player1_lives = 3
        # How many lives does player 2 have?
        self.player2_lives = 3
        
        ########################################################
        # Internal system parameters. These are changed during the game.
        ########################################################
        
        # By default, the game hasn't started yet, so say so.
        self.game_started = False
        
        # By default, the game isn't over yet, so say so
        self.game_finished = False
        
        # Keep track of the number of volleys per round. Starts at 0
        self.number_of_volleys = 0
        