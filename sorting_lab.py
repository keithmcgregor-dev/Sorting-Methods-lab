"""
Sorting Algorithms Visualization Lab

Complete the TODO sections.

Do not use list.sort() or sorted() to perform the sorting.
"""

import random
import time
import platform
import subprocess
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# Settings
# ------------------------------------------------------------

DEFAULT_LIST_SIZE = 20
MIN_VALUE = 1
MAX_VALUE = 100
ANIMATION_DELAY = 0.10
SOUND_ENABLED = True
LOW_FREQUENCY = 200
HIGH_FREQUENCY = 1200


# ------------------------------------------------------------
# Sound Functions
# ------------------------------------------------------------

def value_to_frequency(value, min_value, max_value, low_frequency, high_frequency):
    if max_value == min_value:
        return low_frequency
    clamped_value = max(min_value, min(value, max_value))
    ratio = (clamped_value - min_value) / (max_value - min_value)
    frequency = low_frequency + ratio * (high_frequency - low_frequency)
    return frequency

def play_value_sound(value):
    """
    Play a short sound whose pitch depends on value.

    
    """
    if not SOUND_ENABLED:
        return
    try:
        frequency = int(value_to_frequency(value, MIN_VALUE, MAX_VALUE, LOW_FREQUENCY, HIGH_FREQUENCY))  
        if platform.system() == "Windows":
            import winsound
            winsound.Beep(frequency, 50)
        else:
           print("\a", end="", flush=True)  
    except  Exception:
        pass


# ------------------------------------------------------------
# Utility Functions
# ------------------------------------------------------------

def generate_list(size=DEFAULT_LIST_SIZE):

    

    
    return [random.randint(MIN_VALUE,MAX_VALUE) for i in range(size)]

def draw_list(values, title="Sorting"):
    
    plt.clf()

    plt.bar(range(len(values)), values)

    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")

    plt.pause(ANIMATION_DELAY)


# ------------------------------------------------------------
# Sorting Algorithms
# ------------------------------------------------------------

def selection_sort(values):
    """
    Sort values using Selection Sort.

    TODO:
        1. Move through each position in the list.
        2. Find the smallest value in the unsorted portion.
        3. Swap it into the correct position.
        4. Call draw_list() after an important change.
        5. Call play_value_sound() for a meaningful value.
    """
    n = len(values)
    for current in range(n):
        min = current
        for i in range(current + 1, n):
            play_value_sound(values[i])
            if values[min] > values[i]:
                min = i
        values[current], values[min] = values[min], values[current]
        draw_list(values, "Selection Sort")
    return values


            

