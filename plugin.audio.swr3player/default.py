# -*- coding: utf-8 -*-


import os,xbmcgui,xbmc,xbmcaddon,xbmcvfs
import requests as req
import re

title = 'SWR3 Video Livestream'
url = 'https://www.swr3.de/aktuell/live-blog/video-livestream-104.html'
pDialog = xbmcgui.DialogProgress()
pDialog.create(title, 'Initializing script...')

addonID = 'plugin.audio.swr3player'
addon = xbmcaddon.Addon(id = addonID)
addonPath = addon.getAddonInfo('path')
icon = xbmcvfs.translatePath( os.path.join( addonPath , 'icon.png' ) )

xbmc.log(url,xbmc.LOGINFO)
pDialog.update(25, 'Loding web page')

resp = req.get(url)
m3u = re.search('".*m3u8"', resp.text).group()
m3u = m3u[1:-1]
xbmc.log(m3u,xbmc.LOGINFO)

pDialog.update(50, 'Loding playlist')
m3uResp = req.get(m3u)
xbmc.log(m3uResp.text,xbmc.LOGINFO)

pDialog.update(75, 'Extracting video URL')
stream = re.search('.*master-720.*\n', m3uResp.text).group().strip()
xbmc.log(stream,xbmc.LOGINFO)

pDialog.update(100, 'Starting playback')
xbmcPlayer = xbmc.Player()
playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
listitem = xbmcgui.ListItem( title)
listart = "{ 'icon':'%s', 'thumb': '%s' }" % (icon, icon)
listitem.setArt( listart )
playlist.clear()
playlist.add( stream, listitem )
pDialog.close()
xbmc.executebuiltin("ActivateWindow(home)")
xbmcPlayer.play(playlist)

