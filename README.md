
# Push Clip

Push Clip is an Electron app that integrates with a Flask server to enable clipboard management. It allows you to view and update clipboard content seamlessly, both locally and across devices (including mobile or VMs) via the local network.

## Features

- View the current clipboard content from your device.
- Update the clipboard content remotely via the app.
- Fetch the local IP dynamically, allowing remote updates on mobile devices or VMs connected to the same local network.

## Dependencies

### Node.js (Electron app):
- **Electron**: For creating the desktop application interface.
- **Child Process**: Used for spawning the Flask server.
- **Path**: Path management to handle file paths for bundled files.

### Python (Flask Server):
- **Flask**: Web framework for creating the server.
- **pyperclip**: Used to interact with the system clipboard.
- **Flask-CORS**: Enables Cross-Origin Resource Sharing for mobile/VM access.
- **Socket**: To fetch the local IP address dynamically.

## Installation

### 1. Clone the repository:

bash
git clone https://github.com/yourusername/pushclip.git
cd pushclip


### 2. Install Node.js dependencies:

Make sure you have [Node.js](https://nodejs.org/) installed. Then install the required packages:

bash
npm install


### 3. Install Python dependencies:

Ensure you have [Python](https://www.python.org/downloads/) installed. Then, install the required Python packages:

bash
pip install flask pyperclip flask-cors


### 4. Start the application:

For development mode, simply run:

bash
npm start


This command will start the Flask server and the Electron app. You can access the app on your local machine at http://127.0.0.1:5000.

### 5. Update clipboard remotely:

Once the app is running, you can use the **local IP address** of your machine to update the clipboard remotely on any mobile device or VM on the same network.

To find the local IP address dynamically (which the app uses), go to the Settings page in the app or use the command below in the terminal:

bash
python -c "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.settimeout(0); s.connect(('10.254.254.254', 1)); print(s.getsockname()[0])"


Then, on your mobile device or VM, open the app and input the **local IP address** along with port 5000 to update the clipboard remotely.

## Development

If you're actively developing or modifying the app, you can run it in development mode by using:

bash
npm run dev


This will run the app locally with live-reloading for easier development.

## License

MIT License


This README file covers all aspects of the project, from installation to remote clipboard management, and includes instructions for developers.

