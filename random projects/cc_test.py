import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((1000, 700))
font = pygame.font.SysFont("Arial", 18)
large_font = pygame.font.SysFont("Arial", 36)
clock = pygame.time.Clock()

# --- Game State ---
cookies = 0
click_value = 1
auto_cps = 0
last_tick = pygame.time.get_ticks()
cookie_scale = 1.0
floating_texts = [] # List of [x, y, text, lifetime]

# --- Buildings: [Name, Base Cost, Base CpS, Owned, Current Mult] ---
buildings = [
    {"name": "Cursor", "cost": 15, "cps": 0.1, "owned": 0, "mult": 1},
    {"name": "Grandma", "cost": 100, "cps": 1, "owned": 0, "mult": 1},
    {"name": "Farm", "cost": 1100, "cps": 8, "owned": 0, "mult": 1},
    {"name": "Mine", "cost": 12000, "cps": 47, "owned": 0, "mult": 1},
    {"name": "Factory", "cost": 130000, "cps": 260, "owned": 0, "mult": 1},
    {"name": "Portal", "cost": 10**6, "cps": 10000, "owned": 0, "mult": 1},
    {"name": "Time Machine", "cost": 14 * 10**12, "cps": 65 * 10**6, "owned": 0, "mult": 1}
]

# --- Upgrades: [Name, Cost, Target Building Index, Requirement (Owned Amount)] ---
upgrades = [
    {"name": "Iron Cursors", "cost": 100, "target": 0, "req": 1, "bought": False},
    {"name": "Forwards from Grandma", "cost": 1000, "target": 1, "req": 1, "bought": False},
    {"name": "Sturdier Conveyor Belts", "cost": 1.3 * 10**6, "target": 4, "req": 1, "bought": False}
]

def update_cps():
    global auto_cps
    auto_cps = sum(b["owned"] * b["cps"] * b["mult"] for b in buildings)

running = True
while running:
    # 1. Logic & Particles
    now = pygame.time.get_ticks()
    if now - last_tick >= 1000:
        cookies += auto_cps
        last_tick = now
    
    if cookie_scale > 1.0: cookie_scale -= 0.05
    for text in floating_texts[:]:
        text[1] -= 2 # Float up
        text[3] -= 1 # Lifetime
        if text[3] <= 0: floating_texts.remove(text)

    screen.fill((25, 25, 30))
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Click Cookie
            if math.hypot(mx - 250, my - 350) < (100 * cookie_scale):
                cookies += click_value
                cookie_scale = 1.2
                floating_texts.append([mx, my, f"+{click_value}", 30])
            
            # Shop Logic (Right Panel)
            for i, b in enumerate(buildings):
                rect = pygame.Rect(700, 50 + (i * 60), 280, 50)
                if rect.collidepoint(mx, my) and cookies >= b["cost"]:
                    cookies -= b["cost"]
                    b["owned"] += 1
                    b["cost"] = int(b["cost"] * 1.15)
                    update_cps()
            
            # Upgrade Logic (Bottom Row)
            for i, u in enumerate(upgrades):
                rect = pygame.Rect(50 + (i * 160), 600, 150, 60)
                target_b = buildings[u["target"]]
                if not u["bought"] and target_b["owned"] >= u["req"]:
                    if rect.collidepoint(mx, my) and cookies >= u["cost"]:
                        cookies -= u["cost"]
                        u["bought"] = True
                        target_b["mult"] *= 2 # Standard upgrade doubles output
                        update_cps()

    # 2. Draw Cookie & Particles
    pygame.draw.circle(screen, (139, 69, 19), (250, 350), int(100 * cookie_scale))
    for x, y, txt, life in floating_texts:
        t_surf = font.render(txt, True, (255, 255, 255))
        t_surf.set_alpha(life * 8)
        screen.blit(t_surf, (x, y))

    # 3. UI Panels
    screen.blit(large_font.render(f"{int(cookies):,} Cookies", True, (255, 255, 255)), (50, 30))
    screen.blit(font.render(f"Cookies Per Second: {auto_cps:,.1f}", True, (255, 215, 0)), (50, 80))

    # Sidebar: Buildings
    pygame.draw.rect(screen, (40, 40, 45), (680, 0, 320, 700))
    for i, b in enumerate(buildings):
        rect = pygame.Rect(700, 50 + (i * 60), 280, 50)
        color = (100, 100, 110) if cookies >= b["cost"] else (50, 50, 55)
        pygame.draw.rect(screen, color, rect, border_radius=5)
        screen.blit(font.render(f"{b['name']} ({b['owned']})", True, (255, 255, 255)), (rect.x+10, rect.y+5))
        screen.blit(font.render(f"Cost: {b['cost']:,}", True, (255, 215, 0)), (rect.x+10, rect.y+25))

    # Bottom: Upgrades
    for i, u in enumerate(upgrades):
        if not u["bought"] and buildings[u["target"]]["owned"] >= u["req"]:
            rect = pygame.Rect(50 + (i * 160), 600, 150, 60)
            color = (0, 150, 0) if cookies >= u["cost"] else (80, 0, 0)
            pygame.draw.rect(screen, color, rect, border_radius=5)
            screen.blit(font.render(u["name"], True, (255, 255, 255)), (rect.x+5, rect.y+5))
            screen.blit(font.render(f"Cost: {u['cost']:,}", True, (255, 215, 0)), (rect.x+5, rect.y+30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()