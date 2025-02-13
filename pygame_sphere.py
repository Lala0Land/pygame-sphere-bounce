import pygame
import random

# Константы
WIDTH, HEIGHT = 800, 600
SPHERE_RADIUS = 200
BALL_RADIUS = 10
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Центральная сфера
sphere_center = (WIDTH // 2, HEIGHT // 2)
balls = []  # Список шариков

running = True
while running:
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (100, 100, 100), sphere_center, SPHERE_RADIUS, 2)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            # Проверка, что клик внутри сферы
            if (mx - sphere_center[0]) ** 2 + (my - sphere_center[1]) ** 2 <= SPHERE_RADIUS ** 2:
                color = random.choice(COLORS)
                speed_x = random.uniform(-3, 3)
                speed_y = random.uniform(-3, 3)
                balls.append({'pos': [mx, my], 'vel': [speed_x, speed_y], 'color': color})
    
    # Обновление позиций шариков и отражение от границ сферы
    for ball in balls:
        ball['pos'][0] += ball['vel'][0]
        ball['pos'][1] += ball['vel'][1]
        
        dx = ball['pos'][0] - sphere_center[0]
        dy = ball['pos'][1] - sphere_center[1]
        distance = (dx ** 2 + dy ** 2) ** 0.5
        
        if distance + BALL_RADIUS >= SPHERE_RADIUS:
            # Нормализация вектора движения
            norm_dx, norm_dy = dx / distance, dy / distance
            dot_product = ball['vel'][0] * norm_dx + ball['vel'][1] * norm_dy
            
            # Отражение скорости относительно нормали
            ball['vel'][0] -= 2 * dot_product * norm_dx
            ball['vel'][1] -= 2 * dot_product * norm_dy
            
            # Перемещаем шарик обратно внутрь сферы
            overlap = (distance + BALL_RADIUS) - SPHERE_RADIUS
            ball['pos'][0] -= overlap * norm_dx
            ball['pos'][1] -= overlap * norm_dy
        
        pygame.draw.circle(screen, ball['color'], (int(ball['pos'][0]), int(ball['pos'][1])), BALL_RADIUS)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
