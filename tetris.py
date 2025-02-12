import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((200, 400))

# Tetromino-Formen
tetrominos = [
    [(1, 5), (0, 4), (0, 5), (0, 6)],  # T-Form
    [(1, 5), (0, 5), (0, 6), (1, 6)],  # Quadrat
    [(1, 4), (0, 4), (0, 5), (0, 6)],  # L-Form
    [(1, 6), (0, 4), (0, 5), (0, 6)],  # Spiegelverkehrtes L
    [(1, 5), (0, 4), (0, 5), (1, 6)],  # Z-Form
    [(1, 5), (0, 5), (0, 6), (1, 4)],  # S-Form
    [(0, 4), (0, 5), (1, 5), (1, 6)],  # J-Form
    [(1, 4), (1, 5), (1, 6), (1, 7)]   # I-Form
]

# Farben für Tetrominos
colors = [
    (255, 0, 0),  # Rot
    (0, 255, 0),  # Grün
    (0, 0, 255),  # Blau
    (255, 255, 0),# Gelb
    (255, 0, 255),# Magenta
    (0, 255, 255),# Cyan
    (255, 165, 0) # Orange
]

# Spielfeld (10x20)
grid = [[0] * 20 for _ in range(10)]
tetromino_color = random.choice(colors)

# Score-Variablen
score = 0
highscore = 0
font = pygame.font.Font(None, 30)  # Schriftart für die Anzeige

# Highscore aus Datei laden
try:
    with open("highscore.txt", "r") as f:
        highscore = int(f.read())
except:
    highscore = 0  # Falls die Datei nicht existiert

def is_valid_move(position, offset):
    """Prüft, ob eine Bewegung gültig ist."""
    for i in range(4):
        new_x = position[i][0] + offset[0]
        new_y = position[i][1] + offset[1]
        if new_y < 0: continue
        if new_y >= 20 or new_x >= 10 or new_x < 0: return False
        if grid[new_x][new_y]: return False
    return True

def rotate(tetromino):
    """Dreht ein Tetromino, falls möglich."""
    cx, cy = tetromino[0][0], tetromino[0][1]  # Mittelpunkt des Tetrominos
    new_position = [(cx + cy - tetromino[i][1], cy - cx + tetromino[i][0]) for i in range(4)]
    if is_valid_move(new_position, [0, 0]): return new_position
    return tetromino

def get_random_tetromino():
    """Gibt eine zufällige Tetromino-Form zurück."""
    return [pos[:] for pos in random.choice(tetrominos)]  # Kopie der Liste zurückgeben

def clear_full_rows():
    """Löscht volle Reihen und verschiebt die oberen Reihen nach unten."""
    global grid, score, highscore
    new_grid = [[0] * 20 for _ in range(10)]
    y_offset = 19
    rows_cleared = 0  # Zählt gelöschte Reihen

    for y in range(19, -1, -1):
        if 0 in [grid[x][y] for x in range(10)]:  
            for x in range(10):
                new_grid[x][y_offset] = grid[x][y]
            y_offset -= 1
        else:
            rows_cleared += 1  # Eine volle Reihe gefunden

    grid = new_grid
    score += rows_cleared * 100  # 100 Punkte pro Reihe
    if score > highscore:
        highscore = score  # Highscore aktualisieren

current_tetromino = get_random_tetromino()
movement_vector = [0, 1]

# Spiel-Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # Speichere den Highscore
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement_vector = [-1, 0]
            if event.key == pygame.K_RIGHT:
                movement_vector = [1, 0]
            if event.key == pygame.K_SPACE:
                current_tetromino = rotate(current_tetromino)
        else:
            movement_vector = [0, 1]

    # Kollision prüfen
    if not is_valid_move(current_tetromino, movement_vector):
        if movement_vector == [0, 1]:  # Falls nach unten blockiert -> fixiere das Tetromino
            for i in range(4):
                grid[current_tetromino[i][0]][current_tetromino[i][1]] = tetromino_color
            clear_full_rows()  # Volle Reihen löschen
            current_tetromino = get_random_tetromino()
            tetromino_color = random.choice(colors)
            if not is_valid_move(current_tetromino, [0, 0]):  # Falls kein Platz -> Game Over
                pygame.quit()
                # Speichere den Highscore
                with open("highscore.txt", "w") as f:
                    f.write(str(highscore))
                sys.exit()
        movement_vector = [0, 0]

    # Bildschirm leeren
    screen.fill(pygame.Color('black'))

    # Tetromino zeichnen
    for i in range(4):
        pygame.draw.rect(screen, tetromino_color, 
                         (current_tetromino[i][0] * 20, current_tetromino[i][1] * 20, 20, 20))

    # Tetromino bewegen
    current_tetromino = [(current_tetromino[i][0] + movement_vector[0], 
                          current_tetromino[i][1] + movement_vector[1]) for i in range(4)]

    # Spielfeld zeichnen
    for x in range(10):
        for y in range(20):
            if grid[x][y]:
                pygame.draw.rect(screen, grid[x][y], (x * 20, y * 20, 20, 20))

    # Score und Highscore anzeigen
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    highscore_text = font.render(f"Highscore: {highscore}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(highscore_text, (10, 30))

    pygame.display.flip()
    pygame.time.delay(200)
