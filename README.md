dc22funnybadge
==============

See http://youtu.be/8gDq2SKJC88 for an example.

Has two LED modes: gentle LED wave, and persistance mode. Persistance mode requires you to modify the mounting point so you can swing around

NB: You will probably short out the VCC to the ground plane when you drill a hole! You'll have to clear back the ground plane from around your
mounting hole.

The makeitrain.py file converts a file with 1's and 0's indicating the pattern to display. Must be 8 rows high (each LED is a row), can be any length
I think. E.g. to display a square:


    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    0 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    0 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 

