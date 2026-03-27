# Chia công việc cho 4 người

## Person 1 — Core loop, state flow, player feel
**Phụ trách**
- `main.py`
- `src/game.py`
- `src/states/*`
- `src/entities/player.py`

**Deliverables**
- Vòng lặp game ổn định theo `deltaTime`
- Menu -> Play -> Game Over flow
- Input flap/thrust
- Trọng lực, cảm giác điều khiển, giới hạn trần/sàn
- Hoàn thiện animation state của player

## Person 2 — Background, parallax, visual pipeline
**Phụ trách**
- `src/environment/background.py`
- `assets/images/backgrounds/*`
- tích hợp sprite layer thực tế

**Deliverables**
- 3+ lớp background chạy vô hạn, không hở nền
- Tốc độ layer khác nhau đúng hiệu ứng parallax
- Có thể đổi theme nền dễ dàng
- Painter's algorithm / draw order rõ ràng

## Person 3 — Obstacles, collectibles, spawn system
**Phụ trách**
- `src/entities/obstacle.py`
- `src/entities/collectible.py`
- `src/environment/spawner.py`
- tuning trong `src/settings.py`

**Deliverables**
- Obstacle spawn procedural
- Gap random, vị trí random hợp lý
- Collectible spawn đi kèm obstacle
- Despawn / object pool nếu muốn nâng cấp
- Extension: dynamic obstacles

## Person 4 — Collision, score, difficulty, polish, README
**Phụ trách**
- `src/systems/collision.py`
- `src/systems/difficulty.py`
- `src/systems/particles.py`
- `src/ui/*`
- `README.md`

**Deliverables**
- Collision chính xác
- Score / best score / game over
- Extension: difficulty scaling
- Extension: particle effects
- README đầy đủ asset attribution + control manual + giải thích parallax

---

# Cách làm song song để ít đụng code
1. Chốt trước interface:
   - Player phải có: `update(dt)`, `draw(screen)`, `rect()`, `flap()`
   - ObstacleManager phải có: `spawn(...)`, `update(dt, scroll_speed)`, `draw(screen)`, `consume_passed(player_x)`
   - CollectibleManager phải có: `spawn(x, y)`, `update(dt, scroll_speed)`, `draw(screen)`
2. Mỗi người làm đúng module của mình, không sửa lung tung file người khác.
3. Gom code bằng pull request hoặc merge theo thứ tự:
   - Core + states
   - Background
   - Obstacles/collectibles
   - Collision/UI/polish
4. Cuối cùng cả nhóm cùng tuning gameplay.

# Mốc gợi ý
- Day 1: chạy được placeholder demo
- Day 2: thay asset thật + animation thật
- Day 3: polish + README + test presentation
