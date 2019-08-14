import wx
import wx.html2

class BrowserFrame(wx.Frame):
    """ 
    Main browser frame
    """

    def __init__(self, *args, **kw):
        super(BrowserFrame, self).__init__(*args, **kw)

        # create main panel
        self.panel = wx.Panel(self) 

        # create "Go" button
        self.goButton = wx.Button(self.panel,label="Go")
        self.goButton.Bind(wx.EVT_BUTTON, self.go)
       
        # create a sizer (stacked vertically)
        self.vertical = wx.BoxSizer(wx.VERTICAL) 
        
        # create url entry
        self.urlentry = wx.TextCtrl(self.panel, value="http://google.com")

        # add entry to screen
        self.vertical.Add(self.urlentry,flag=wx.EXPAND)
        
        # add "Go" button
        self.vertical.Add(self.goButton)

        # create browser window
        self.browser = wx.html2.WebView.New(self.panel,url="http://test.com",name="Simple Browser",size=(700,700))
        
        # add browser window to the screen
        self.vertical.Add(self.browser, flag=wx.EXPAND, proportion=1)
        
        self.panel.SetSizer(self.vertical)


    # This method is not working correctly
    def go(self, event):
        url = self.urlentry.GetLineText(0) # get url
        print(url)
        print(self.browser.LoadURL("http://google.com"))
        self.browser.Reload()


        

if __name__ == "__main__":
    app = wx.App() 
    frame = BrowserFrame(None, title="Simple Browser",size=(1200,768))
    frame.Show()
    app.MainLoop()

