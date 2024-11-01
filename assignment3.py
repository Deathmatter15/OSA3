#!/usr/bin/env python3

# Python file for a multi-threaded network server in python.
import sys 
import select
import socket
import threading
from queue import Queue

# Functions  Classes
class Node: 
  def __init__(self, data = None, next = None, book_next = None, next_frequent_search = None):
    self.next: Node = next
    self.data = data
    self.book_next: Node = book_next
    self.next_frequent_search = next_frequent_search
#End Node

class LList:
  def __init__(self):
    self.list:Node= None
    self.tail:Node= None
    self.header:Node = {}
    self.footer:Node = {}
    return
  #End init()

  def add_book_next(self, book_num, node:Node): 
    print(f"Executing add_book_next: {book_num}")
    if book_num not in self.header:
      self.header[book_num] = node
      self.footer[book_num] = node
    else:
      self.footer[book_num].book_next = node
      self.footer[book_num] = node
  #End add_book_next() 
  def add_list(self, node:Node): 
    if self.list is None:
      self.list = node
      self.tail = self.list.next
    else:
      self.tail = node
      self.tail = self.tail.next
  #End add_list()
  def add(self, book_num, write):
    print(f"Executing add() for {write}")
    new_node = Node(write)
    self.add_book_next(book_num, new_node)
    self.add_list(new_node)
    return
  #End add()
  
  def write(self, book_num):
    print(f"Execute self.write(): {book_num}")
    if(book_num < 10):
      file_name = f"book_0{book_num}.txt"
    else: 
      file_name = f"book_{book_num}.txt"
    
    if book_num in self.header:
      curr_Node = self.header[book_num]
    else:
      print(f"{book_num} not in header")
      sys.exit()
  
    with open(file_name, 'w') as file:
      while curr_Node is not None: 
        file.write(curr_Node.data)
        curr_Node = curr_Node.book_next
    return
  #End write()
#End LList

def arg_debugging(debug = True):
  if len(sys.argv) !=5:
    print("Usage: ./assignment -l <port> -p <pattern>")
    return None, None

  port = int(sys.argv[2])
  if port < 1024:
    print(f"Invalid port {port}")
    sys.exit()
  pattern: str = sys.argv[4]
  
  if(debug):
    print(f"Script name: {sys.argv[0]}")
    print(f"port number: {port}")
    print(f"Pattern type: {pattern}")
  return port, pattern
#End arg_debugging.

def client_receiver(data, write): 
    print("Executing client_receiver()")
    write += data.decode('utf-8') 
    text = write.rstrip("\n")
    print(text)
    return write
#End client_receiver

def client_handler(cli_sock, lock, shared_list, book_num):
  print("Executing client_handler()")
  cli_sock.setblocking(False)
  cli_sock.settimeout(10)
  write = ""

  while True:
    try:
      data = cli_sock.recv(1024)
      if len(data) == 0:
        break
      write = client_receiver(data, write)

    except socket.timeout:
      print("Operation timeout!")
      break
    except Exception as e:
      print(f"Exception as: {e}")
      break

    if lock.acquire(blocking = False):
      shared_list.add(book_num, write)
      lock.release()
      write = ""

  #End client thread.
  lock.acquire(blocking = True)
  shared_list.write(book_num)
  lock.release()
  cli_sock.close()
  return
#End client_handler.

def init_serv_sock(port):
  serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Solves address in use when Ctrl+C.
  serv_sock.bind(("", port))
  #serv_sock.bind('0.0.0.0', port))
  #serv_sock.bind((socket.gethostbyname(socket.gethostname()), port))
  serv_sock.setblocking(True)
  serv_sock.listen(10)
  return serv_sock
#End init_serv.

def start_server(serv_sock):
  print("Executing start_server()")
  lock = threading.Lock()
  book_num: int = 0
  shared_list = LList()
  # Server Operation
  
  while True:
    (cli_sock, address) = serv_sock.accept()
    book_num = book_num + 1
    print(f"Starting thread for {address}\n")
    ct = threading.Thread(target = client_handler, args = [cli_sock, lock, shared_list, book_num])
    ct.start()
#End start_server.

def main():
  # Accept system arguments.
  port, pattern = arg_debugging(True)
  if port is None or pattern is None: 
    sys.exit(1)

  # Initialise Server
  serv_sock = init_serv_sock(port)
  start_server(serv_sock)
#End main().

if __name__ == "__main__":
    main()
#End call().