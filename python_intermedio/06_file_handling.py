#File Handling
import os
# .txt file

txt_file = open("learning_python/python_intermedio/my_file.txt","r+")
# print(txt_file.read())
# print(txt_file.read(30))
# print(txt_file.readline())
# print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)

