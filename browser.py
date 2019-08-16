#!/bin/python

import wx
import wx.html2
import sys

class BrowserFrame(wx.Frame):
    """ 
    Main browser frame
    """

    def __init__(self, url, *args, **kw):
        super(BrowserFrame, self).__init__(*args, **kw)
        
        if url:
            self.url = url
        else:
            self.url = "https://google.com"
        # For scrolling
        self.xPos = 0
        self.yPos = 0

        # create main panel
        self.panel = wx.Panel(self) 
      
        # create a sizer (stacked vertically)
        self.vertical = wx.BoxSizer(wx.VERTICAL) 
        
        # create url entry
        self.urlentry = wx.TextCtrl(self.panel, value=self.url,style=wx.TE_PROCESS_ENTER)

        # add entry to screen
        self.vertical.Add(self.urlentry,flag=wx.EXPAND)
        
        # add "Go" button
        #self.vertical.Add(self.goButton)

        # create browser window
        self.browser = wx.html2.WebView.New(self.panel,url=self.url, name="Simple Browser",size=(700,700))
        self.go(None)
        # add browser window to the screen
        self.vertical.Add(self.browser, flag=wx.EXPAND, proportion=1)
        
        self.panel.SetSizer(self.vertical)

        self.urlentry.Bind(wx.EVT_TEXT_ENTER, self.go)

        self.browser.Bind(wx.EVT_KEY_DOWN, self.keyboardEvents)

        self.browser.Bind(wx.html2.EVT_WEBVIEW_TITLE_CHANGED, self.changeTitle)

    # This method is not working correctly
    def go(self, event):
        url = self.urlentry.GetLineText(0) # get url
        if url[:8].lower() != "https://":
            url = "https://" + url
            self.urlentry.SetValue(url)

        
        print(url)
        self.browser.LoadURL(url)
        self.yPos = 0
        self.browser.SetFocus()

    def changeTitle(self, event):
        title = event.GetString()
        self.SetTitle("Simple Browser - " + title)
        

    def keyboardEvents(self, event):
        keycode = event.GetKeyCode()
        print(keycode)


        if event.ShiftDown() and keycode == ord('J'):
            self.yPos += 50
            self.browser.RunScript('scrollTo(%d, %d)' % (self.xPos, self.yPos))
        elif keycode == ord('J'):
            self.yPos += 10
            self.browser.RunScript('scrollTo(%d, %d)' % (self.xPos, self.yPos))

        elif event.ShiftDown() and keycode == ord('K'):
            self.yPos -= 50
            self.browser.RunScript('scrollTo(%d, %d)' % (self.xPos, self.yPos))
        elif keycode == ord('K'):
            self.yPos -= 10
            self.browser.RunScript('scrollTo(%d, %d)' % (self.xPos, self.yPos))

        if keycode == ord('O'):
            self.urlentry.SetFocus()


        if yPos < 0:
            yPos = 0

if __name__ == "__main__":
    app = wx.App() 
    
    
    if len(sys.argv) == 2:
        url = sys.argv[1]
    else:
        url = None
    frame = BrowserFrame(url, None, title="Simple Browser",size=(1200,768))
    frame.Show()
    app.MainLoop()

