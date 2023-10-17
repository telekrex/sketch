# Draw This
First Edition (June 2023)

## About
I originally created this game to be printed on paper and the players use dice to decide the drawing prompt. Since I used Python to test it when I was settling on the design, I've since decided to clean it up and upload it, maybe someone will think it's fun. The following is the instructions, translated from the print-out version to virtual. You'll have to run it as a Python script, I didn't think packaging was necessary.

## Setup
1. Download & install Python, no third party libraries or modules needed
2. Clone or download this repository
3. Open a terminal

## How it works:
Number of players: **1+**  
Objective: **Generate an idea, then try to draw it!**

An idea will be a combination of a **subject(s)**, a **modifier**, **an action**, and an **environment**.

The `/contents` folder contains files with lists of possibilities. There's a ton of content already here, but I encourage you to add more of your own. Just be sure to go along with the example content's format and use case. If you're unsure, think like this:

- *Subject(s)* will be a character, a thing, or idea.
- *Modifiers* will describe the subject; sometimes physical, sometimes a trait, sometimes a mood.
- *Actions* will be something for your subject to be doing.
- *Environments* [self explanatory] are the surroundings for your subject to be in.

## Play
To generate an idea, run the file `draw-this.py` in a terminal of your choice. The script will print an idea for you in the terminal, now try to draw it!

Sometimes the generated idea won't make sense - that's okay. It's up to you to get creative and make it happen.