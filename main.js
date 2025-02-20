const { app, BrowserWindow } = require('electron');
const { spawn } = require('child_process');
const path = require('path');

let mainWindow;
let flaskServer;

app.whenReady().then(() => {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true, // Isolate contexts
        }
    });

    // Set the window icon after the window is created
    mainWindow.setIcon(path.join(__dirname, 'favicon.ico'));

    // Start Flask server using the Python executable
    const flaskPath = path.join(__dirname, 'xclipserver.py');
    flaskServer = spawn('python', [flaskPath], { stdio: 'inherit' });

    flaskServer.on('close', (code) => {
        console.log(`Flask server exited with code ${code}`);
    });

    flaskServer.on('error', (err) => {
        console.error("❌ Failed to start Flask server:", err);
    });

    // Fetch the local IP dynamically from the Flask server
    const isDev = !app.isPackaged;

    if (isDev) {
        mainWindow.loadURL('http://127.0.0.1:5000');  // Load from Flask in development
    } else {
        mainWindow.loadFile(path.join(__dirname, 'index.html')); // Load from local file in packaged app
    }

    // Kill Flask server on app exit
    app.on('window-all-closed', () => {
        if (flaskServer) flaskServer.kill(); // Kill Flask server on exit
        if (process.platform !== 'darwin') app.quit();
    });
});
