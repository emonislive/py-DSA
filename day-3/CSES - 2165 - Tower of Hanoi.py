def towerOfHanoi(n, source, destination, middle):
    # Base case:
    # No disks means there is nothing to move.
    if n == 0:
        return

    # ! STEP 1:
    # Move the top (n-1) smaller disks from the source rod to the auxiliary (middle) rod
    # This frees the largest disk (disk n), which is sitting at the bottom of the source rod
    towerOfHanoi(n - 1, source, middle, destination)

    # ! STEP 2:
    # Now that the largest disk is free, move it directly from the source rod to the destination rod.
    #
    # ! IMPORTANT:
    # The recursive call above only handled (n-1) disks.
    # It NEVER moves the largest disk.
    # This line is the ONLY place where disk n is moved.
    print(source, destination)

    # ! STEP 3:
    # Move the (n-1) smaller disks from the auxiliary rod onto the largest disk at the destination rod.
    towerOfHanoi(n - 1, middle, destination, source)


def main():
    # Number of disks
    disks = int(input())

    # Minimum moves required = 2^n - 1
    moves = 2 ** disks - 1
    print(moves)

    # Convention:
    # Rod 1 -> Source
    # Rod 2 -> Auxiliary
    # Rod 3 -> Destination
    towerOfHanoi(disks, 1, 3, 2)


main()