# -*- coding: utf-8 -*-
"""task6lab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hQQUVjQqrfbUKvjBmbWF_gPKBMWBX4vu
"""

names = ["Shahzad Haider", "Eid Muhammad", "Ali Haider", "Emily Brown"]

# Using list comprehension to extract first names in lowercase
first_names = [name.split()[0].lower() for name in names]