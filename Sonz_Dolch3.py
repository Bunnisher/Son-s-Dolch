import pygame
import random

# Initialize pygame
pygame.init()

# Set up the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dolch Sight Word Flashcards")

# Set up fonts
font = pygame.font.SysFont("Arial", 100, bold=True)
small_font = pygame.font.SysFont("Arial", 30)

# Load Dolch sight words from file
with open("school3.txt") as f:
    words = [line.strip() for line in f]

# Initialize the current word and color
current_word = random.choice(words)
current_color = (random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255))
bg_color = (random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255))

# Initialize the score and incorrect words
score = {
    "correct": 0,
    "wrong": 0
}
incorrect_words = set()

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Save incorrect words to file before quitting
            with open("needs_work.txt", "w") as f:
                f.writelines([f"{word}\n" for word in sorted(incorrect_words)])
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_word = random.choice(words)
                # Calculate random color for word and background
                current_color = (random.randint(0, 255), random.randint(
                    0, 255), random.randint(0, 255))
                bg_color = (random.randint(0, 255), random.randint(
                    0, 255), random.randint(0, 255))
            elif event.key == pygame.K_UP:
                score["correct"] += 1
            elif event.key == pygame.K_DOWN:
                score["wrong"] += 1
                incorrect_words.add(current_word.lower())

    # Draw the screen
    screen.fill(bg_color)
    word_surface = font.render(current_word.lower(), True, current_color)
    word_rect = word_surface.get_rect(
        center=(screen_width//2, screen_height//2))
    screen.blit(word_surface, word_rect)
    score_surface = small_font.render(
        f"Correct: {score['correct']}   Wrong: {score['wrong']}", True, (255, 255, 255))
    score_rect = score_surface.get_rect(topright=(screen_width-10, 10))
    screen.blit(score_surface, score_rect)
    pygame.display.update()

# Clean up
pygame.quit()
