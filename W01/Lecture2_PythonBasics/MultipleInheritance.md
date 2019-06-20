# Self-reading topic: MULTIPLE INHERITANCE

## Definition

A class can inherit from more than one parent class. 
Java does not support it, while C++ and Python do. Example implementation:

`class ChildClass(MotherClass, FatherClass,...)`

## Diamond Problem

![](https://www.python-course.eu/images/multiple_inheritance_diamond.png)

Occurs when two classes `B` and `C` inherits from class `A`, and there is a class `D` inheriting
from both class `B` and `C`.

Given `d` is an instance of `D`. 
If both `B` and `C` override a method `m` of `A`, the output of `d.m()` depends on the order
of inherited classes in the class header of `D`:
* `class D(B, C)`: `d.m()` calls `m` method of class `B`
* `class D(C, B)`: `d.m()` calls `m` method of class `C`

Otherwise, if only either `B` or `C` overrides method `m` of `A`:
* Python 2.7: `d.m()` calls `A.m()` (old-styled class)
* Python 3: `d.m()` calls `B.m()` or `C.m()`

Rules in old-styled classes: depth-first and then left-to-right

