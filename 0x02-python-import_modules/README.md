    You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

guillaume@ubuntu:~/0x02$ ./2-args.py 
0 arguments.
guillaume@ubuntu:~/0x02$ ./2-args.py Hello
1 argument:
1: Hello
guillaume@ubuntu:~/0x02$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
guillaume@ubuntu:~/0x02$ 

Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: 0x02-python-import_modules
    File: 2-args.py

3. Infinite addition
mandatory
Score: 0.00% (Checks completed: 0.00%)

Write a program that prints the result of the addition of all arguments

    The output should be the result of the addition of all arguments, followed by a new line
    You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
    Your code should not be executed when imported

guillaume@ubuntu:~/0x02$ ./3-infinite_add.py
0
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
89
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10 -40 -300 89 
-162
guillaume@ubuntu:~/0x02$ 

Last but not least, your program should also handle big numbers. And the good news is: if your program works for the above example, it will work for the following example:

guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 1111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999990000000000000000000 11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334567788888899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334568900000011111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999989999999999999999999
guillaume@ubuntu:~/0x02$

Remember how you did (or did not) do it in C? #pythoniscool

Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: 0x02-python-import_modules
    File: 3-infinite_add.py

4. Who are you?
mandatory
Score: 0.00% (Checks completed: 0.00%)

Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).

    You should print one name per line, in alpha order
    You should print only names that do not start with __
    Your code should not be executed when imported
    Make sure you are running your code in Python3.8.x (hidden_4.pyc has been compiled with this version)

guillaume@ubuntu:~/0x02$ curl -Lso "hidden_4.pyc" "https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc"
guillaume@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
guillaume@ubuntu:~/0x02$ 

Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: 0x02-python-import_modules
    File: 4-hidden_discovery.py

5. Everything can be imported
mandatory
Score: 0.00% (Checks completed: 0.00%)

Write a program that imports the variable a from the file variable_load_5.py and prints its value.

    You are not allowed to use * for importing or __import__
    Your code should not be executed when imported

guillaume@ubuntu:~/0x02$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""

guillaume@ubuntu:~/0x02$ ./5-variable_load.py
98
guillaume@ubuntu:~/0x02$

Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: 0x02-python-import_modules
    File: 5-variable_load.py

