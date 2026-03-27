# Infinite Flyer — Python/Pygame Skeleton

Project skeleton for the **Infinite Flyer** assignment:
- parallax scrolling
- frame-based animation with `deltaTime`
- procedural obstacle / collectible spawning
- collision detection and game over
- extensions: difficulty scaling, dynamic obstacles, particle effects

## Tech stack
- Python 3.11+
- Pygame CE / Pygame

## Run
```bash
pip install -r requirements.txt
python main.py
```

## Current controls
- **SPACE** / **Left Mouse**: flap
- **R**: restart when game over
- **ESC**: quit

## Folder map
- `src/core`: engine-level helpers, loop, config
- `src/states`: menu / play / game over states
- `src/entities`: player, obstacles, collectibles
- `src/environment`: parallax background, spawner
- `src/systems`: animation, collision, difficulty, particles
- `src/ui`: HUD and overlay rendering
- `assets`: art / sound / fonts (currently placeholder)

## Suggested next steps
1. Replace placeholder rectangles/circles with spritesheets and art assets.
2. Implement exact frame extraction from spritesheets in `systems/animation.py`.
3. Add sound effects and polish.
4. Tune spawn balance and difficulty curve.
