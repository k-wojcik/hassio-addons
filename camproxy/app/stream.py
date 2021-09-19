# Run manually:
# > set OPTIONS_PATH=%cd%\camproxy\app\dev\env\options.json
# > python stream.py | ffplay -i pipe:

from shared import logger, options
import socket
import time
import datetime
import sys

def main(camId):
    logger.info("Start stream for cam: " + camId)

    if sys.version_info.major < 3:
        sys.exit("Python 3 is required.\n")

    cam_config = [x for x in options["cams"] if x['key'] == camId][0]["proxy"]
    
    channel_number = cam_config["channel"]
    stream = cam_config["stream"]
    TCP_IP = cam_config["ip"]
    TCP_PORT = cam_config["port"]
    USERNAME = cam_config["user"].encode()
    PASSWORD = cam_config["password"].encode()

    pad = lambda string, length: string.ljust(length, b'\0')
    pre = b'\xaa\x00\x00\x00'

    # Initialize socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    s.setblocking(1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((TCP_IP, TCP_PORT))

	# Initial request... response is XML followed by many "#" symbols
    s.send(b'GET /bubble/live?ch=0&stream=0 HTTP/1.1\r\n\r\n')
    s.recv(1024) 

	# Username/password... response is mostly empty bytes
    s.send(pad(pre, 18) + pad(USERNAME, 20) + pad(PASSWORD, 20))
    s.recv(54)

    # Request the stream... Uhh... No password is required ¯\_(ツ)_/¯
    unknownByte = bytes([1])
    s.send(pre + pad(b'\x00\x0a', 6) + pad(bytes([channel_number]), 4) +
           pad(bytes([stream]), 4) + pad(unknownByte, 8))
    s.setblocking(0)


    try:
        while True:
            try:
                yield s.recv(16)
            except BlockingIOError:
                time.sleep(.1)
                pass

    # https://docs.python.org/2/howto/sockets.html#disconnecting
    except BrokenPipeError:
        s.shutdown(1)
        s.close()
    except KeyboardInterrupt:
        stdout.close()
        s.shutdown(1)
        s.close()


# Support directly calling from command line with a file path containing the email_data
if __name__ == "__main__":
    stdout = sys.stdout.buffer
    generator = main(sys.argv[1])
    while True:
        stdout.write(next(generator))
