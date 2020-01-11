#!/usr/bin/python3
import os
import json

sequences = []
max_messages = 1000
length = max_messages

for i in range(0,3):
    print(f"getting messages from localhost:800{i}")
    # get public message list from every server
    stream = os.popen(f'node ../dmclient.js localhost:800{i} "get public message list" id0')
    
    # get actual output
    output = stream.read()
    output = output.split("get public message list:1")
    output = output[1]
    
    # read json message list
    data = json.loads(output)
    sequences.append([x["msg"] for x in data][:max_messages])

min_length = min([len(x) for x in sequences])
if min_length < max_messages: # then trim
    sequences = [x[:min_length] for x in sequences]
    length = min_length

if sequences[0] == sequences[1] == sequences[2]:
    print("the system respects sequential consistency")
else:
    print("the system is not sequentially consistent")

for i in range(0, length):
    print(f"{sequences[0][i]}\t\t\t|{sequences[1][i]}\t\t\t|{sequences[2][i]}") 