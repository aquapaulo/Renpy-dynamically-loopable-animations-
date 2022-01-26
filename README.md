# Renpy dynamically loopable animations 
Allows Renpy to wait for an animation loop to be over before advancing to the next one - Seamless Loop Transitions!

This is specially useful for adult animations if you want to replicate how other engines allow the loop to seamlessly transition to another loop.

Original code credit goes to anne O'nymous on f95:
https://f95zone.to/threads/is-it-possible-to-tell-renpy-to-stop-a-looped-video-and-move-to-a-different-video-only-at-the-end-of-the-video-thats-beeing-looped.84078/


This page includes the code, examples on how to use it and the animation frames you'll need to execute the example.
You must place the folder "animation frames" into the "images" folder.

The animation frames were rendered out in 1080p and contain a sphere moving from point A to B then to C. I suggest creating a new project at 1080p and testing it out to see if it works correctly.

# disadvantages and bugs 
This code has some bugs, such as sometimes it showing the first frame of the loop before advancing to the next animation loop.
It's a pretty intensive piece of code too so if you're doing this at 1080p it may cause renpy to pause for half a second and load in the next loop's images.
Not advisable to use on low end PC aimed projects, at too big a resolution or framerate, and I'd presume to be careful with it on mobile?

It could also be the images I utilized went straight from Blender to renpy so they're quite uncompressed.
Idunno, I took a month to finally find a way for this to work and caught a cold in the process so I'm dead tired lol
