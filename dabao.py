#!/usr/bin/env python3
# -\- coding: utf-8 -\-
from PyInstaller.__main__ import run
import os

# -F:打包成一个EXE文件
# -w:不带console输出控制台，window窗体格式
# --paths：依赖包路径
# --icon：图标
# --noupx：不用upx压缩
# --clean：清理掉临时文件

if __name__ == '__main__':
    # opts = ['-F', '-w', '--paths=D:\py3\Lib\site-packages\PyQt5\Qt\bin',
    #         '--paths=D:\Program\Anaconda3\envs\py35\Lib\site-packages\PySide2\plugins',
    #         '--noupx', '--clean',
    #         r'GUI.py']

    opts = ['-F', r'GUI.py']
    run(opts)

