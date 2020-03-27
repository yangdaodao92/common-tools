import wx

app = wx.App()
window = wx.Frame(None, title="wxPython - www.yiibai.com", size=(2500, 1300), pos=(20, 20))

panel = wx.Panel(window)
label = wx.StaticText(panel, label="Hello World", pos=(100, 100))
window.Show(True)
app.MainLoop()
