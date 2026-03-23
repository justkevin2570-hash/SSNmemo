import sys
import socket
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt
from db import init_db, get_all_windows, create_window
from window import MemoWindow

_SINGLE_INSTANCE_PORT = 47391  # 임의의 고정 포트

_open_windows = []


def _make_tray_icon():
    pix = QPixmap(32, 32)
    pix.fill(Qt.transparent)
    p = QPainter(pix)
    p.setRenderHint(QPainter.Antialiasing)
    p.setBrush(QColor('#f7c948'))
    p.setPen(QColor('#c8a000'))
    p.drawRoundedRect(2, 2, 28, 28, 4, 4)
    p.setPen(QColor('#7a6000'))
    p.drawLine(7, 10, 25, 10)
    p.drawLine(7, 16, 25, 16)
    p.drawLine(7, 22, 18, 22)
    p.end()
    return QIcon(pix)


def new_window(offset_from=None):
    x, y = 130, 130
    if offset_from:
        pos = offset_from.pos()
        x, y = pos.x() + 30, pos.y() + 30
    wid = create_window(x=x, y=y)
    _launch_window(wid, x, y, 320, 400, collapsed=False)


def _launch_window(wid, x, y, width, height, collapsed, color=''):
    win = MemoWindow(window_id=wid, on_new=new_window)
    win.apply_state(x, y, width, height, collapsed, color)
    win.show()
    _open_windows.append(win)
    win.destroyed.connect(lambda _: _open_windows.remove(win) if win in _open_windows else None)


if __name__ == '__main__':
    # 중복 실행 방지: 이미 실행 중이면 조용히 종료
    _lock_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _lock_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
    try:
        _lock_sock.bind(('127.0.0.1', _SINGLE_INSTANCE_PORT))
    except OSError:
        sys.exit(0)

    init_db()
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    tray = QSystemTrayIcon(_make_tray_icon(), app)
    tray.setToolTip('서서니 메모')

    menu = QMenu()
    act_new  = QAction('새 메모')
    act_quit = QAction('종료')
    act_new.triggered.connect(lambda: new_window())
    act_quit.triggered.connect(app.quit)
    menu.addAction(act_new)
    menu.addSeparator()
    menu.addAction(act_quit)
    def _restore_all_windows():
        for w in get_all_windows():
            _launch_window(w['id'], w['x'], w['y'], w['width'], w['height'], bool(w['collapsed']), w.get('color', ''))
        if not _open_windows:
            new_window()

    def on_tray_activated(reason):
        if reason == QSystemTrayIcon.Trigger:  # 좌클릭
            if _open_windows:
                for win in _open_windows:
                    win.show()
                    win.raise_()
                    win.activateWindow()
            else:
                _restore_all_windows()

    tray.activated.connect(on_tray_activated)
    tray.setContextMenu(menu)
    tray.show()

    for w in get_all_windows():
        _launch_window(w['id'], w['x'], w['y'], w['width'], w['height'], bool(w['collapsed']), w.get('color', ''))

    sys.exit(app.exec_())
