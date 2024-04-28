import pygame
import random

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('My great game !!!')

background_image = pygame.image.load("background_game.png").convert()
background_image = pygame.transform.scale(background_image, (500, 500))
player = pygame.image.load('ship2.jpg')
enemy_image = pygame.image.load('enemy.png')

# Set initial position and dimensions of the player
player_width = 50
player_height = 51
player_vel = 0.5  # Increased velocity for faster movement
player_x = (500 - player_width) / 2
player_y = 500 - player_height

# Create a list to store enemy positions
enemies = []

# Variable to control enemy generation
create_enemy = True

# Run until the user asks to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate new enemy
    if create_enemy:
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
    player_vel = 0.5  # מהירות גבוהה יותר לתנועה
    player_x = (500 - player_width) / 2
    player_y = 500 - player_height

    # רשימה לאותיות של אויבים
    enemies = []

    # פונקציה ליצירת אויב חדש
    def generate_enemy():
        enemy_width = 50
        enemy_height = 51
        enemy_x = random.randint(0, 500 - enemy_width)
        enemy_y = 0 - enemy_height
        enemies.append([enemy_x, enemy_y])
        create_enemy = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel

    if keys[pygame.K_RIGHT] and player_x < 500 - player_width - player_vel:
        player_x += player_vel
    # פונקציה להזזת האויבים למעלה
    def move_enemies():
        for enemy in enemies:
            enemy[1] += 0.3  # שינוי מיקום אנכי - ניתן לשנות את הערך כדי לשנות את המהירות

    # פונקציה לציור השחקן
    def draw_player():
        pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_width, player_height))
        screen.blit(player, (player_x, player_y))

    # פונקציה לציור האויבים
    def draw_enemies():
        for enemy in enemies:
            enemy_x, enemy_y = enemy
            screen.blit(enemy_image, (enemy_x, enemy_y))

    # פונקציה ליצירת שני אויבים חדשים כאשר שני האויבים יוצאים מהמסך
    def create_new_enemies():
        if all(enemy[1] > 500 for enemy in enemies):
            for _ in range(2):  # יצירת שני אויבים חדשים
                generate_enemy()

    # ריצה עד שהמשתמש יבקש לסיים
    running = True
    while running:
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
        create_new_enemies()

    # Move enemies upward
    for enemy in enemies:
        enemy[1] += 0.3  # Adjust this value to control enemy speed
        # הצגת תמונת הרקע
        screen.blit(background_image, (0, 0))

    # Blit the background image to the screen
    screen.blit(background_image, (0, 0))
        # ציור השחקן
        draw_player()

    # Draw the player
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_width, player_height))
    screen.blit(player, (player_x, player_y))
        # ציור האויבים
        draw_enemies()

    # Draw enemies
    for enemy in enemies:
        enemy_x, enemy_y = enemy
        screen.blit(enemy_image, (enemy_x, enemy_y))
        pygame.display.flip()

    pygame.display.flip()
    pygame.quit()

pygame.quit()
if __name__ == "__main__":
    main()