#!/usr/bin/python3

network_map = {
  # "ALIAS": "NETWORK_ID",
  "earth": "8056c2e21c000001"
}

from os import geteuid

if geteuid() != 0:
  exit("Root access required 🥺")

import subprocess
import sys

CLI = "zerotier-cli"

def joinNetwork(*args, **kwargs):
  if len(args) != 1:
    print("Please supply network ID")
    sys.exit()
  else:
    query = args[0]
    if query in network_map:
      query = network_map[query]
    output = subprocess.run([CLI, 'join', query], stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(output)

def leaveNetwork(*args, **kwargs):
  if len(args) != 1:
    print("Please supply network ID")
    sys.exit()
  else:
    query = args[0]
    if query in network_map:
      query = network_map[query]
    output = subprocess.run([CLI, 'leave', query], stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(output)

def listNetworks(*args, **kwargs):
  if len(args) != 0:
    print("No arguments required, ignoring arguments")
  output = subprocess.run([CLI, 'listnetworks'], stdout=subprocess.PIPE).stdout.decode('utf-8').replace("200 listnetworks ", "")
  for key in network_map:
    output = output.replace(network_map[key], f"{key} ({network_map[key]})")
  print(output)

def showNetworks(*args, **kwargs):
  if len(args) != 0:
    print("No arguments required, ignoring arguments")
  for key in network_map:
    print(key, network_map[key])

commands = {
  "join": joinNetwork,
  "leave": leaveNetwork,
  "list": listNetworks,
  "show": showNetworks
}

if __name__ == "__main__":
  if len(sys.argv) == 1 or sys.argv[1] not in commands:
    print(f"{sys.argv[0]} " + "|".join(commands.keys()))
    sys.exit()

  command = sys.argv[1]
  if command in commands:
    commands[command](*sys.argv[2:])

