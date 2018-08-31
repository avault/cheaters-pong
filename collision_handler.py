# This "class", or virtual object, is a collision handler. It's a virtual "watcher" that decides what happens when two objects collide.
class CollisionHandler(object):
    
    # Everything inside here (i.e. inside this function __init__), are things that are set
    # when the collision handler is first made.
    def __init__(self, game_parameters):
        
        # Record the game's parameters
        self.game_parameters = game_parameters

    # Everything inside here says what happens when a ball hits a paddle
    def ball_paddle_collision(self, ball, paddle):
        
        # First, we check if there's horizontal overlap.
        horizontal_displacement = ball.x_position - paddle.x_position
        horizontal_distance = abs(horizontal_displacement) # This is horizontal distance between the ball and the paddle. Take absolute value to avoid negatives or positives.
        shortest_horizontal_distance_before_overlap = ball.radius + paddle.width/2. # This is the closest the ball and the paddle can get without colliding
        horizontal_overlap = (horizontal_distance < shortest_horizontal_distance_before_overlap) # This is a boolean that is true if there's overlap horizontally
        
        # Second, we check if there's vertical overlap.
        vertical_displacement = ball.y_position - paddle.y_position
        vertical_distance = abs(vertical_displacement) # This is vertical distance between the ball and the paddle. Take absolute value to avoid negatives or positives.
        shortest_vertical_distance_before_overlap = ball.radius + paddle.height/2. # This is the closest the ball and the paddle can get without colliding
        vertical_overlap = (vertical_distance < shortest_vertical_distance_before_overlap) # This is a boolean that is true if there's overlap vertically
        
        # If there's both horizontal vertical overlap, there's a collision
        collision_occurred = (horizontal_overlap and vertical_overlap)

        # Here we say what actually happens if there's a collision.
        if collision_occurred:
            
            # If a collision occured, we'll record which direction it was moving before hand
            direction_of_motion = ball.x_velocity/abs(ball.x_velocity)
            
            # We'll also completely revise how fast it's moving and at what angle
            angle = random(float(PI)/2.) - float(PI)/4.
            
            # Check what player hit the ball, based on the direction the ball approaches
            # When player 1 hits, the distance is greater than 0
            if (horizontal_displacement > 0):
                base_speed = self.game_parameters.ball_player1_speed
            elif (horizontal_displacement < 0):
                base_speed = self.game_parameters.ball_player2_speed
            speed = random(base_speed*0.5, base_speed*1.5)

            
            # Combine the above pieces of information to get the balls new velocity
            ball.x_velocity = -1.*direction_of_motion*speed*cos(angle)
            ball.y_velocity = speed*sin(angle)
            
            # Also, move the ball to the edge of the paddle, so as to avoid it getting stuck in the paddle
            ball.x_position = paddle.x_position + horizontal_displacement/horizontal_distance*(paddle.width/2. + ball.radius)
            
            # Add on to the number of volleys
            self.game_parameters.number_of_volleys += 1
            
    # Everything inside here says what happens when a ball hits the top or bottom wall
    def ball_vertical_wall_collision(self, ball):
        
        # First, we check if the ball ran into the top wall
        ball_above_top_wall = (ball.y_position < ball.radius)
        
        # Next we check if the ball ran into the bottom wall
        ball_below_bottom_wall = (ball.y_position > height - ball.radius)
        
        # If the ball was out of bounds on top or bottom, there was a collision with the wall
        collision_occurred = (ball_above_top_wall or ball_below_bottom_wall)
        
        # Here we say what actually happens if there's a collision.
        if collision_occurred:
            
            # If a collision occured, we'll reverse the vertical motion of the ball (i.e. just multiply by -1)
            ball.y_velocity *= -1.
            
    # Everything inside here says what happens when the ball hits a goal
    def ball_goal_collision(self, ball):
        
        # First, we check if the ball ran into player 1's or player 2's goal
        ball_in_player1_goal = (ball.x_position - ball.radius < self.game_parameters.goal_width)
        ball_in_player2_goal = (ball.x_position + ball.radius > width - self.game_parameters.goal_width)
        
        # In this section we say what happened if the ball ended up in player 1's goal
        if ball_in_player1_goal:
            
            # If the ball's in player 1's goal, we subtract one life from player 1's lives
            self.game_parameters.player1_lives -= 1
            
            # If the number of lives dips below 0 (and the game isn't over), mark the game as over and save the winner.
            if (self.game_parameters.player1_lives <= 0.) and (not self.game_parameters.game_finished):
                self.game_parameters.game_finished = True
                self.game_parameters.winner = self.game_parameters.player2_name
            
        # In this section we say what happened if the ball ended up in player 2's goal
        elif ball_in_player2_goal:
            
            # If the ball's in player 1's goal, we subtract one life from player 2's lives
            self.game_parameters.player2_lives -= 1     
            
            # If the number of lives dips below 0 (and the game isn't over), mark the game as over and save the winner.
            if (self.game_parameters.player2_lives <= 0.) and (not self.game_parameters.game_finished):
                self.game_parameters.game_finished = True
                self.game_parameters.winner = self.game_parameters.player1_name
            
        # If the ball ends up in either goal, we reset it to its original position, give it a random velocity, and reset the volley counter
        if (ball_in_player1_goal or ball_in_player2_goal):
            
            # Move the ball back to the center
            ball.x_position = width/2.
            ball.y_position = height/2.
            
            # Have the ball go off in a random direction
            angle = random(360.)
            ball.x_velocity = self.game_parameters.ball_default_speed*cos(angle)
            ball.y_velocity = self.game_parameters.ball_default_speed*sin(angle)
            
            # Reset the volley counter
            self.game_parameters.number_of_volleys = 0
            
    # Everything inside here says what happens when a paddle hits a wall
    def paddle_wall_collision(self, paddle):
        
        # First, we check if the paddle ran into the top wall
        paddle_above_top_wall = (paddle.y_position < paddle.height/2.)
        
        # Next we check if the ball ran into the bottom wall
        paddle_below_bottom_wall = (paddle.y_position > height - paddle.height/2.)
            
        # If the ball ran into the top wall, move it down so it's just up against the wall
        if paddle_above_top_wall:
            paddle.y_position = paddle.height/2.
            
        # If the ball ran into the bottom wall, move it up so it's just up against the wall
        if paddle_below_bottom_wall:
            paddle.y_position = height - paddle.height/2.