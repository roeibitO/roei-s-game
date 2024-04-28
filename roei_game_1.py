import pygame
import random
import sys

def main():
    """ראשי הפונקציה להפעלת המשחק."""
    pygame.init()

    # הגדרת חלון התצוגה
    screen = pygame.display.set_mode([500, 500])
    pygame.display.set_caption('המשחק הכי טוב שלי!!!')

    # טעינת תמונת הרקע
    background_image = pygame.image.load("background_game.png").convert()
    background_image = pygame.transform.scale(background_image, (500, 500))
    # טעינת תמונת השחקן והאויב
    player = pygame.image.load('ship2.jpg')
    enemy_image = pygame.image.load('enemy.png')

    # הגדרת מיקום וממדי השחקן
    player_width = 50
    player_height = 51
    player_vel = 4  # מהירות גבוהה יותר לתנועה
    player_x = (500 - player_width) / 2
    player_y = 500 - player_height

    # רשימה לאותיות של אויבים
    enemies = []

    # פונקציה ליצירת אויב חדש
    def generate_enemy():
        enemy_width = 50
        enemy_height = 51
        enemy_x = random.randint(0, 500 - enemy_width)
        enemy_y = random.randint(-500, -enemy_height)  # יצירת אויב באקראי בחלק העליון של המסך
        enemies.append([enemy_x, enemy_y])

    # פונקציה להזזת האויבים למעלה
    def move_enemies():
        for enemy in enemies:
            enemy[1] += 3  # שינוי מיקום אנכי - ניתן לשנות את הערך כדי לשנות את המהירות

    # פונקציה לציור השחקן
    def draw_player():
        screen.blit(player, (player_x, player_y))

    # פונקציה לציור האויבים
    def draw_enemies():
        for enemy in enemies:
            enemy_x, enemy_y = enemy
            screen.blit(enemy_image, (enemy_x, enemy_y))

    clock = pygame.time.Clock()

    # Run until the user asks to quit
    running = True
    while running:
        screen.fill((0, 0, 0))  # מילוי צבע שחור למחיקת המסך
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_vel

        if keys[pygame.K_RIGHT] and player_x < 500 - player_width - player_vel:
            player_x += player_vel

        move_enemies()

        # יצירת אויבים חדשים
        if len(enemies) < 2:
            generate_enemy()

        # Move enemies upward
        for enemy in enemies:
            enemy[1] += 3  # Adjust this value to control enemy speed

        # יצירת אויבים חדשים כאשר שני האויבים האחרונים יוצאים מהתמונה
        if len(enemies) >= 2 and all(enemy[1] > 500 for enemy in enemies[-2:]):
            generate_enemy()
            generate_enemy()

        # בדיקת פגיעת השחקן באויב
        for enemy in enemies:
            if (enemy[0] <= player_x <= enemy[0] + player_width or
                    enemy[0] <= player_x + player_width <= enemy[0] + player_width) and \
                    (enemy[1] <= player_y <= enemy[1] + player_height or
                     enemy[1] <= player_y + player_height <= enemy[1] + player_height):
                pygame.quit()
                sys.exit()

        # הצגת תמונת הרקע
        screen.blit(background_image, (0, 0))

        # ציור השחקן
        draw_player()

        # ציור האויבים
        draw_enemies()

        pygame.display.flip()
        clock.tick(60)  # קביעת מהירות הפריים

    pygame.quit()

if __name__ == "__main__":
    main()
