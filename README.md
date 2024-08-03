# decorator
Here, we have a few lines of code that explain decorators in Python. hope it will be helpful 

Function Timing and Repetition Decorators

This code demonstrates the use of Python decorators to add functionality for timing the execution of functions and repeating their execution with specified delays.
Decorators Overview

    timer Decorator:
        This decorator measures and prints the execution time of the function it wraps.
        It uses the perf_counter from the time module to get high-resolution timestamps before and after the function execution.
        The execution time is calculated as the difference between the start and end times.

    repeat Decorator:
        This decorator repeats the execution of the function it wraps a specified number of times.
        It also introduces a delay between each execution using the sleep function from the time module.
        The number of repetitions and the delay between them are specified when applying the decorator.

Code Implementation

Here’s the implementation of the timer and repeat decorators and their usage on two example functions, first and second.

How It Works

    timer Decorator:
        When applied to a function, it wraps the function in a new function (wrapper) that records the start time before calling the original function.
        After the function call, it calculates the elapsed time and prints it in a formatted string.
    repeat Decorator:
        When applied to a function, it wraps the function in a new function (wrapper) that calls the original function multiple times in a loop.
        It includes a delay between each call to the function using the sleep function.

Example Functions

    first Function:
        This function prints a given text.
        Decorated with @timer and @repeat(repeat_count=2, delay=2), it will print the text twice with a 2-second delay between each print.
        The total execution time, including delays, will be measured and printed by the timer decorator.

    second Function:
        This function also prints a given text.
        Decorated with @timer and @repeat(repeat_count=3, delay=1), it will print the text three times with a 1-second delay between each print.
        The total execution time, including delays, will be measured and printed by the timer decorator.
            The first function prints "keanu" twice with a 2-second delay between prints and reports the total execution time.
    The second function prints "matrix" three times with a 1-second delay between prints and reports the total execution time.

Notes

    Ensure that the script is saved and run in a suitable environment where the time module's sleep and perf_counter functions work correctly.
    The measured times may vary slightly depending on the system's performance and load.