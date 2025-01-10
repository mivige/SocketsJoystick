# JoystickPantalla.py
import socket
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Joystick Emulator")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Point properties
POINT_SIZE = 10
MOVE_DISTANCE = 10

class Point:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.x = WINDOW_SIZE[0] // 2
        self.y = WINDOW_SIZE[1] // 2
    
    def move(self, direction):
        if direction == 'UP':
            self.y = max(POINT_SIZE, self.y - MOVE_DISTANCE)
        elif direction == 'DOWN':
            self.y = min(WINDOW_SIZE[1] - POINT_SIZE, self.y + MOVE_DISTANCE)
        elif direction == 'LEFT':
            self.x = max(POINT_SIZE, self.x - MOVE_DISTANCE)
        elif direction == 'RIGHT':
            self.x = min(WINDOW_SIZE[0] - POINT_SIZE, self.x + MOVE_DISTANCE)
    
    def draw(self, surface):
        pygame.draw.circle(surface, RED, (self.x, self.y), POINT_SIZE)

def main():
    # Create TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind socket to port
    server_address = ('0.0.0.0', 10000)  # Listen on all available interfaces
    print(f'Starting up on {server_address[0]}:{server_address[1]}')
    sock.bind(server_address)
    
    # Listen for incoming connections
    sock.listen(1)
    
    point = Point()
    clock = pygame.time.Clock()
    running = True
    
    while running:
        print('Waiting for a connection...')
        connection, client_address = sock.accept()
        
        try:
            print(f'Connection from {client_address}')
            
            while True:
                # Handle Pygame events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break
                
                # Set socket to non-blocking
                connection.setblocking(False)
                
                try:
                    data = connection.recv(16).decode()
                    
                    if data == 'QUIT':
                        running = False
                        break
                    
                    if data:
                        # Handle received command
                        if data == 'RESET':
                            point.reset()
                        else:
                            point.move(data)
                except BlockingIOError:
                    pass  # No data available
                
                # Update display
                screen.fill(BLACK)
                point.draw(screen)
                pygame.display.flip()
                
                # Control frame rate
                clock.tick(60)
                
        except Exception as e:
            print(f"Error: {e}")
        finally:
            connection.close()
            
    pygame.quit()
    sock.close()

if __name__ == '__main__':
    main()