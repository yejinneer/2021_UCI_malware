#!/usr/bin/env python
# coding: utf-8

import os
from TextFormat import bcolors, MENU_PRINT_FORMAT, TITLE_PRINT_FORMAT

# BinaryFile Class
class BinaryFile:
    # 파일 경로
    path = None
    # 파일 사이즈
    file_size = None
    # 파일 -> 바이트 어레이
    bytes_array = None
    
    # 초기화 ( 파일 경로 )
    def __init__(self, path):
        try:
            if(path is not None):
                string = None
                self.path = path
                self.file_size = os.stat(path).st_size * 0.001
                self.name = os.path.basename(self.path)
                self.name = self.name.replace(".pcap", "")

                # 파일읽음 -> 바이트 어레이 -> self.bytes_array 에 담기
                with open(path, 'rb') as f:
                    string = f.read()

                self.bytes_array = string
        except Exception:
            print("잘못된 파일 경로 입니다.")
            return None

    # 헥스 단위 여백을 추가하기 위한 메소드
    def make_hex_sep(self, string):
        new_string = ""
        cnt = 0
        hex_cnt = 0

        for s in string:
            cnt = cnt + 1

            new_string = new_string + s

            if(cnt == 2):
                new_string = new_string + " "
                cnt = 0

        return new_string
    
    # 파일 Info 출력
    def print_info(self):
        path_str = "file path : {}".format(self.path)
        size_str = "file size : {}KB".format(self.file_size)
        title_str = TITLE_PRINT_FORMAT.format(" FILE INFO ")
        
        print(title_str)
        print("{1}#{2}{0}{1}#{2}".format(path_str.center(len(title_str)-11), bcolors.OKBLUE, bcolors.ENDC))
        print("{1}#{2}{0}{1}#{2}".format(size_str.center(len(title_str)-11), bcolors.OKBLUE, bcolors.ENDC))
        print("-" * (len(title_str) - 9))
        
    # 파일의 byte array를 반환한다. 추가로 byte array의 길이도 반환함.
    def get_bytes_array(self):
        return self.bytes_array, len(self.bytes_array)