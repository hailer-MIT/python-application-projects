import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake properties
SNAKE_SIZE = 20
SNAKE_SPEED = 5

# Snake class
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
    
    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= SNAKE_SPEED
        elif self.direction == "DOWN":
            y += SNAKE_SPEED
        elif self.direction == "LEFT":
            x -= SNAKE_SPEED
        elif self.direction == "RIGHT":
            x += SNAKE_SPEED
        self.body.insert(0, (x, y))
        self.body.pop()  # Remove the last segment of the snake's body
    
    def change_direction(self, new_direction):
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = new_direction
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = new_direction
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = new_direction
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = new_direction
    
    def draw(self):
        for segment in self.body:
            pygame.draw.rect(WIN, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

# Apple class
class Apple:
    def __init__(self):
        self.x = random.randint(0, WIDTH - SNAKE_SIZE)
        self.y = random.randint(0, HEIGHT - SNAKE_SIZE)
    
    def draw(self):
        pygame.draw.rect(WIN, RED, (self.x, self.y, SNAKE_SIZE, SNAKE_SIZE))

# Main function
def main():
    clock = pygame.time.Clock()
    snake = Snake()
    apple = Apple()

    running = True
    while running:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")
        
        snake.move()

        if snake.body[0][0] == apple.x and snake.body[0][1] == apple.y:
            apple = Apple()
        
        WIN.fill(BLACK)
        snake.draw()
        apple.draw()
        pygame.display.update()

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()