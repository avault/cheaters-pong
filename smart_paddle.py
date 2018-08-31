# This "class", or virtual object, describes a paddle controlled by an AI.
class SmartPaddle(object):
       
    # Everything inside here (i.e. inside this function __init__), are things that are set
    # when the paddle is first made.
    def __init__(self, x_position, y_position, game_parameters, watched_ball):
        
        # Here we set the size of the paddle
        self.width = 20.
        self.height = 100.
        
        # These lines set where the paddle is (i.e. the position of the paddle)
        self.x_position = x_position
        self.y_position = y_position
        
        # This line set how fast the paddle moves
        self.speed = 200.
        
        # Record the game's parameters
        self.game_parameters = game_parameters
        
        # Save which ball we're watching
        self.watched_ball = watched_ball
        
        # Record the number of volleys the paddle has "seen" so far.
        self.watched_volleys = 0
        
        # What is the target location for this paddle to move to?
        self.target_location = self.game_parameters.field_height/2.
        
    # Everything inside here decides what the paddle actually looks like
    def draw_paddle(self):
        
        # This line is where we set say that we want to draw our paddle from the center, not from some the corner (i.e. rectMode(CORNER)), or something of the sort
        rectMode(CENTER)
        
        # This is the line that actually draws the paddle!
        rect(self.x_position, self.y_position, self.width, self.height)
        
    # This is how we move the paddle.
    def move_paddle(self, dt):
        
        # Calculate how far to the target
        target_displacement = self.target_location - self.y_position
        target_distance = abs(target_displacement)

        if (target_distance > 5):
            target_direction = target_displacement/target_distance
            self.y_position += target_direction*self.speed*dt
        
    # The paddle "watches" to see when the ball was launched or returned by its opponent. When it does, it finds the new location to move to.
    # The means to do that is described in this function.
    def paddle_sight(self):
        
        # Have we seen any volleys yet?
        watched_no_volleys = (self.watched_volleys == 0)
        
        # Or does the number of volleys we've seen need to be updated?
        need_to_update_watched_volleys = (self.watched_volleys != self.game_parameters.number_of_volleys)
        
        # If either of the above are true, calculate the target location for the AI to move to
        if (watched_no_volleys or need_to_update_watched_volleys):
            self.calculate_paddle_target()
            
        # Also, if we need to update the number of volleys we've seen, then do so
        if need_to_update_watched_volleys:
            self.watched_volleys = self.game_parameters.number_of_volleys
            
    # Everything inside here describes how the paddle calculates which location to move to.
    def calculate_paddle_target(self):
        
        # Don't bother to do any of this, unless the ball is moving
        if (self.watched_ball.x_velocity == 0.) or (self.watched_ball.y_velocity == 0.):
            return 0
        
        # Calculate the time it takes until the first bounce
        if (self.watched_ball.y_velocity < 0):
            t_0 = self.watched_ball.y_position/abs(self.watched_ball.y_velocity)
        elif (self.watched_ball.y_velocity > 0):
            t_0 = (self.game_parameters.field_height - self.watched_ball.y_position)/abs(self.watched_ball.y_velocity)
            
        # Calculate the time it takes until the paddle hits the target.
        t = (self.x_position - self.watched_ball.x_position)/self.watched_ball.x_velocity
        
        # If the ball never hits the paddle (t is negative), then break out of the function
        if (t < 0.):
            return 0
        
        # Calculate the time from the first bounce until the target
        t_prime = t - t_0
        
        # When there's no bouncing (t_0 > t), exit early
        if (t_prime < 0):
            self.target_location = self.watched_ball.y_position + self.watched_ball.y_velocity*t
        
        # Then the distance the ball travels after the last bounce is...
        final_distance = (abs(self.watched_ball.y_velocity)*t_prime % self.game_parameters.field_height)
        
        # And the number of times it bounced is...
        n_bounced = (abs(self.watched_ball.y_velocity)*t_prime - final_distance)/self.game_parameters.field_height + 1
        n_bounced = int(n_bounced)
        
        # Now we look at where the ball will end up depending on both number of bounces and and what the original direction of motion was
        if (self.watched_ball.y_velocity < 0):
            # If n is odd, then the final yposition will just be the final distance
            if (n_bounced % 2) == 1:
                self.target_location = final_distance
            # Else if n is even, the final y position will be the final distance away from the other wall
            if (n_bounced % 2) == 0:
                self.target_location = self.game_parameters.field_height - final_distance
        elif (self.watched_ball.y_velocity >= 0):
             # If n is even, then the final yposition will just be the final distance
            if (n_bounced % 2) == 0:
                self.target_location = final_distance
            # Else if n is odd, the final y position will be the final distance away from the other wall
            if (n_bounced % 2) == 1:
                self.target_location = self.game_parameters.field_height - final_distance

            
        