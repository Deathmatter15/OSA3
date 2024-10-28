#!/usr/bin/env python3

# Python file for a multi-threaded network server in python.

# Libraries 
import sys 
import socket
import threading
from queue import Queue

# Shared Data Structures
global_list = []
list_lock = threading.Lock()
book_count = 0

# Node Class 
class Node: 
  def __init__(self, next = None, book_next = None, next_frequent_search = None):
    self.next = next
    self.book_next = book_next
    self.next_frequent_search = next_frequent_search

# Helper Functions
  #Argument Checker
def arg_debugging(debug = True):
  if len(sys.argv) !=5:
    print("Usage: ./assignment -l <port> -p <pattern>")
    return None, None

  port: int = sys.argv[2]
  if port < 1024:
    print("Usage: 1025 or Higher Port Number.")
    return None, None
  
  pattern: str = sys.argv[4]
  if(debug):
    print(f"Script name: {sys.argv[0]}")
    print(f"Port number: {port}")
    print(f"Pattern type: {pattern}")
  return port, pattern

# Main Script
def main():
  port, pattern = arg_debugging()
  if port is None or pattern is None: 
    sys.exit(1)

#Listening for network port commentions (>1024)

#Create indiviudal threads for connection. 

#Non-blovking reads from sockets

#Receive and store data in a list. 

if __name__ == "__main__":
    main()
