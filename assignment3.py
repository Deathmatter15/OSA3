#!/usr/bin/env python3

# Python file for a multi-threaded network server in python.
import sys 
import socket
import threading
from queue import Queue

# Functions  Classes
class Node: 
  def __init__(self, data = None, next = None, book_next = None, next_frequent_search = None):
    self.next = next
    self.data = data
    self.book_next = book_next
    self.next_frequent_search = next_frequent_search

class llist:
  def __init__(self):
    self.list = None
    self.tail = None
    self.header = {}
    return

  def add(self, book_num, write):
    new_Node = Node(write)
    if book_num not in self.header:
      self.header[book_num] = new_Node
    
    if self.list is None:
      self.list = new_Node
      self.tail = self.list.next
    else:
      self.tail = new_Node
      self.tail = self.tail.next
    return

  def write(self, book_num):
    if(book_num < 10):
      file_name = f"book_0{book_num}.txt"
    else: 
      file_name = f"book_{book_num}.txt"
    curr_Node = self.header[book_num]
    with open(file_name, 'w') as file:
      while curr_Node.data is not None: 
        file.write(curr_Node.data)
    return

def arg_debugging(debug = True):
  if len(sys.argv) !=5:
    print("Usage: ./assignment -l <port> -p <pattern>")
    return None, None

  port: int = int(sys.argv[2])
  if port < 1024:
    print("Usage: 1025 or greater port Number.")
    return None, None
  
  pattern: str = sys.argv[4]
  if(debug):
    print(f"Script name: {sys.argv[0]}")
    print(f"port number: {port}")
    print(f"Pattern type: {pattern}")
  return port, pattern

def init_serv_sock(port):
  serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serv_sock.bind((socket.gethostbyname(socket.gethostname()), port))
  serv_sock.setblocking(True)
  serv_sock.listen(10)
  return serv_sock

def client_handler(cli_sock, lock, shared_list, book_num):
  cli_sock.setblocking(False)
  write: str = ""
  while True:
    try:
      data = cli_sock.recv(1024)
      if not data:
        print(f"Connection closed")
        break
      print(f"Received: {data.decode('utf-8')}")
      write += data.decode("utf-8")

      if lock.acquire(blocking = False):
        shared_list.add(book_num, write) #add data to this list
        lock.release()
        write = ""
    except:
      break
  lock.acquire(blocking = True)
  shared_list.write(book_num)
  lock.release()
  cli_sock.close()
  print("Close connection")

def start_server(port):
    serv_sock = init_serv_sock(port)
    lock = threading.Lock()
    book_num: int = 0
    shared_list = llist()
    print("Server started, waiting for signal")
  # Server Operation
    
    while True:
      (cli_sock, address) = serv_sock.accept()
      bookNum += 1
      print(f"Accepted Connection from {address}")
      ct = threading.Thread(target = client_handler, args=[cli_sock, lock, shared_list, book_num])
      ct.start()

# Main Script
def main():
  # Argument Manager
  port, pattern = arg_debugging()
  if port is None or pattern is None: 
    sys.exit(1)
  start_server(port)
  # Initialising Socket
if __name__ == "__main__":
    main()
