from __future__ import annotations


def check_player_vs_obstacles(player, obstacles) -> bool:
    p_rect = player.rect()
    for obstacle in obstacles:
        if p_rect.colliderect(obstacle.top_rect()) or p_rect.colliderect(obstacle.bottom_rect()):
            return True
    return False


def check_player_vs_collectibles(player, collectibles) -> int:
    p_rect = player.rect()
    score = 0
    for item in collectibles:
        if item.active and p_rect.colliderect(item.rect()):
            item.active = False
            score += 1
    return score
