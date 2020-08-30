# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [300,200]
    if direction == "RIGHT":
        ball_vel = [random.randrange(120, 240)/60, -random.randrange(60,180)/60]
    elif direction == "LEFT":
        ball_vel = [-random.randrange(120,240)/60, -random.randrange(60,180)/60]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score  # these are ints
    ball_pos = [300, 200]
    ball_vel = [0,0]
    paddle1_pos = (HEIGHT - PAD_HEIGHT)/2
    paddle2_pos = (HEIGHT - PAD_HEIGHT)/2
    paddle1_vel = 0
    paddle2_vel = 0
    score = [0,0]
    if LEFT:
        spawn_ball("LEFT")
    else:
        spawn_ball("RIGHT")
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_pos,paddle2_pos,LEFT
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,0.1,'White','White')
    
    # collison and reflection with top and bottom edge
    if ball_pos[1] >= HEIGHT - BALL_RADIUS or ball_pos[1] <= BALL_RADIUS:
         ball_vel[1] = -ball_vel[1]
            
    # collison and reflection with left and right gutters and ball coliison with paddle
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        
        if paddle1_pos < ball_pos[1] and ball_pos[1] < paddle1_pos + PAD_HEIGHT:
            ball_vel[0] = -1.1 * ball_vel[0]
        else:
            score[1] += 1
            spawn_ball("RIGHT")
            
    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        
        if paddle2_pos < ball_pos[1] and ball_pos[1] < paddle2_pos + PAD_HEIGHT:
            ball_vel[0] = -1.1 *ball_vel[0]
        else:
            score[0] += 1
            spawn_ball("LEFT")
            
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel > 0 and paddle1_pos + paddle1_vel <= HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if paddle2_pos + paddle2_vel > 0 and paddle2_pos + paddle2_vel <= HEIGHT -PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_line([PAD_WIDTH/2,paddle1_pos],[PAD_WIDTH/2,paddle1_pos+PAD_HEIGHT],PAD_WIDTH,'white')
    canvas.draw_line([WIDTH - PAD_WIDTH/2,paddle2_pos],[WIDTH - PAD_WIDTH/2,paddle2_pos+PAD_HEIGHT],PAD_WIDTH,'white')
    
    
    # draw scores
    canvas.draw_text(str(score[0]),(150,40),40,"Red")
    canvas.draw_text(str(score[1]),(400,40),40,"Red")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 3
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -3
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -3
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 3
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart',new_game,100)

# start frame
new_game()
frame.start()
