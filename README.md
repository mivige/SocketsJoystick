# 🎮 Joystick Emulator

**🚀 Built for:**  
*Computer Networks (Redes de Computadores) – University of the Balearic Islands (UIB)*  
📚 **Course Year:** 2024/25  
🧑‍💻 **Author:** Michele Vincenzo Gentile 

---

A network-based joystick emulator implemented using Python socket programming. This project consists of a server that displays the joystick position and a client that controls the movement using keyboard input.

---

## 🌟 Features

- 🕹️ Real-time joystick movement simulation
- 🌐 Client-server architecture using TCP/IP sockets
- 💻 Cross-computer compatibility with proper network configuration
- 🎨 Visual feedback with colored display
- 🖥️ Server available as both Python script and executable
- 📡 Automatic IP address display for easy connection
- 🛠️ Comprehensive error handling and timeout management

---

## 📋 Prerequisites

- Python 3.x
- Pygame library (`pip install pygame`)
- Windows operating system (uses `msvcrt` for keyboard input)
- Network connectivity between client and server computers

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mivige/SocketsJoystick.git
   ```
2. Install required dependencies:
   ```bash
   pip install pygame
   ```

---

## 🚀 Usage

### Server Setup (JoystickPantalla)

1. Run the server using either:
   - Python script: `python JoystickPantalla.py`
   - Executable: Run `JoystickPantalla.exe`
2. Note the IP address displayed on the server window.

### Client Setup (JoystickTeclado)

1. Open `JoystickTeclado.py` and update the `SERVER_IP_ADDRESS` on line 17 with the server's IP.
2. Run the client: `python JoystickTeclado.py`.

### Controls

- `W`: Move up
- `S`: Move down
- `A`: Move left
- `D`: Move right
- `R`: Reset position
- `Q`: Quit

---

## 📶 Network Configuration

### Troubleshooting

If connection fails:
1. Verify both computers are on the same network subnet.
2. Check Windows Firewall settings.
3. Ensure network profile is set to "Private".
4. Test basic connectivity using `ping`.
5. Verify the correct IP address is being used.

### Required Setup

1. Configure Windows Firewall:
   - Open Windows Defender Firewall with Advanced Security.
   - Create new Inbound Rule for TCP port 10000.
   - Allow the connection for all profiles.

2. Set Network Profile:
   - Open Windows Settings > Network & Internet.
   - Set network profile to "Private".

3. Verify Connection:
   - Both computers must be on the same network.
   - Test connectivity using `ping` command.
   - Ensure port 10000 is not blocked by network policy.

---

## 📁 Project Structure

```plaintext
SocketsJoystick/
├── src/
│   ├── JoystickPantalla.py    # Server implementation
│   └── JoystickTeclado.py     # Client implementation
├── executables/
│   └── JoystickPantalla.exe   # Server executable
└── README.md                  # This file
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

This project was developed as part of a Computer Networks course practice assignments at the University of the Balearic Islands.