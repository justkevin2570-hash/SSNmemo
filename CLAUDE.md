# Project Context: Tmemo (Electron + SQLite)

## 1. Core Concept
- A Windows-based lightweight sticky note application similar to "Simple Sticky Notes".
- Focused on quick memo-taking for high school administrative tasks and math research (Yuja-pi).

## 2. Key Features & Constraints
- **Window Shade (Roll-up):** Double-clicking the custom title bar must collapse the window to only show the title bar (approx. 40px height) and hide the content area. Double-clicking again restores the original size.
- **Always on Top:** A toggle feature to keep the memo window above all other windows (essential for multitasking with Excel/NEIS).
- **Frameless UI:** Use `frame: false` in Electron to implement a custom, draggable title bar.
- **Offline First:** Use SQLite for local data persistence. Ensure the app works perfectly without an internet connection.
- **Visuals:** Support transparency/opacity control and pastel-colored backgrounds like real sticky notes.

## 3. Tech Stack Specifics
- **Runtime:** Electron (Main process + Renderer process)
- **Frontend:** Vanilla HTML, CSS, and JavaScript (No heavy frameworks for maximum lightness).
- **Database:** SQLite (via `sqlite3` or `better-sqlite3` node modules).
- **Communication:** Use `contextBridge` and `ipcMain/ipcRenderer` for secure communication.

## 4. Coding Style & Rules
- Keep the code modular: Separate DB logic, IPC handling, and UI rendering.
- UI should be clean and "distraction-free".
- When implementing the 'Window Shade' feature, ensure `-webkit-app-region: drag` does not block `dblclick` events on the title bar.
- Ensure the window position and size (including collapsed state) are saved in the DB so they persist after restarting the app.

## 5. Future Roadmap
- Later transition to a sync-enabled online mode (Login system), but keep the current focus on local SQLite performance.
