import time, threading

"""
Handle multiple tasks at same time through threading
Program calculates square and cube of numbers using
multithreading

"""


def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)  # while waiting here, your cpu is doing nothing. It's idle
        print('square:', n*n)
        

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:', n*n*n)

arr = [2,3,8,9]



"""

t = time.time()
# instead of calling these function directly, use threading
# calc_square(arr)
# calc_cube(arr)

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

# join waits until the thread is done
t1.join()
t2.join()
"""

def withoutThreads():
    t = time.time()
    calc_square(arr)
    calc_cube(arr)
    print("done in : ", time.time()-t)
    print("Hah... I am done with all my work now!")
    


def withThreads():
    t = time.time()
    t1 = threading.Thread(target=calc_square, args=(arr,))
    t2 = threading.Thread(target=calc_cube, args=(arr,))

    t1.start()
    t2.start()

    # join waits until the thread is done
    t1.join()
    t2.join()
    print("done in : ", time.time()-t)
    print("Hah... I am done with all my work now!")

#withoutThreads()

withoutThreads()

#print("done in : ", time.time()-t)
#print("Hah... I am done with all my work now!")









