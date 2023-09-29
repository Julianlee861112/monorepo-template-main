# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!

## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
   MObject is an abstract class since it defined an **init** method for its subclass to implement.
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
   It is called destructor, the function is called when it is about to be destroyed.
1. What class does Texture inherit from?
   Image
1. What methods and attributes does the Texture class inherit from 'Image'?
   **init**, getWidth, getHeight, getPixelColoR, getPixels, setPixelsToRandomValue.
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
   I think it is a 'has-a' relationship. Because a Texture should be an attribute of Image rather than a subclass of Image.
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us?
   Yes, Python does automatically create a constructor if a constuctor is not given.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:

-   The first time the logger is constructed, it will print out:
    -   `Logger created exactly once`
-   If the logger is already initialized, it will print: - `logger already created`
    Note: You do not 'have' a constructor, but you construct the object in the _instance_ member function where you will create an object.  
    Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

    Not safe, in a single-threaded environment, creating a simple Singleton might involve checking if an instance exists and creating one if it doesn't. However, in a multi-threaded environment, multiple threads might simultaneously check if the instance exists and then proceed to create it, leading to the creation of multiple instances.
