# Prompt 1 (me with help from my children for the details)

Make me a game in a webpage that is like Pacman but with the following alterations or features:

1. Instead of pacman let's do a human running away from slow dinosaurs
2. Make the background purple
3. Make 2 different enemies that is a cat and an eagle
4. there will be weird artifacts around the place and then if the person mine it they get a power up
5. every time we collect 10 coins the guy will jump and say Yay
6. want some simple music, chiptune
7. After we finish finding 3 of the artifacts then we will beat the level
8. There will be 6 or 7 levels and they get harder

Show me your thinking in the chat window as your development progresses.

Do the game in one shot, put it on the internet using a Claude artifact and Netlify if possible, format this README properly and include a link to the game on Claude Artifact and Netlify.

# Prompt 2 (from voice note)

Okay. This is a talking session where we tell you what's wrong with the game. So, uh, this is David here. And, uh, one thing is that the, um, is that the maze is one dimensional. Um, in the original Pacman, there were lots of different loops and things you could go around. Um, but in this one, almost all the time, it's almost one dimensional, um, bent into a two d shape. So we need to have lots of different options where you can go left or right. Also, there should be four, um, four enemies on the first level. So we should probably have two dinosaurs and the cats and the eagle on the first level. Um, also, if the, um, dinosaurs freeze, we also should be able to destroy them. So at the moment, if we walk into them, then they are. They kill us. But if they're frozen, um, we should kill them. Um, so... yeah. Any... anything else to add to this? Um, make one of the relics, uh, be able... like, we can... Yes. Like, destroy it. Destroy the relic. Okay. You mean the artifacts, aren't you? Yeah. Yeah. Okay. What do you think? Uh, I'm just really... should also get to go out of, um, because we shouldn't get trapped and -- Yeah. We should... it shouldn't be possible to get trapped down the end of a tunnel. Um, at the moment, you can. Um, Yeah. So just redesign the maze and let us have the option of, um, let us have the option of, um, destroying the dinosaurs if they are frozen. Um, that'll do for now. Okay. Wait. Wait. Wait. I have to also... maybe on, like, the first on, like, the first level, then, like, there will be one dinosaur. Unlike that dinosaur, only could get to go a little, like, slow. Like, slow. That's it. Thank you.

# Prompt 3 (fixes)
Make one more change to the game. If I press an arrow key that goes into the wall, my character must stop moving. also the yay is too loud, it's much louder than the music and sound effects, make it quieter.

# Prompt 4 (more fixes)
The previous instruction to stop if turning into a wall has produced a bug where sometimes the player stops and then cannot start again

I think it is stopping half way between two squares and that's what's breaking the movement

Fix it please. Arrow controls should be responsive when player is alive
