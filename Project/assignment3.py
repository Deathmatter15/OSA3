#!/usr/bin/env python3
# Libraries 
import sys 

# main script
def main():
  if len(sys.argv) !=5:
    print("Usage: ./assigment -l <port> -p <pattern>")
    return

  port = sys.argv[2]
  pattern = sys.argv[4]
  
  print(f"Script name: {sys.argv[0]}")
  print(f"Port number: {port}")
  print(f"Pattern type: {pattern}")

#Python file for a multi-threaded network server in python.

#Listening for network port commentions (>1024)

#Create indiviudal threads for connection. 

#Non-blovking reads from sockets

#Receive and store data in a list. 

if __name__ == "__main__":
    main()
