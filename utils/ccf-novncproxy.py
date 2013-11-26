#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename:ccf-novncproxy.py
# Date:Tue Nov 26 15:55:47 CST 2013
# Author:Pengbo Li
# E-mail:lipengbo10054444@gmail.com

from websockify import WebSocketProxy


if __name__ == '__main__':
    # Create and start the NovaWebSockets proxy
    server = WebSocketProxy(listen_host='0.0.0.0',
                            listen_port=6080,
                            daemon=True,
                            web='./',
                            target_host='192.168.5.109',
                            target_port='5900',
                            wrap_mode='exit',
                            wrap_cmd=None)
    server.start_server()
