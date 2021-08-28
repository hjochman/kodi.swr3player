# -*- coding: utf-8 -*-


import os,sys,xbmcplugin,xbmcgui,xbmc,xbmcaddon,urllib

addonID = 'plugin.audio.swr3player'
addon = xbmcaddon.Addon(id = addonID)
addonPath = addon.getAddonInfo('path')
profilePath = addon.getAddonInfo('profile')
icon = xbmc.translatePath( os.path.join( addonPath , 'icon.png' ) )
title = 'SWR3 Video Livestream'

#view-source:https://www.swr3.de/aktuell/live-blog/video-livestream-104.html
#<script id="playerJSON" type="text/plain">
#stream = 'https://swrswr3vrhls-i.akamaihd.net/hls/live/780818/vrswr3/master.m3u8'
# 28.Aug 21 https://swrswr3vrhls-i.akamaihd.net/hls/live/780818/vrswr3/master.m3u8?set-segment-duration=responsive
# https://swrswr3vrhls-i.akamaihd.net/hls/live/780818/vrswr3/master-720p-3628.m3u8
stream = 'https://swrswr3vrhls-i.akamaihd.net/hls/live/780818/vrswr3/master-720p-3628.m3u8'

xbmcPlayer = xbmc.Player()
playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
xbmc.executebuiltin("ActivateWindow(home)")
listitem = xbmcgui.ListItem( title, iconImage=icon, thumbnailImage=icon)
playlist.clear()
playlist.add( stream, listitem )
xbmcPlayer.play(playlist)

