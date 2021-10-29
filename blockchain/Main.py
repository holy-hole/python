#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 14:15:35 2021

@author: horihayato
"""

from Block import Block
import hashlib
from datetime import datetime

class main:

    block_chain = []
     
    genesis_block = Block(0, 0, 0, "-")
    block_chain.append(genesis_block)
    
    transaction = Block.new_transaction("大島", "田中", 100)
    new_block = Block(1, str(datetime.now()),transaction , block_chain[0].now_hash)
    block_chain.append(new_block)
    
    for key, value in genesis_block.__dict__.items():
      print(key, ':', value)
     
    print("")
     
    for key, value in new_block.__dict__.items():
      print(key, ':', value)
    
    password = "pass1234".encode('ascii')
    hash = hashlib.sha256(password).hexdigest()
    print(hash)