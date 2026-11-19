
def hanoi_solver(n):
    # Create the three rods
    rod1 = list(range(n, 0, -1))
    rod2 = []
    rod3 = []

    moves = []

    # Store the starting arrangement
    moves.append(f"{rod1} {rod2} {rod3}")

    def move_disks(n, source, auxiliary, target):
        if n == 1:
            # Move the top disk
            target.append(source.pop())

            # Record the current arrangement
            moves.append(f"{rod1} {rod2} {rod3}")
        else:
            # Move n-1 disks to the auxiliary rod
            move_disks(n - 1, source, target, auxiliary)

            # Move the largest remaining disk to the target
            target.append(source.pop())

            # Record the current arrangement
            moves.append(f"{rod1} {rod2} {rod3}")

            # Move n-1 disks from auxiliary to target
            move_disks(n - 1, auxiliary, source, target)

    # Solve the puzzle
    move_disks(n, rod1, rod2, rod3)

    return "\n".join(moves)
