# Dino Dash

A Pac-Man style maze run in a purple ruin. I wrote this with my children, to teach them
how to make a simple game by prompting Claude. They supplied some of the artistic
details such as dino, eagle, cat, player shouting Yay every 10 coins! Their prompt is the first item in 
[original-prompt.md](original-prompt.md).

You can play the game on Netlify, it is good fun! You play a lone human. Slow dinosaurs
plod after you, cats hunt fast, and eagles fly straight over the walls. Mine
three relics to clear a level. There are seven levels, and each one is bigger
and faster than the last.

## Play it

| Where | Link |
| --- | --- |
| Netlify | https://pacman-dino-dash.netlify.app |

## Controls

| Input | Action |
| --- | --- |
| Arrow keys or `W` `A` `S` `D` | Run |
| `P` | Pause |
| `M` | Mute the music |
| Swipe the maze, or the on-screen pad | Run, on a phone |

## Rules

1. **Coins.** Every open tile holds a coin. Each coin scores 10 points.
2. **Yay.** Every tenth coin makes the runner jump, shout "Yay!", and score a
   50 point bonus. The shout uses the browser voice, and the `Voice` button
   turns it off.
3. **Relics.** Three strange shards sit in each maze. Stand on one to mine it.
   The gauge fills in under a second, and it drains if you step away.
4. **Powers.** Each relic pays one power, and the relic wears that power's
   colour. Every level hides one red **Smash** relic; the other two rotate
   through Scare, Freeze, Speed and Shield.

   | Power | Time | What it does |
   | --- | ---: | --- |
   | Smash | 8s | Touch an enemy and it is destroyed for the rest of the level. |
   | Freeze | 6s | Everything stops. A stopped enemy breaks apart if you run into it. |
   | Scare | 8s | They flee. A touch sends one back to its start, worth 200 points. |
   | Speed | 8s | You outrun everything except the eagles. |
   | Shield | 10s | A hit costs you nothing and sends the enemy home. |
5. **Exit.** Three relics clear the level. You do not have to sweep the coins.
6. **Lives.** You get three runners. A hit costs one runner and your power, and
   everybody returns to their starting tile.

## The enemies

| Enemy | Colour | Behaviour |
| --- | --- | --- |
| Dinosaur | Green | Slow, and it always takes the shortest path to you. Level one keeps one dawdler at half speed. |
| Cat | Pink | Fast, and it mistimes about one corner in three, taking the second best way. |
| Eagle | Cyan | Ignores the maze and flies straight at you, at middling speed. |

Dinosaurs walk the maze with a breadth-first distance field that is rebuilt
every frame from your tile, so they never lose your scent. Cats read the same
field but mistime corners. No enemy reverses on the spot, except that one which
has climbed away from you for three tiles turns round, so a wrong turn can never
trap it in a loop. Under Scare, every enemy reads the field backwards and
runs away, and touching one is worth 200 points.

## The levels

| Level | Maze | Dinosaurs | Cats | Eagles | Speed | Junctions |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 19 x 15 | 2 | 1 | 1 | 1.00 | 32% |
| 2 | 19 x 15 | 3 | 1 | 1 | 1.05 | 49% |
| 3 | 21 x 15 | 3 | 2 | 1 | 1.10 | 40% |
| 4 | 21 x 17 | 4 | 2 | 2 | 1.15 | 28% |
| 5 | 23 x 17 | 4 | 3 | 2 | 1.21 | 36% |
| 6 | 23 x 19 | 5 | 3 | 3 | 1.27 | 35% |
| 7 | 25 x 19 | 6 | 4 | 3 | 1.34 | 42% |

One dinosaur on level one moves at half speed. Junctions are the share of floor
tiles with three or four ways out, and later levels tighten the maze as well as
adding enemies.

The music speeds up with the level as well: the chiptune loop runs at
`128 + 7 x level` beats per minute.

## How it is built

One HTML file, no libraries, no build step.

- **Maze.** Three steps, all from a seed made of the level number, so a level
  is the same maze on every run. A recursive-backtracker carves a perfect maze,
  which is a tree of dead ends. Two passes then open interior walls that already
  touch two corridors, which is what makes the loops. Last the generator braids
  the board: every tile with one way out gets a second, preferring a wall with
  corridor on the far side so the cut closes a loop. No tunnel ends in a wall,
  so a chase always has a way out.
- **Movement.** Entities hold float tile coordinates. A turn is allowed inside
  a window around each tile centre, and the window is as wide as one frame of
  travel, so a fast runner never skips a junction.
- **Drawing.** Canvas 2D. The maze renders once to an offscreen canvas per
  level; runner, enemies, coins and relics draw each frame.
- **Sound.** Web Audio, written by hand. A square-wave arpeggio, a triangle
  bass, and a filtered noise hat run off a 25 ms lookahead scheduler over an
  A-minor vamp. Coins, mining, hits and fanfares are short oscillator blips.
