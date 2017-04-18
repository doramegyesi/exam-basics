# EXAM: Programming Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Create a `.gitignore` file so generated files won't be committed
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.
- **Don't push your work** to GitHub until your mentor announces that the time is up


# Tasks
## 1-3. Complete the following tasks: (~90 mins)
- [Odd Average](oddavg/odd_avg.py)
- [Copy](copy/copy.py)
- [BlackJack](blackjack/black_jack.py)

### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- The solution follows [styleguide](https://google.github.io/styleguide/pyguide.html) [1p]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently with descriptive commit messages [1p]

## 4. Question time! (~10 mins) [4p]

### Name each building block of a method! [2p]

![anatomy](anatomy/anatomy_py.png)

#### Your answer:
[add your answer here]   
1:   That is a keyword to define a function.
     We need to call the function later though if we actually want to
     use it.
2:   Name of the method.
3:   Argument of the method.
4:   That is a for loop, the body of the function.
5:   A variable, will be changed by the for loop here.
6:   It is a statement that gives a value back to the calling function
and exits the function afterwards.
7:   That is the output, it will return at the end of the function.

### What is the constructor? When it is used? [2p]
#### Your answer:
The constructor is usually the first, special method of a class.
Looks like this:
def __init__()
Python will automatically call it when a new instance is made within that class.
So when I create a new instance, it is going to inherit whatever I write in the argument
of the constructor.
