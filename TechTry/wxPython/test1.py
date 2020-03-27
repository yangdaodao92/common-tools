import wx

class MainWindow(wx.Frame):

    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, wx.NewId(), 'Logging')

        self.log_window = wx.LogWindow(self, 'Log Window', show=True)

        box_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        show_log_button = wx.Button(self, wx.NewId(), 'Show Log')
        show_log_button.Bind(wx.EVT_BUTTON, self._show_log)

        log_message_button = wx.Button(self, wx.NewId(), 'Log Message')
        log_message_button.Bind(wx.EVT_BUTTON, self._log_message)

        box_sizer.AddMany((show_log_button, log_message_button))
        self.SetSizer(box_sizer)
        self.Fit()

        self.Bind(wx.EVT_CLOSE, self._on_close)

    def _show_log(self, event):
        self.log_window.Show()

    def _log_message(self, event):
        wx.LogError('New error messageaaaaaaaaaaaaa aaaaaaaaaa aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    def _on_close(self, event):
        self.log_window.Show(False)
        wx.Log.SetActiveTarget(None)
        event.Skip()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = MainWindow()
    dlg.Show()
    app.MainLoop()

app = wx.App()
frame = MainWindow(None).Show()
app.MainLoop()
