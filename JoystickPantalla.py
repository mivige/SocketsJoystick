# JoystickPantalla.py
import socket
import pygame
import sys

def get_local_ip():
    """Get the local IP address of the machine."""
    try:
        # Create a temporary socket to get local IP
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(('8.8.8.8', 80))
        local_ip = temp_socket.getsockname()[0]
        temp_socket.close()
        return local_ip
    except Exception:
        # Fallback method if the first method fails
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)

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
GRAY = (128, 128, 128)

# Point properties
POINT_SIZE = 10
MOVE_DISTANCE = 10

# Font setup
font = pygame.font.Font(None, 30)

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

def draw_text(surface, text, y_position):
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(WINDOW_SIZE[0]/2, y_position))
    surface.blit(text_surface, text_rect)

def main():
    # Get local IP address
    local_ip = get_local_ip()
    
    # Create TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind socket to port
    server_address = ('0.0.0.0', 10000)
    status_message = f'Server running on port {server_address[1]}'
    
    sock.bind(server_address)
    sock.listen(1)
    
    point = Point()
    clock = pygame.time.Clock()
    running = True
    connected = False
    
    while running:
        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update display
        screen.fill(BLACK)
        point.draw(screen)
        
        if not connected:
            # Accept connection (non-blocking)
            sock.setblocking(False)
            try:
                connection, client_address = sock.accept()
                connected = True
                status_message = f'Connected to: {client_address[0]}'
                connection.setblocking(False)
            except BlockingIOError:
                status_message = 'Waiting for connection...'
                # Display IP address when waiting
                status_message += f' Server IP: {local_ip}'
        else:
            try:
                data = connection.recv(16).decode()
                if data == 'QUIT':
                    connected = False
                    connection.close()
                elif data:
                    if data == 'RESET':
                        point.reset()
                    else:
                        point.move(data)
                    status_message = f'Received command: {data}'
            except BlockingIOError:
                pass
            except ConnectionResetError:
                connected = False
                status_message = 'Client disconnected'
                
        # Draw status messages
        draw_text(surface=screen, text=status_message, y_position=30)
        
        pygame.display.flip()
        clock.tick(60)
            
    pygame.quit()
    sock.close()

if __name__ == '__main__':
    main()