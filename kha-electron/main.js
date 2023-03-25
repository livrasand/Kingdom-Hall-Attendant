const { app, BrowserWindow } = require('electron');
const remoteMain = require("@electron/remote/main");

let mainWindow;

const createWindow = () => {
  mainWindow = new BrowserWindow({
    width: 1080,
    height: 920,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    }
  });
  mainWindow.loadFile('src/index.html');
  mainWindow.setTitle('Kingdom Hall Attendant');
  // mainWindow.webContents.openDevTools();
  remoteMain.enable(mainWindow.webContents);
}

app.whenReady().then(() => {
  createWindow();
  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit();
});
