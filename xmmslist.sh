#!/bin/sh

#
# xmmslist.sh
#
# Transfers the xmmslist playlist to a Web server. See the README file for
# more information.
#
# Copyright (C) 2003 Erik C. Thauvin. All rights reserved.
#
# This software is provided "as is" without express or implied warranties.
#
# Permission is granted to use, copy, modify and distribute this software,
# provided this disclaimer and copyright are preserved on all copies. This
# software may not, however, be sold or distributed for profit, or included
# with other software which is sold or distributed for profit, without the
# permission of the author.
#
# $Id$

# The receiving host name
RHOST="nix.thauvin.net"

# The receiving host location
RLOC="/var/www/html/erik/tunez/"

if test -n "`ps -cx|grep xmms$`"; then
	# ncftpput -u user -p password ${RHOST} ${RLOC} ${HOME}/bin/playlist.txt
	scp -q ${HOME}/bin/playlist.txt ${RHOST}:${RLOC}
fi
