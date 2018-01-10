#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "销毁"
        print "111" + '222'

if __name__ == "__main__":
    p1 = Point()
    p2 = Point()
    del p1
    del p2