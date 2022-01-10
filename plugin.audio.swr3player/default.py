# -*- coding: utf-8 -*-


import os,sys,xbmcplugin,xbmcgui,xbmc,xbmcaddon
import requests as req
import re

addonID = 'plugin.audio.swr3player'
addon = xbmcaddon.Addon(id = addonID)
addonPath = addon.getAddonInfo('path')
profilePath = addon.getAddonInfo('profile')
icon = xbmc.translatePath( os.path.join( addonPath , 'icon.png' ) )
title = 'SWR3 Video Livestream'

resp = req.get("https://www.swr3.de/aktuell/live-blog/video-livestream-104.html")
m3u = re.search('".*m3u8"', resp.text).group()
m3u = m3u[1:-1]
xbmc.log(m3u,xbmc.LOGNOTICE)

m3uResp = req.get(m3u)
xbmc.log(m3uResp.text,xbmc.LOGNOTICE)

stream = re.search('.*master-720.*\n', m3uResp.text).group().strip()
xbmc.log(stream,xbmc.LOGNOTICE)

xbmcPlayer = xbmc.Player()
playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
xbmc.executebuiltin("ActivateWindow(home)")
listitem = xbmcgui.ListItem( title, iconImage=icon, thumbnailImage=icon)
playlist.clear()
playlist.add( stream, listitem )
xbmcPlayer.play(playlist)

