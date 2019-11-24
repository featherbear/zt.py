#!/usr/bin/python3

network_map = {
  # "ALIAS": "NETWORK_ID",
  "earth": "8056c2e21c000001"
}

from os import system as exec
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
    exec(" ".join([CLI, "join", query]))

def leaveNetwork(*args, **kwargs):
  if len(args) != 1:
    print("Please supply network ID")
    sys.exit()
  else:
    query = args[0]
    if query in network_map:
      query = network_map[query]
    exec(" ".join([CLI, "leave", query]))

def listNetworks(*args, **kwargs):
  if len(args) != 0:
    print("No arguments required, ignoring arguments")
  exec(" ".join([CLI, "listnetworks"]))

commands = {
  "join": joinNetwork,
  "leave": leaveNetwork,
  "list": listNetworks
}

if __name__ == "__main__":
  if len(sys.argv) == 1 or sys.argv[1] not in commands:
    print(f"{sys.argv[0]} " + "|".join(commands.keys()))
    sys.exit()

  command = sys.argv[1]
  if command in commands:
    commands[command](*sys.argv[2:])
