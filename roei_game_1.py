import pygame
import random
import sys
from pygame import mixer

def main():
    """ראשי הפונקציה להפעלת המשחק."""
    pygame.init()

    # הגדרת חלון התצוגה
    screen = pygame.display.set_mode([500, 500])
    pygame.display.set_caption('המשחק הכי טוב שלי!!!')

    # טעינת תמונת הרקע
    background_image = pygame.image.load("background_game.png").convert()
    background_image = pygame.transform.scale(background_image, (500, 500))
    
    # טעינת תמונת סוף המשחק
    game_over_image = pygame.image.load("gameover.jpg").convert()
    game_over_image = pygame.transform.scale(game_over_image, (500, 500))
    
    # טעינת תמונת השחקן והאויב
    player = pygame.image.load('ship2.jpg')
    enemy_image = pygame.image.load('moonenemy.png')
    # טעינת תמונת היריות
    bullet_image = pygame.image.load('truebullet.png')

    mixer.music.load("sound.mp3")
    mixer.music.play(-1)

    shotsound = pygame.mixer.Sound("bulletssaund1.wav")
    kchow = pygame.mixer.Sound("kchow!.mp3")

    # הגדרת מיקום וממדי השחקן
    player_width = 50
    player_height = 51
    player_vel = 8  # מהירות גבוהה יותר לתנועה
    player_x = (500 - player_width) / 2
    player_y = 500 - player_height

    # רשימה של אויבים
    enemies = []

    # רשימה של יריות
    bullets = []

    # פונקציה ליצירת אויב חדש
    def generate_enemy():
        enemy_width = 50
        enemy_height = 51
        enemy_x = random.randint(0, 500 - enemy_width)
        enemy_y = random.randint(-500, -enemy_height)  # יצירת אויב באקראי בחלק העליון של המסך
        enemies.append([enemy_x, enemy_y])

    # פונקציה ליצירת יריות
    def fire_bullet():
        bullet_x = player_x + player_width / 2
        bullet_y = player_y
        bullets.append([bullet_x, bullet_y])

    # פונקציה להזזת האויבים למעלה
    def move_enemies():
        for enemy in enemies:
            enemy[1] += 3.5  # שינוי מיקום אנכי - ניתן לשנות את הערך כדי לשנות את המהירות

    # פונקציה להזזת היריות למעלה
    def move_bullets():
        for bullet in bullets:
            bullet[1] -= 5  # שינוי מיקום אנכי של היריה - ניתן לשנות את המהירות

    # פונקציה לציור השחקן
    def draw_player():
        screen.blit(player, (player_x, player_y))

    # פונקציה לציור האויבים
    def draw_enemies():
        for enemy in enemies:
            enemy_x, enemy_y = enemy
            screen.blit(enemy_image, (enemy_x, enemy_y))

    # פונקציה לציור היריות
    def draw_bullets():
        for bullet in bullets:
            bullet_x, bullet_y = bullet
            screen.blit(bullet_image, (bullet_x, bullet_y))

    clock = pygame.time.Clock()

    # Run until the user asks to quit
    running = True
    while running:
        screen.fill((0, 0, 0))  # מילוי צבע שחור למחיקת המסך
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    fire_bullet()
                    shotsound.play()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_vel

        if keys[pygame.K_RIGHT] and player_x < 500 - player_width - player_vel:
            player_x += player_vel

        move_enemies()
        move_bullets()

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
                running = False

        # בדיקת פגיעת יריות באויבים
        for bullet in bullets[:]:
            bullet_x, bullet_y = bullet
            for enemy in enemies[:]:
                enemy_x, enemy_y = enemy
                if (enemy_x <= bullet_x <= enemy_x + player_width or
                        enemy_x <= bullet_x + player_width <= enemy_x + player_width) and \
                        (enemy_y <= bullet_y <= enemy_y + player_height or
                         enemy_y <= bullet_y + player_height <= enemy_y + player_height):
                    bullets.remove(bullet)
                    kchow.play()
                    enemies.remove(enemy)
                    break

        # הצגת תמונת הרקע
        screen.blit(background_image, (0, 0))

        # ציור השחקן
        draw_player()

        # ציור האויבים
        draw_enemies()

        # ציור היריות
        draw_bullets()

        pygame.display.flip()
        clock.tick(60)  # קביעת מהירות הפריים

    # מציג את מסך ה-"Game Over"
    screen.blit(game_over_image, (0, 0))
    pygame.display.flip()

    # ממתין לשנייה לפני סגירת החלון
    pygame.time.wait(2000)

    pygame.quit()

if __name__ == "__main__":
    main()
