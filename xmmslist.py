#!/usr/bin/python

#
# File:         xmmslist.py
# 
# Function:     Shell-command for XMMS Song Change plugin.
#
# Author(s):    Erik C. Thauvin (erik@thauvin.net)
#
# Copyright:    Copyright (C) 2003 Erik C. Thauvin
#               All Rights Reserved.
#
# Source:       Started anew.
#
# Notes:        See the README file for more information.
#
# History:
#
#   2003-08-11  ECT    Initial coding.
#
#   
# Disclaimer:
#   
#   This software is provided "as is" without express or implied warranties.
#   Permission is granted to use, copy, modify and distribute this software,
#   provided this disclaimer and copyright are preserved on all copies. This
#   software may not, however, be sold or distributed for profit, or included
#   with other software which is sold or distributed for profit, without the
#   permission of the author.
#
# $Id$

import sys
import re
import cgi
import urllib
import time
import os.path

# The script version number
version='0.1'

# The output file
playlist=os.path.expanduser('~/bin/playlist.txt')

# The maximum number of songs to keep in the playlist
maxsongs=20

# The song search tooltip and URL
songtip='Search for the lyrics of this song.'
songsearch='http://www.lyricsstation.com/search.asp?R1=V1&amp;txtSearch='

# The artist search tooltip and URL
bandtip='Search for this artist on Google.'
bandsearch='"http://www.google.com/search?cat=gwd%2FTop%2FArts%2FMusic&amp;q='

# The album search tooltip and URL
albumtip='Search for this album on freedb.'
albumsearch='http://www.freedb.org/freedb_search.php?allfields=NO&amp;fields=artist&amp;fields=title&amp;allcats=YES&amp;grouping=cats&amp;words='


if len(sys.argv) > 1:
	# XMMS title format should be set to: %p -- %t -- %a
	# e.g.: The Artist -- The Song -- The Album
	m = re.search('(.*) -- (.*) -- (.*)', sys.argv[1])
	if m:
		
		try:
			f = open(playlist, 'r')
			lines = f.readlines()
			f.close()
		except IOError:
			lines = ''

		song = '<tr valign="top">'

		# Song
		if len(m.group(2)) >= 1:
			song += '<td><a title="' + songtip + '" href="' + songsearch + urllib.quote_plus(m.group(2)) + '" target="_blank">' + cgi.escape(m.group(2)) + '</a></td>'
		else:
			song += '<td><font color="gray">n/a</font></td>'
	
		song += '<td>&nbsp</td>'
		
		# Artist
		if len(m.group(1)) >= 1:
			song += '<td><a title="' + bandtip + '" href=' + bandsearch + urllib.quote_plus('"' + m.group(1) + '"') + '" target="_blank">' + cgi.escape(m.group(1)) + '</a></td>'
		else:
			song += '<td><font color="gray">n/a</font></td>'
		
		song += '<td>&nbsp</td>'
		
		# Album
		if len(m.group(3)) >= 1:
			song += '<td><a title="'+ albumtip + '" href="' + albumsearch + urllib.quote_plus((m.group(1) + ' ' + m.group(3)).replace('(', '').replace(')', '').replace('.', '')) + '" target="_blank">' + cgi.escape(m.group(3)) + '</a></td>'
		else:
			song += '<td><font color="gray">n/a</font></td>'
	
		song += '</tr>\n'

		f = open(playlist, 'w')
		f.write(song)
		
		stop = len(lines) - 1
		if stop > 0:
			i = 1
			for line in lines:
				if song != line:
					f.write(line)
				i += 1
				if i >= maxsongs or i > stop:
					break
					
		# Last Update
		f.write('<tr><td colspan="3" valign="bottom" align="left"><br><br><small>' + time.strftime('Updated on %B %d, %Y at %H:%M %Z') + '</small></td><td colspan="2" valign="bottom" align="right"><small><a href="http://www.thauvin.net/blog/stories.jsp?id=5#xmmslist" class="small" target="_blank">' + os.path.basename(sys.argv[0]) + '</a> ' + version + '</small></td></tr>\n')
	
		f.close()
