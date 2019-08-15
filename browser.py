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
        #self.goButton = wx.Button(self.panel,label="Go")
        #self.goButton.Bind(wx.EVT_BUTTON, self.go)
       
        # create a sizer (stacked vertically)
        self.vertical = wx.BoxSizer(wx.VERTICAL) 
        
        # create url entry
        self.urlentry = wx.TextCtrl(self.panel, value="http://google.com",style=wx.TE_PROCESS_ENTER)

        # add entry to screen
        self.vertical.Add(self.urlentry,flag=wx.EXPAND)
        
        # add "Go" button
        #self.vertical.Add(self.goButton)

        # create browser window
        self.browser = wx.html2.WebView.New(self.panel,url="http://google.com",name="Simple Browser",size=(700,700))
    
        # add browser window to the screen
        self.vertical.Add(self.browser, flag=wx.EXPAND, proportion=1)
        
        self.panel.SetSizer(self.vertical)

        self.urlentry.Bind(wx.EVT_TEXT_ENTER, self.go)

        self.Bind(wx.EVT_KEY_DOWN, self.keyboardEvents)

        self.browser.Bind(wx.html2.EVT_WEBVIEW_TITLE_CHANGED, self.changeTitle)

    # This method is not working correctly
    def go(self, event):
        url = self.urlentry.GetLineText(0) # get url
        if url[:7].lower() != "https://":
            url = "https://" + url
            self.urlentry.SetValue(url)
        print(url)
        self.browser.LoadURL(url)
        self.browser.SetFocus()

    def changeTitle(self, event):
        title = event.GetString()
        self.SetTitle("Simple Browser - " + title)
        

    def keyboardEvents(self, event):
        keycode = event.GetKeyCode()
        if keycode == ord('j'):
            print('j')

        

if __name__ == "__main__":
    app = wx.App() 
    frame = BrowserFrame(None, title="Simple Browser",size=(1200,768))
    frame.Show()
    app.MainLoop()

