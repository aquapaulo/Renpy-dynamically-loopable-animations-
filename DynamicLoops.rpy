
## credit for the original code goes to anne O'nymous on f95 ##

##For this to work we'll have to create a screen that holds our animations.
# The line below dictates that the screen will require the exact duration of the scene and the animation's name.
screen loopingMovie( duration, myMovie ):

    default loop = True

    timer duration repeat True action If( loop is True, NullAction(), Return() )

    add myMovie

    # A 100% transparent button that covers all the screen and allows us to move forward in the animation
    imagebutton:
        xpos 0
        ypos 0
        xsize config.screen_width
        ysize config.screen_height
        idle Solid( "#00000000" )
        action SetScreenVariable( "loop", False )


#in here, we declare the animation sequences.
#I advise lower framerates than these or else the animation will pause and spring back into playing due to loading the next loop

image anim_A:

    "anim_frames/A/f1.png"
    0.1
    "anim_frames/A/f2.png"
    0.1
    "anim_frames/A/f3.png"
    0.1
    "anim_frames/A/f4.png"
    0.1
    "anim_frames/A/f5.png"
    0.1
    "anim_frames/A/f6.png"
    0.1
    "anim_frames/A/f7.png"
    0.1
    "anim_frames/A/f8.png"
    0.1
    "anim_frames/A/f9.png"
    0.1
    "anim_frames/A/f10.png"
    0.1
    "anim_frames/A/f11.png"
    0.1
    "anim_frames/A/f12.png"
    0.1
    "anim_frames/A/f13.png"
    0.1
    "anim_frames/A/f14.png"
    0.1
    "anim_frames/A/f15.png"
    0.1
    "anim_frames/A/f16.png"
    0.1
    "anim_frames/A/f17.png"
    0.1
    "anim_frames/A/f18.png"
    0.1
    "anim_frames/A/f19.png"
    0.1
    "anim_frames/A/f20.png"
    0.1
    #to help prevent frame-skipping we duplicate this final frame, we will not count its additional pause thus the duration is "2.0"
    "anim_frames/A/f20.png"
    0.1
    repeat

image anim_B:
    "anim_frames/B/f1.png"
    0.1
    "anim_frames/B/f2.png"
    0.1
    "anim_frames/B/f3.png"
    0.1
    "anim_frames/B/f4.png"
    0.1
    "anim_frames/B/f5.png"
    0.1
    "anim_frames/B/f6.png"
    0.1
    "anim_frames/B/f7.png"
    0.1
    "anim_frames/B/f8.png"
    0.1
    "anim_frames/B/f9.png"
    0.1
    "anim_frames/B/f10.png"
    0.1
    "anim_frames/B/f11.png"
    0.1
    "anim_frames/B/f12.png"
    0.1
    "anim_frames/B/f13.png"
    0.1
    "anim_frames/B/f14.png"
    0.1
    "anim_frames/B/f15.png"
    0.1
    "anim_frames/B/f16.png"
    0.1
    "anim_frames/B/f17.png"
    0.1
    "anim_frames/B/f18.png"
    0.1
    "anim_frames/B/f19.png"
    0.1
    "anim_frames/B/f20.png"
    0.1
    #to help prevent frame-skipping we duplicate this final frame, we will not count its additional pause thus the duration is "2.0"
    "anim_frames/B/f20.png"
    0.1
    repeat

image anim_C:

    "anim_frames/C/f1.png"
    0.1
    "anim_frames/C/f2.png"
    0.1
    "anim_frames/C/f3.png"
    0.1
    "anim_frames/C/f4.png"
    0.1
    "anim_frames/C/f5.png"
    0.1
    "anim_frames/C/f6.png"
    0.1
    "anim_frames/C/f7.png"
    0.1
    "anim_frames/C/f8.png"
    0.1
    "anim_frames/C/f9.png"
    0.1
    "anim_frames/C/f10.png"
    0.1
    "anim_frames/C/f11.png"
    0.1
    "anim_frames/C/f12.png"
    0.1
    "anim_frames/C/f13.png"
    0.1
    "anim_frames/C/f14.png"
    0.1
    "anim_frames/C/f15.png"
    0.1
    "anim_frames/C/f16.png"
    0.1
    "anim_frames/C/f17.png"
    0.1
    "anim_frames/C/f18.png"
    0.1
    "anim_frames/C/f19.png"
    0.1
    "anim_frames/C/f20.png"
    0.1
    #to help prevent frame-skipping we duplicate this final frame, we will not count its additional pause thus the duration is "2.0"
    "anim_frames/C/f20.png"
    0.1



image anim_B_to_looping_C:

    "anim_frames/B/f1.png"
    0.1
    "anim_frames/B/f2.png"
    0.1
    "anim_frames/B/f3.png"
    0.1
    "anim_frames/B/f4.png"
    0.1
    "anim_frames/B/f5.png"
    0.1
    "anim_frames/B/f6.png"
    0.1
    "anim_frames/B/f7.png"
    0.1
    "anim_frames/B/f8.png"
    0.1
    "anim_frames/B/f9.png"
    0.1
    "anim_frames/B/f10.png"
    0.1
    "anim_frames/B/f11.png"
    0.1
    "anim_frames/B/f12.png"
    0.1
    "anim_frames/B/f13.png"
    0.1
    "anim_frames/B/f14.png"
    0.1
    "anim_frames/B/f15.png"
    0.1
    "anim_frames/B/f16.png"
    0.1
    "anim_frames/B/f17.png"
    0.1
    "anim_frames/B/f18.png"
    0.1
    "anim_frames/B/f19.png"
    0.1
    "anim_frames/B/f20.png"
    0.1
    #this will now play the full "anim_B" loop once and then transition to a looping "anim_C"
    #the duration later will be as long as this block below, so "2.0".
    #this is just an example transition of course, the actual transition animation should be shorter.
    block:
        "anim_frames/C/f1.png"
        0.1
        "anim_frames/C/f2.png"
        0.1
        "anim_frames/C/f3.png"
        0.1
        "anim_frames/C/f4.png"
        0.1
        "anim_frames/C/f5.png"
        0.1
        "anim_frames/C/f6.png"
        0.1
        "anim_frames/C/f7.png"
        0.1
        "anim_frames/C/f8.png"
        0.1
        "anim_frames/C/f9.png"
        0.1
        "anim_frames/C/f10.png"
        0.1
        "anim_frames/C/f11.png"
        0.1
        "anim_frames/C/f12.png"
        0.1
        "anim_frames/C/f13.png"
        0.1
        "anim_frames/C/f14.png"
        0.1
        "anim_frames/C/f15.png"
        0.1
        "anim_frames/C/f16.png"
        0.1
        "anim_frames/C/f17.png"
        0.1
        "anim_frames/C/f18.png"
        0.1
        "anim_frames/C/f19.png"
        0.1
        "anim_frames/C/f20.png"
        0.1
        #to help prevent frame-skipping we duplicate this final frame, we will not count its additional pause thus the duration is "2.0"
        "anim_frames/C/f20.png"
        0.1
        repeat



label start:

label animationsection:
    show screen loopingMovie(2.0, "anim_A")
    "This loop, animation A, has the ball go from one point to the other. Click to have it continue."

    show screen loopingMovie(2.0, "anim_B")
    "This loop, animation B, behaves the same as the last loop. Click to have it continue."
    show screen loopingMovie(2.0, "anim_C")
    "This loop, animation C, stops at the end. Click to move on to the next example."
    show screen loopingMovie(2.0, "anim_B_to_looping_C")

    "This loop has animation B transition into animation C and loop C. Click to restart."
    jump animationsection


# The game starts here.