def bubble_sort(values):
    """
    Sort values using Bubble Sort.

    TODO:
        Compare adjacent values and swap values that are
        out of order.

        Call draw_list() after each swap.
        Also call play_value_sound() for one of the swapped values.
    """
    
    n = len(values)
    for i in range(n):
        for j in range(0, n-i-1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                play_value_sound(values[j + 1])
                draw_list(values, "Bubble Sort")
    return values

def insertion_sort(values):
    """
    Sort values using Insertion Sort.

    TODO:
        Insert each new value into the correct position
        within the already-sorted portion of the list.

        Call draw_list() as values move.
        Play the value currently being inserted.
    """
    n = len(values)
    for i in range(1, n):
        key = values[i]
        j = i - 1
        play_value_sound(key)
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1
            draw_list(values, "Insertion Sort")
        values[j + 1] = key
    return values


def merge(left, right):
    """
    Merge two already-sorted lists.

    TODO:
        Return one sorted list containing all values
        from left and right.
    """
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(values):
    """
    Sort values using Merge Sort.

    TODO:
        Implement Merge Sort recursively.

    NOTE:
        Merge Sort is a little different from the other algorithms
        because recursive calls often create smaller lists.

        You may modify this function's parameters or create helper
        functions if needed to make the visualization work.

        Play each value as it is written back into the main list.
    """
    sorted_list = split(values)
    
   
    for i in range(len(values)):
        values[i] = sorted_list[i]
        play_value_sound(values[i])
        draw_list(values, "merge sort")
        
    return values
def split(mylist):
    n = len(mylist)
    if n <= 1:
        return mylist
    
    half = n // 2
    left = split(mylist[0:half])
    right = split(mylist[half:])

    return merge(left, right)

    


def quick_sort(values):
    """
    OPTIONAL CHALLENGE

    Sort values using Quick Sort.

    You may create helper functions such as partition().

    TODO:
        Implement Quick Sort and visualize important steps.
        Play the pivot or a value involved in a swap.
    """
    pass


# ------------------------------------------------------------
# Algorithm Explanations / Pseudocode
# ------------------------------------------------------------

def print_selection_info():
    """
    TODO:
        Print:
        1. A short explanation of Selection Sort in your own words.
        2. Pseudocode for Selection Sort.
    """
    print("Selection sort takes 2 different parts of your list, a sorted part and an unsorted part. It goes through each unsorted values and finds the lowest, then moves that to the front of the sorted line. It does this and then increases the size of the sorted group.It continues until there is no values left that are unsorted.")
    print("Scan through the entire unsorted portion of the list to locate the absolute smallest item, swap that minimum value into the current starting position of the unsorted segment  " \
    "go one step to the right and repeat the process until every item has been placed in its correct sorted order")
def print_bubble_info():
    """
    TODO:
        Print:
        1. A short explanation of Bubble Sort in your own words.
        2. Pseudocode for Bubble Sort.
    """
    print("it goes through the lsit and compares neighbors and swaps them if the lest is greater than the right, eventually the largest values are swapped to the top and only stops when all neighbors are greater then their left neighbor.")
    print("Walk down the list comparing each index with its right neighbor,If the left value is greater than the right value, swap them immediately " \
    "Continue making passes through the list, stopping early and exiting the loop the moment a full pass finishes with zero swaps needed")
def print_insertion_info():
    """
    TODO:
        Print:
        1. A short explanation of Insertion Sort in your own words.
        2. Pseudocode for Insertion Sort.
    """
    print("insertion sort is where you go through the list and one at a time you just take an unsorted item and put it in its correct order amoung the already sorted part of the list")
    print("go through the list, treating all elements behind the current index as a sorted sub list,Take the current item and shift larger elements to the right to make space " \
    "Drop the current item into its exact  correct position within those sorted elements, then move to the next item.")
def print_merge_info():
    """
    TODO:
        Print:
        1. A short explanation of Merge Sort in your own words.
        2. Pseudocode for Merge Sort.
    """
    print("you split the list in half down to a single item smaller list which are already sorted and then you merge all of the small list into one bigger sorted list.")
    print("cut the list in half over and over again until every sub list is made  of only a single item,Take those smaller pieces and merge them back together in the correct order " \
    "Continue combining the sorted halves upward until they all come together into one sorted list")
def print_quick_info():
    """
    OPTIONAL CHALLENGE

    TODO:
        Print:
        1. A short explanation of Quick Sort in your own words.
        2. Pseudocode for Quick Sort.
    """
    print("you take a pivot and put everything smaller to its left and everything larger to its right, then in one of those sublists find another pivot and do the same until the whole list is in order. ")
    print("Choose one element and then sort everything smaller to its left,"\
    " then go into that side of the list and pick another pivot and o the same, eventually you will go over to the right side of the orginal pivot and repeat until the whole list is in order.")

def print_info_menu():
    print()
    print("ALGORITHM INFORMATION")
    print()
    print("1. Selection Sort")
    print("2. Bubble Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Return to Main Menu")
    print()


def algorithm_info_menu():
    """
    Display explanations and pseudocode for the sorting algorithms.

    TODO:
        Complete the menu logic below if your instructor asks you
        to make changes or additions.
    """

    while True:

        print_info_menu()

        choice = input("Choice: ").strip()

        if choice == "1":
            print_selection_info()

        elif choice == "2":
            print_bubble_info()

        elif choice == "3":
            print_insertion_info()

        elif choice == "4":
            print_merge_info()

        elif choice == "5":
            print_quick_info()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please enter a number from 1 through 6.")


# ------------------------------------------------------------
# Menu
# ------------------------------------------------------------

def print_menu():
    print()
    print("SORTING VISUALIZER")
    print()
    print("1. Generate New Random List")
    print("2. Selection Sort")
    print("3. Bubble Sort")
    print("4. Insertion Sort")
    print("5. Merge Sort")
    print("6. Quick Sort")
    print("7. Algorithm Information / Pseudocode")
    print("8. Exit")
    print()


def main():

    # Interactive plotting allows the graph to update repeatedly.
    plt.ion()

    values = generate_list()

    while True:

        print()
        print("Current List:")
        print(values)

        print_menu()

        choice = input("Choice: ").strip()

        if choice == "1":
            values = generate_list()
            draw_list(values, "New Random List")

        elif choice == "2":
            working_list = values.copy()
            draw_list(working_list, "Selection Sort")
            selection_sort(working_list)
            print("Sorted List:")
            print(working_list)

        elif choice == "3":
            working_list = values.copy()
            draw_list(working_list, "Bubble Sort")
            bubble_sort(working_list)
            print("Sorted List:")
            print(working_list)

        elif choice == "4":
            working_list = values.copy()
            draw_list(working_list, "Insertion Sort")
            insertion_sort(working_list)
            print("Sorted List:")
            print(working_list)

        elif choice == "5":
            working_list = values.copy()
            draw_list(working_list, "Merge Sort")

            # You may need to modify this section depending on
            # how you implement merge_sort().
            result = merge_sort(working_list)

            if result is not None:
                working_list = result

            print("Sorted List:")
            print(working_list)

        elif choice == "6":
            working_list = values.copy()
            draw_list(working_list, "Quick Sort")

            result = quick_sort(working_list)

            if result is not None:
                working_list = result

            print("Sorted List:")
            print(working_list)

        elif choice == "7":
            algorithm_info_menu()

        elif choice == "8":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 through 8.")

    plt.ioff()
    plt.close()


if __name__ == "__main__":
    main()
