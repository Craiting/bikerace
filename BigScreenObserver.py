import wx
import wx.dataview as dv
import thread

from Observer import Observer


class BigScreenObserver(Observer):

    def __init__(self, name):
        super(BigScreenObserver, self).__init__(name)
        try:
            thread.start_new_thread(main, ())
        except Exception as e:
            print "Error: unable to start thread", e


class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)

        self.SetTitle('Control Form')
        self.Show(True)

def main():
    app = wx.App()
    windowClass(None)
    app.MainLoop()
