#!/usr/bin/env python
# coding: utf-8

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
		
# 타이틀 출력 포맷
TITLE_PRINT_FORMAT = bcolors.OKBLUE+"{0:-^100}" + bcolors.ENDC

# 메뉴 출력 포맷
MENU_PRINT_FORMAT = bcolors.OKBLUE+"{0:-^92}" + bcolors.ENDC