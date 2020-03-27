import wx
import wx.xrc
import time
from threading import Thread
from wx.lib.pubsub import pub
import os

# def sss(bs_index, ip, log_out):
#     pub.sendMessage('update', bs_index=bs_index, ip=ip, log_out=log_out)
#
#
# # 新线程执行的代码:
# def loop():
#     n = 0
#     while n < 5:
#         n = n+1
#         time.sleep(3)
#         wx.CallAfter(sss, 1, 'ip' + str(n), 'logout' + str(n))
#         print(n)
#         # wx.CallAfter(Publisher.sendMessage, 'update', 2, str('ip' + str(n)), 'logout' + str(n))
#         # wx.CallAfter(Publisher.sendMessage, 'update', 3, str('ip' + str(n)), 'logout' + str(n))
#         # wx.CallAfter(Publisher.sendMessage, 'update', 4, str('ip' + str(n)), 'logout' + str(n))
class TestThread(Thread):
    """Test Worker Thread Class."""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.start()  # start the thread

    # ----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        for i in range(6):
            time.sleep(3)
            wx.CallAfter(self.postTime, bs_index=1, ip='ip' + str(i), log_out='logout' + str(i))
        time.sleep(2)
        wx.CallAfter(pub.sendMessage, "update", bs_index=1, ip='end', log_out='end')

    # ----------------------------------------------------------------------
    def postTime(self, bs_index, ip, log_out):
        pub.sendMessage("update", bs_index=bs_index, ip=ip, log_out=log_out)

project_name = ['gcj_customer_service', 'gcj_cstm_task_manager', 'member_center_bg', 'member_center_api', 'gcw_master_site']

