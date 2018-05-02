
import cx_Freeze
import sys
import os
import subprocess
import re


base = None
if sys.platform == "win32":
    base = "Win32GUI"



executables= [cx_Freeze.Executable("main.py", base=base)],

cx_Freeze.setup(
    name = "GNU Pyctronic",
    options= {"build_exe": {"packages":["tkinter"]}},
    version = "0.001",
    license='GPL3',
    author='Ronal Forero',
    author_email='l337.ronald@gmail.comt',
    description = '<pytronic is a program with basic tools for the calculation of analog components such as resistors, capacitors and inductors, also transformers>',
    executables = executables
)

