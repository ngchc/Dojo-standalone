#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.1 on Wed Jun 27 15:32:10 2018
#

#########
import numpy as np
import PIL
import PIL.Image
import skimage.util
#########

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class SuperPixel(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SuperPixel.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((484, 444))
        self.SelectAlgorithm = wx.Notebook(self, 1)
        self.Felzenszwalb = wx.Panel(self.SelectAlgorithm, wx.ID_ANY)
        self.spin_ctrl_1_1d = wx.SpinCtrlDouble(self.Felzenszwalb, wx.ID_ANY, "100.0", min=0.0, max=1000.0)
        self.spin_ctrl_1_2d = wx.SpinCtrlDouble(self.Felzenszwalb, wx.ID_ANY, "0.5", min=0.0, max=100.0)
        self.spin_ctrl_1_3 = wx.SpinCtrl(self.Felzenszwalb, wx.ID_ANY, "50", min=0, max=500)
        self.SLIC = wx.Panel(self.SelectAlgorithm, wx.ID_ANY)
        self.spin_ctrl_2_1 = wx.SpinCtrl(self.SLIC, wx.ID_ANY, "250", min=0, max=10000)
        self.spin_ctrl_2_2d = wx.SpinCtrlDouble(self.SLIC, wx.ID_ANY, "10.0", min=0.0, max=100.0)
        self.spin_ctrl_2_3d = wx.SpinCtrlDouble(self.SLIC, wx.ID_ANY, "1.0", min=0.0, max=100.0)
        self.Quickshift = wx.Panel(self.SelectAlgorithm, wx.ID_ANY)
        self.spin_ctrl_3_1d = wx.SpinCtrlDouble(self.Quickshift, wx.ID_ANY, "3.0", min=0.0, max=100.0)
        self.spin_ctrl_3_2d = wx.SpinCtrlDouble(self.Quickshift, wx.ID_ANY, "6.0", min=0.0, max=100.0)
        self.spin_ctrl_3_3 = wx.SpinCtrlDouble(self.Quickshift, wx.ID_ANY, "0.5", min=0.0, max=1.0)
        self.Watershed = wx.Panel(self.SelectAlgorithm, wx.ID_ANY)
        self.spin_ctrl_4_1 = wx.SpinCtrl(self.Watershed, wx.ID_ANY, "250", min=0, max=10000)
        self.spin_ctrl_4_2d = wx.SpinCtrlDouble(self.Watershed, wx.ID_ANY, "0.001", min=0.0, max=10.0)
        self.panel_5 = wx.Panel(self, wx.ID_ANY)
        self.spin_ctrl_x = wx.SpinCtrl(self.panel_5, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_y = wx.SpinCtrl(self.panel_5, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_z = wx.SpinCtrl(self.panel_5, wx.ID_ANY, "0", min=0, max=100)
        self.panel_3 = wx.Panel(self.panel_5, wx.ID_ANY)
        self.SuperPixPreview = wx.Button(self.panel_5, 2, "Preview")
        self.panel_4 = wx.Panel(self.panel_5, wx.ID_ANY)
        self.SuperPixExecute = wx.Button(self.panel_5, 3, "Execute")
        self.panel_1 = wx.Panel(self.panel_5, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self._SP_SelectAlgorithm, id=1)
        self.Bind(wx.EVT_BUTTON, self._SP_Preview, id=2)
        self.Bind(wx.EVT_BUTTON, self._SP_Execute, id=3)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: SuperPixel.__set_properties
        self.SetTitle("Superpixelization")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("./../../icons/Mojo2_16.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SuperPixPreview.SetMinSize((93, 26))
        self.SuperPixExecute.SetMinSize((93, 26))
        self.panel_1.SetMinSize((4000, 4000))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SuperPixel.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.StaticBoxSizer(wx.StaticBox(self.panel_5, wx.ID_ANY, ""), wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(5, 2, 0, 0)
        grid_sizer_5 = wx.FlexGridSizer(2, 2, 0, 0)
        grid_sizer_4 = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_3 = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_2 = wx.FlexGridSizer(3, 2, 0, 0)
        text_1_1 = wx.StaticText(self.Felzenszwalb, wx.ID_ANY, "Scale")
        grid_sizer_2.Add(text_1_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        grid_sizer_2.Add(self.spin_ctrl_1_1d, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        text_1_2 = wx.StaticText(self.Felzenszwalb, wx.ID_ANY, "Sigma")
        grid_sizer_2.Add(text_1_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        grid_sizer_2.Add(self.spin_ctrl_1_2d, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        text_1_3 = wx.StaticText(self.Felzenszwalb, wx.ID_ANY, "Min size")
        grid_sizer_2.Add(text_1_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        grid_sizer_2.Add(self.spin_ctrl_1_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        self.Felzenszwalb.SetSizer(grid_sizer_2)
        text_2_1 = wx.StaticText(self.SLIC, wx.ID_ANY, "N segments")
        grid_sizer_3.Add(text_2_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        grid_sizer_3.Add(self.spin_ctrl_2_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        text_2_2 = wx.StaticText(self.SLIC, wx.ID_ANY, "Compactness")
        grid_sizer_3.Add(text_2_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        grid_sizer_3.Add(self.spin_ctrl_2_2d, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        text_2_3 = wx.StaticText(self.SLIC, wx.ID_ANY, "Sigma")
        grid_sizer_3.Add(text_2_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        grid_sizer_3.Add(self.spin_ctrl_2_3d, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        self.SLIC.SetSizer(grid_sizer_3)
        text_3_1 = wx.StaticText(self.Quickshift, wx.ID_ANY, "Kernel size")
        grid_sizer_4.Add(text_3_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        grid_sizer_4.Add(self.spin_ctrl_3_1d, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        text_3_2 = wx.StaticText(self.Quickshift, wx.ID_ANY, "Max dist")
        grid_sizer_4.Add(text_3_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        grid_sizer_4.Add(self.spin_ctrl_3_2d, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        text_3_3 = wx.StaticText(self.Quickshift, wx.ID_ANY, "Ratio")
        grid_sizer_4.Add(text_3_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        grid_sizer_4.Add(self.spin_ctrl_3_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        self.Quickshift.SetSizer(grid_sizer_4)
        text_4_1 = wx.StaticText(self.Watershed, wx.ID_ANY, "N markers")
        grid_sizer_5.Add(text_4_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        grid_sizer_5.Add(self.spin_ctrl_4_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        text_4_2 = wx.StaticText(self.Watershed, wx.ID_ANY, "Compactness")
        grid_sizer_5.Add(text_4_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        grid_sizer_5.Add(self.spin_ctrl_4_2d, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        self.Watershed.SetSizer(grid_sizer_5)
        self.SelectAlgorithm.AddPage(self.Felzenszwalb, "Felzenszwalb")
        self.SelectAlgorithm.AddPage(self.SLIC, "SLIC")
        self.SelectAlgorithm.AddPage(self.Quickshift, "Quickshift")
        self.SelectAlgorithm.AddPage(self.Watershed, "Watershed")
        sizer_2.Add(self.SelectAlgorithm, 1, wx.ALL | wx.EXPAND, 0)
        ####
        xsize = 256
        ysize = 256
        # img = PIL.Image.open('y=00000000,x=00000000.tif')
        # img = skimage.util.img_as_float(img)
        img  = wx.Image('y=00000000,x=00000000.tif')
        img  = img.Scale(xsize, ysize, wx.IMAGE_QUALITY_HIGH)
        bimg = img.ConvertToBitmap()
        ####
        # bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("C:\\Users\\uraku\\Desktop\\Mojo180625\\superpixel\\y=00000000,x=00000000_.tif", wx.BITMAP_TYPE_ANY))
        bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, bimg, pos=(0, 0), size=img.GetSize())
        ####
        bitmap_1.SetMinSize((256, 256))
        sizer_3.Add(bitmap_1, 1, wx.ALL, 10)
        locx = wx.StaticText(self.panel_5, wx.ID_ANY, "X id")
        grid_sizer_1.Add(locx, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        grid_sizer_1.Add(self.spin_ctrl_x, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        locy = wx.StaticText(self.panel_5, wx.ID_ANY, "Y id")
        grid_sizer_1.Add(locy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        grid_sizer_1.Add(self.spin_ctrl_y, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        locz = wx.StaticText(self.panel_5, wx.ID_ANY, "Z id")
        grid_sizer_1.Add(locz, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        grid_sizer_1.Add(self.spin_ctrl_z, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        grid_sizer_1.Add(self.panel_3, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.SuperPixPreview, 0, wx.ALL, 4)
        grid_sizer_1.Add(self.panel_4, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.SuperPixExecute, 0, wx.ALL, 4)
        sizer_1.Add(grid_sizer_1, 1, wx.ALIGN_RIGHT, 0)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.panel_5.SetSizer(sizer_1)
        sizer_3.Add(self.panel_5, 0, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.ALIGN_RIGHT | wx.ALL | wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade

    def _SP_SelectAlgorithm(self, event):  # wxGlade: SuperPixel.<event_handler>
        print("Event handler '_SP_SelectAlgorithm' not implemented!")
        event.Skip()

    def _SP_Preview(self, event):  # wxGlade: SuperPixel.<event_handler>
        print("Event handler '_SP_Preview' not implemented!")
        event.Skip()

    def _SP_Execute(self, event):  # wxGlade: SuperPixel.<event_handler>
        print("Event handler '_SP_Execute' not implemented!")
        event.Skip()

# end of class SuperPixel

class MyApp(wx.App):
    def OnInit(self):
        self.SuperPixel = SuperPixel(None, wx.ID_ANY, "")
        self.SetTopWindow(self.SuperPixel)
        self.SuperPixel.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
