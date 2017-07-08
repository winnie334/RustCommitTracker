from win32api import *
from win32gui import *
import win32con
import sys
import os
import time


class WindowsBalloonTip:
    def __init__(self, title, msg):
        message_map = {win32con.WM_DESTROY: self.OnDestroy, }
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = 'PythonTaskbar'
        wc.lpfnWndProc = message_map
        class_atom = RegisterClass(wc)
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow(class_atom, "Taskbar", style, 0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, 0,
                                 0, hinst, None)
        UpdateWindow(self.hwnd)
        icon_path_name = os.path.abspath(os.path.join(sys.path[0], 'resources/rust_icon.ico'))
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
            hicon = LoadImage(hinst, icon_path_name, win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
            hicon = LoadIcon(0, win32con.IDI_APPLICATION)
        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, 'Tooltip')
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(NIM_MODIFY,
                         (self.hwnd, 0, NIF_INFO, win32con.WM_USER + 20, hicon, 'Balloon Tooltip', msg, 200, title))
        time.sleep(5)
        DestroyWindow(self.hwnd)
        class_atom = UnregisterClass(class_atom, hinst)

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)


def balloon_tip(title, msg):
    w=WindowsBalloonTip(title, msg)
