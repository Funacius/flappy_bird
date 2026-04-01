# Infinite Flyer — Assignment 3
**Course:** Game Programming (SEM252)  
**Objective:** Master 2D Graphics, Parallax Scrolling, and Frame-based Animation.

## 🛠️ Tech Stack
- **Python 3.11+**
- **Pygame CE / Pygame**

## 🚀 Run
```bash
pip install -r requirements.txt
python main.py
```

## 🕹️ Controls
- **SPACE** / **Left Mouse**: Flap / Thrust upwards
- **R**: Restart when Game Over
- **ESC**: Quit application

---

## 🎮 Game Overview
**Infinite Flyer** is an endless side-scrolling survival game. The player controls a red plane navigating through procedurally generated obstacles while collecting coins. The game features a dynamic difficulty system that increases speed and obstacle frequency over time.

## 🧠 Technical Implementation

### 1. Parallax Scrolling System
The background consists of **3 distinct layers** moving at different relative speeds to create an illusion of depth:
*   **Layer 1 (Sky):** Moves at 15% of the base speed.
*   **Layer 2 (Mountains):** Moves at 35% of the base speed.
*   **Layer 3 (Ground):** Moves at 100% of the base speed, matching the obstacles.

**The Math:** 
To ensure seamless looping without gaps, each layer uses the **Modulo Operator (`%`)**. 
The horizontal offset is calculated as:
`self.offset = (self.offset + scroll_speed * relative_speed * dt) % image_width`
When drawing, the image is blitted twice (at `x = -offset` and `x = -offset + image_width`) to ensure that as one image leaves the screen, the next is already visible.

### 2. Frame-based Animation
Animations are decoupled from the application's frame rate using `deltaTime`. The `Animation` class tracks a `time_accumulator`. When the accumulator exceeds the `1 / FPS` threshold, the frame index increments. This ensures the plane flaps at the same speed regardless of whether the game is running at 30 FPS or 144 FPS.

### 3. Memory Management (Object Pooling)
To optimize performance and prevent frequent memory allocation/garbage collection, the game utilizes an **Object Pool** for obstacles and collectibles. 
*   When an entity moves off-screen to the left, it is not deleted. Instead, it is **released** back into the pool.
*   When a new entity needs to spawn on the right, it is **acquired** from the pool and reset with new coordinates.

## ✨ Implemented Extensions
1.  **Dynamic Obstacles:** Obstacles move vertically using a Sine wave function (`math.sin(phase)`) to create a challenging "moving gate" effect.
2.  **Difficulty Scaling:** The game tracks elapsed time; every 12 seconds, the "Level" increases, which raises the `scroll_speed` and decreases the `spawn_interval`.
3.  **Particle Systems:** A custom particle engine emits "exhaust" particles whenever the player flaps, providing visual feedback for player input.

## 📂 Folder Map
- `src/core`: Engine-level helpers, Object Pool, and Base Entity.
- `src/states`: Menu, Play, and Game Over state logic.
- `src/entities`: Player, Obstacle, and Collectible logic.
- `src/environment`: Parallax background and procedural spawner.
- `src/systems`: Animation, Collision, Difficulty, and Particles.
- `src/ui`: HUD and text rendering.
- `assets/images`: Sprite sheets and background textures.

## 🎨 Asset Attribution
*   **Player & Obstacles:** "Tappy Plane" by [Kenney.nl](https://kenney.nl/assets/tappy-plane) (CC0).
*   **Background Layers:** "Background Elements" by [Kenney.nl](https://kenney.nl/assets/background-elements) (CC0).
*   **Collectibles:** "Spinning Coin" by [thepeeps191](https://thepeeps191.itch.io/spinning-coin) (itch.io).
*   **Sound Effects:**  "Modern Technology select" from [mixkit](https://mixkit.co/free-sound-effects/click/).
                        "swoosh 4" by [Makoto-AE](https://pixabay.com/sound-effects/film-special-effects-swoosh-4-359828/).
                        "Pixel" by [Robloxuer](https://pixabay.com/music/video-games-pixel-245147/).
                        "Coins" by [SoundReality](https://pixabay.com/sound-effects/film-special-effects-coins-135571/).
