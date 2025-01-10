# JoystickTeclado.py
import socket
import sys
import msvcrt

def get_key():
    """Get a single keypress from stdin without blocking on Windows."""
    if msvcrt.kbhit():
        return msvcrt.getch().decode('utf-8').lower()
    return None

def main():
    # Create TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to server
    server_address = ('localhost', 10000)  # Replace with actual server IP
    print(f'Connecting to {server_address[0]}:{server_address[1]}')
    sock.connect(server_address)
    
    print("Controls:")
    print("W - Up")
    print("S - Down")
    print("A - Left")
    print("D - Right")
    print("R - Reset")
    print("Q - Quit")
    
    try:
        while True:
            key = get_key()
            if key:
                # Map keys to directions
                if key == 'w':  # Up
                    message = 'UP'
                elif key == 's':  # Down
                    message = 'DOWN'
                elif key == 'a':  # Left
                    message = 'LEFT'
                elif key == 'd':  # Right
                    message = 'RIGHT'
                elif key == 'r':  # Reset
                    message = 'RESET'
                elif key == 'q':  # Quit
                    message = 'QUIT'
                    sock.sendall(message.encode())
                    break
                else:
                    continue
                
                # Send message
                sock.sendall(message.encode())
                
    finally:
        sock.close()

if __name__ == '__main__':
    main()