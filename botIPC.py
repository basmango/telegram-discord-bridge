import zmq
import random
import sys
import time
import asyncio
import zmq.asyncio
port = "5666"

async def async_connect():
    ctx = zmq.asyncio.Context()
    sock = ctx.socket(zmq.PAIR)
    sock.connect("tcp://0.0.0.0:%s" % port)
    return sock;
def bind():
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.bind("tcp://*:%s" % port)
    return socket
def connect():
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("tcp://0.0.0.0:%s" % port)
    return socket
