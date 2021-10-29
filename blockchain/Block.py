#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 13:59:50 2021
ブロックの定義


@author: horihayato
"""

import json
import hashlib
 
class Block:
    #必要なモジュール
    def __init__(self, index, timestamp, transaction, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.property_dict = {str(i): j for i, j in self.__dict__.items()}
        self.now_hash = self.calc_hash()
 
    #ハッシュの計算
    def calc_hash(self):
        block_string = json.dumps(self.property_dict, sort_keys=True).encode('ascii')
        return hashlib.sha256(block_string).hexdigest()
    
    #トランザクションを生成
    def new_transaction(sender, recipient, amount):
        transaction = {
        "差出人": sender,
        "あて先": recipient,
        "金額": amount,
        }
        return transaction