# 替换文件的窗口
class ReplaceFileFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1000, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(223, 223, 223))

        replaceBsWrapper = wx.BoxSizer(wx.VERTICAL)

        replaceBs1 = wx.BoxSizer(wx.HORIZONTAL)
        replaceBs1.SetMinSize(wx.Size(-1, 20))
        self.replaceFileName1 = wx.StaticText(self, wx.ID_ANY, 'replaceFileName1', wx.DefaultPosition, wx.DefaultSize, 0)
        self.replaceFileName1.Wrap(-1)
        self.replaceFileName1.SetMinSize(wx.Size(260, -1))
        replaceBs1.Add(self.replaceFileName1, 0, wx.ALL, 5)
        self.replaceFilePath1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(800, -1), 0)
        replaceBs1.Add(self.replaceFilePath1, 0, wx.ALL, 5)
        replaceBsWrapper.Add(replaceBs1, 1, wx.EXPAND, 5)

        replaceBs2 = wx.BoxSizer(wx.HORIZONTAL)
        replaceBs2.SetMinSize(wx.Size(-1, 20))
        self.replaceFileName2 = wx.StaticText(self, wx.ID_ANY, 'replaceFileName1', wx.DefaultPosition, wx.DefaultSize, 0)
        self.replaceFileName2.Wrap(-1)
        self.replaceFileName2.SetMinSize(wx.Size(260, -1))
        replaceBs2.Add(self.replaceFileName2, 0, wx.ALL, 5)
        self.replaceFilePath2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(800, -1), 0)
        replaceBs2.Add(self.replaceFilePath2, 0, wx.ALL, 5)
        replaceBsWrapper.Add(replaceBs2, 1, wx.EXPAND, 5)

        replaceBs3 = wx.BoxSizer(wx.HORIZONTAL)
        replaceBs3.SetMinSize(wx.Size(-1, 20))
        self.replaceFileName3 = wx.StaticText(self, wx.ID_ANY, 'replaceFileName1', wx.DefaultPosition, wx.DefaultSize, 0)
        self.replaceFileName3.Wrap(-1)
        self.replaceFileName3.SetMinSize(wx.Size(260, -1))
        replaceBs3.Add(self.replaceFileName3, 0, wx.ALL, 5)
        self.replaceFilePath3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(800, -1), 0)
        replaceBs3.Add(self.replaceFilePath3, 0, wx.ALL, 5)
        replaceBsWrapper.Add(replaceBs3, 1, wx.EXPAND, 5)

        replaceBs4 = wx.BoxSizer(wx.HORIZONTAL)
        replaceBs4.SetMinSize(wx.Size(-1, 20))
        self.replaceFileName4 = wx.StaticText(self, wx.ID_ANY, 'replaceFileName1', wx.DefaultPosition, wx.DefaultSize, 0)
        self.replaceFileName4.Wrap(-1)
        self.replaceFileName4.SetMinSize(wx.Size(260, -1))
        replaceBs4.Add(self.replaceFileName4, 0, wx.ALL, 5)
        self.replaceFilePath4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(800, -1), 0)
        replaceBs4.Add(self.replaceFilePath4, 0, wx.ALL, 5)
        replaceBsWrapper.Add(replaceBs4, 1, wx.EXPAND, 5)

        replaceBs5 = wx.BoxSizer(wx.HORIZONTAL)
        replaceBs5.SetMinSize(wx.Size(-1, 20))
        self.replaceFileName5 = wx.StaticText(self, wx.ID_ANY, 'replaceFileName1', wx.DefaultPosition, wx.DefaultSize, 0)
        self.replaceFileName5.Wrap(-1)
        self.replaceFileName5.SetMinSize(wx.Size(260, -1))
        replaceBs5.Add(self.replaceFileName5, 0, wx.ALL, 5)
        self.replaceFilePath5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(800, -1), 0)
        replaceBs5.Add(self.replaceFilePath5, 0, wx.ALL, 5)
        replaceBsWrapper.Add(replaceBs5, 1, wx.EXPAND, 5)

        replaceBs6 = wx.BoxSizer(wx.HORIZONTAL)
        replaceBs6.SetMinSize(wx.Size(-1, 20))
        self.replaceFileName6 = wx.StaticText(self, wx.ID_ANY, 'replaceFileName1', wx.DefaultPosition, wx.DefaultSize, 0)
        self.replaceFileName6.Wrap(-1)
        self.replaceFileName6.SetMinSize(wx.Size(260, -1))
        replaceBs6.Add(self.replaceFileName6, 0, wx.ALL, 5)
        self.replaceFilePath6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(800, -1), 0)
        replaceBs6.Add(self.replaceFilePath6, 0, wx.ALL, 5)
        replaceBsWrapper.Add(replaceBs6, 1, wx.EXPAND, 5)

        replaceBs7 = wx.BoxSizer(wx.HORIZONTAL)
        replaceBs7.SetMinSize(wx.Size(-1, 20))
        self.replaceFileName7 = wx.StaticText(self, wx.ID_ANY, 'replaceFileName1', wx.DefaultPosition, wx.DefaultSize, 0)
        self.replaceFileName7.Wrap(-1)
        self.replaceFileName7.SetMinSize(wx.Size(260, -1))
        replaceBs7.Add(self.replaceFileName7, 0, wx.ALL, 5)
        self.replaceFilePath7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(800, -1), 0)
        replaceBs7.Add(self.replaceFilePath7, 0, wx.ALL, 5)
        replaceBsWrapper.Add(replaceBs7, 1, wx.EXPAND, 5)

        replaceBs8 = wx.BoxSizer(wx.HORIZONTAL)
        replaceBs8.SetMinSize(wx.Size(-1, 20))
        self.replaceFileName8 = wx.StaticText(self, wx.ID_ANY, 'replaceFileName1', wx.DefaultPosition, wx.DefaultSize, 0)
        self.replaceFileName8.Wrap(-1)
        self.replaceFileName8.SetMinSize(wx.Size(260, -1))
        replaceBs8.Add(self.replaceFileName8, 0, wx.ALL, 5)
        self.replaceFilePath8 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(800, -1), 0)
        replaceBs8.Add(self.replaceFilePath8, 0, wx.ALL, 5)
        replaceBsWrapper.Add(replaceBs8, 1, wx.EXPAND, 5)

        replaceBs9 = wx.BoxSizer(wx.HORIZONTAL)
        replaceBs9.SetMinSize(wx.Size(-1, 20))
        self.replaceFileName9 = wx.StaticText(self, wx.ID_ANY, 'replaceFileName1', wx.DefaultPosition, wx.DefaultSize, 0)
        self.replaceFileName9.Wrap(-1)
        self.replaceFileName9.SetMinSize(wx.Size(260, -1))
        replaceBs9.Add(self.replaceFileName9, 0, wx.ALL, 5)
        self.replaceFilePath9 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(800, -1), 0)
        replaceBs9.Add(self.replaceFilePath9, 0, wx.ALL, 5)
        replaceBsWrapper.Add(replaceBs9, 1, wx.EXPAND, 5)

        replaceBs10 = wx.BoxSizer(wx.HORIZONTAL)
        replaceBs10.SetMinSize(wx.Size(-1, 20))
        self.replaceFileName10 = wx.StaticText(self, wx.ID_ANY, 'replaceFileName1', wx.DefaultPosition, wx.DefaultSize, 0)
        self.replaceFileName10.Wrap(-1)
        self.replaceFileName10.SetMinSize(wx.Size(260, -1))
        replaceBs10.Add(self.replaceFileName10, 0, wx.ALL, 5)
        self.replaceFilePath10 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(800, -1), 0)
        replaceBs10.Add(self.replaceFilePath10, 0, wx.ALL, 5)
        replaceBsWrapper.Add(replaceBs10, 1, wx.EXPAND, 5)

        replaceBsBtn = wx.BoxSizer(wx.HORIZONTAL)
        replaceBsBtn.SetMinSize(wx.Size(-1, 20))
        self.replaceAndRestartBtn = wx.Button(self, wx.ID_ANY, '替换并重启Tomcat', wx.DefaultPosition, wx.DefaultSize, 0)
        replaceBsBtn.Add(self.replaceAndRestartBtn, 0, wx.ALL, 5)
        self.replaceBtn = wx.Button(self, wx.ID_ANY, '仅替换', wx.DefaultPosition, wx.DefaultSize, 0)
        replaceBsBtn.Add(self.replaceBtn, 0, wx.ALL, 5)
        replaceBsWrapper.Add(replaceBsBtn, 1, wx.EXPAND, 5)

        self.SetSizer(replaceBsWrapper)
        self.Layout()

        self.Centre(wx.BOTH)
        # 绑定事件
        self.replaceBtn.Bind(wx.EVT_BUTTON, self.about_tomcat)

        self.replaceFileNames = [self.replaceFileName1, self.replaceFileName2, self.replaceFileName3, self.replaceFileName4,
                            self.replaceFileName5, self.replaceFileName6, self.replaceFileName7, self.replaceFileName8,
                            self.replaceFileName9, self.replaceFileName10]
        self.replaceFilePaths = [self.replaceFilePath1, self.replaceFilePath2, self.replaceFilePath3, self.replaceFilePath4,
                            self.replaceFilePath5, self.replaceFilePath6, self.replaceFilePath7, self.replaceFilePath8,
                            self.replaceFilePath9, self.replaceFileName10]
        self.files = os.listdir('replaceFiles')
        for i, file in enumerate(self.files):
            self.replaceFileNames[i].SetLabel(file)

    def about_tomcat(self, event):
        replaceMap = {}
        for i, file in enumerate(self.files):
            replaceMap['replaceFiles\\' + self.replaceFileNames[i].GetLabel()] = \
                '/opt/project/webapps_8080/ROOT' + str(self.replaceFilePaths[i].GetValue()).split(project_name[0])[1].replace('\\\\', '/')
        for (k, v) in replaceMap.items():
            print(k)
            print(v)

    def __del__(self):
        pass


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='日志查看', pos=wx.DefaultPosition, size=wx.Size(1600, 1050),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(223, 223, 223))

        mainGridSizer = wx.GridSizer(2, 2, 5, 5)

        # 第一个日志输出
        boxSizer1 = wx.BoxSizer(wx.VERTICAL)
        self.ip1 = wx.StaticText(self, wx.ID_ANY, '192.168.1.1', wx.DefaultPosition, wx.DefaultSize, 0)
        self.ip1.Wrap(-1)
        boxSizer1.Add(self.ip1, 0, wx.ALL, 5)
        self.logOut1 = wx.TextCtrl(self, wx.ID_ANY, '1',
                                   wx.DefaultPosition, wx.Size(1000, 1000),
                                   wx.TE_CHARWRAP | wx.TE_MULTILINE | wx.TE_WORDWRAP)
        self.logOut1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        boxSizer1.Add(self.logOut1, 0, wx.ALL, 5)
        # 第一个日志输出结束

        # 第二个日志输出
        boxSizer2 = wx.BoxSizer(wx.VERTICAL)
        self.ip2 = wx.StaticText(self, wx.ID_ANY, '192.168.1.1', wx.DefaultPosition, wx.DefaultSize, 0)
        self.ip2.Wrap(-1)
        boxSizer2.Add(self.ip2, 0, wx.ALL, 5)
        self.logOut2 = wx.TextCtrl(self, wx.ID_ANY, '2',
                                   wx.DefaultPosition, wx.Size(1000, 1000),
                                   wx.TE_CHARWRAP | wx.TE_MULTILINE | wx.TE_WORDWRAP)
        self.logOut2.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        boxSizer2.Add(self.logOut2, 0, wx.ALL, 5)
        # 第二个日志输出结束

        # 第三个日志输出
        boxSizer3 = wx.BoxSizer(wx.VERTICAL)
        self.ip3 = wx.StaticText(self, wx.ID_ANY, '192.168.1.1', wx.DefaultPosition, wx.DefaultSize, 0)
        self.ip3.Wrap(-1)
        boxSizer3.Add(self.ip3, 0, wx.ALL, 5)
        self.logOut3 = wx.TextCtrl(self, wx.ID_ANY, '3',
                                   wx.DefaultPosition, wx.Size(1000, 1000),
                                   wx.TE_CHARWRAP | wx.TE_MULTILINE | wx.TE_WORDWRAP)
        self.logOut3.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        boxSizer3.Add(self.logOut3, 0, wx.ALL, 5)
        # 第三个日志输出结束

        # 第四个日志输出
        boxSizer4 = wx.BoxSizer(wx.VERTICAL)
        self.ip4 = wx.StaticText(self, wx.ID_ANY, '192.168.1.1', wx.DefaultPosition, wx.DefaultSize, 0)
        self.ip4.Wrap(-1)
        boxSizer4.Add(self.ip4, 0, wx.ALL, 5)

        self.logOut4 = wx.TextCtrl(self, wx.ID_ANY, '4',
                                   wx.DefaultPosition, wx.Size(1000, 1000),
                                       wx.TE_CHARWRAP | wx.TE_MULTILINE | wx.TE_WORDWRAP)
        self.logOut4.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        boxSizer4.Add(self.logOut4, 0, wx.ALL, 5)
        # 第四个日志输出结束

        mainGridSizer.Add(boxSizer1, 1, wx.EXPAND, 5)
        mainGridSizer.Add(boxSizer2, 2, wx.EXPAND, 5)
        mainGridSizer.Add(boxSizer3, 3, wx.EXPAND, 5)
        mainGridSizer.Add(boxSizer4, 4, wx.EXPAND, 5)

        self.SetSizer(mainGridSizer)
        self.Layout()

        # 菜单栏
        self.mainMenuBar = wx.MenuBar(0)
        self.menu1 = wx.Menu()
        self.gccce = wx.MenuItem(self.menu1, wx.ID_ANY, 'gccce', wx.EmptyString, wx.ITEM_NORMAL)
        self.menu1.Append(self.gccce)

        self.task = wx.MenuItem(self.menu1, wx.ID_ANY, 'task', wx.EmptyString, wx.ITEM_NORMAL)
        self.menu1.Append(self.task)

        self.bg = wx.MenuItem(self.menu1, wx.ID_ANY, 'bg', wx.EmptyString, wx.ITEM_NORMAL)
        self.menu1.Append(self.bg)

        self.interface = wx.MenuItem(self.menu1, wx.ID_ANY, 'interface', wx.EmptyString, wx.ITEM_NORMAL)
        self.menu1.Append(self.interface)

        self.master = wx.MenuItem(self.menu1, wx.ID_ANY, 'master', wx.EmptyString, wx.ITEM_NORMAL)
        self.menu1.Append(self.master)

        self.mainMenuBar.Append(self.menu1, '选择项目')

        self.menu2 = wx.Menu()
        self.mainMenuBar.Append(self.menu2, '替换文件')
        self.replaceFiles = wx.MenuItem(self.menu1, wx.ID_ANY, '替换', wx.EmptyString, wx.ITEM_NORMAL)
        self.menu2.Append(self.replaceFiles)

        self.SetMenuBar(self.mainMenuBar)

        # 绑定事件
        self.Bind(wx.EVT_MENU, self.run_thread, self.gccce)
        self.Bind(wx.EVT_MENU, self.open_replace_window, self.replaceFiles)
        self.Centre(wx.BOTH)
        pub.subscribe(self.update_display, 'update')

    def update_display(self, bs_index, ip, log_out):
        if bs_index == 1:
            self.ip1.SetLabel(ip)
            self.logOut1.SetLabel(log_out)
        elif bs_index == 2:
            self.ip2.SetLabel(ip)
            self.logOut2.SetLabel(log_out)
        elif bs_index == 3:
            self.ip3.SetLabel(ip)
            self.logOut3.SetLabel(log_out)
        elif bs_index == 4:
            self.ip4.SetLabel(ip)
            self.logOut4.SetLabel(log_out)

    def run_thread(self, event):
        TestThread()

    def open_replace_window(self, event):
        ReplaceFileFrame(self).Show()

    def __del__(self):
        pass


app = wx.App()
frame = MainFrame(None).Show()
app.MainLoop()
