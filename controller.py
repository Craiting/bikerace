import wx
import wx.dataview as dv


class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)

        self.SetTitle('Control Form')
        self.size(600)
        self.Show(True)


def main():
    app = wx.App()
    windowClass(None)
    app.MainLoop()


main()
