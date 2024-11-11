MAX = 1000
MIN = -1000

# Minimax function with Alpha-Beta pruning
def minimax(depth, node_index, maximizing_player, values, alpha, beta):
    # Base case: if depth reaches 3, return the value at the current node
    if depth == 3:
        return values[node_index]

    if maximizing_player:
        best = MIN
        # Explore both child nodes (left and right)
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            
            # Alpha-Beta pruning: if beta is less than or equal to alpha, break out of the loop
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        # Explore both child nodes (left and right)
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha-Beta pruning: if beta is less than or equal to alpha, break out of the loop
            if beta <= alpha:
                break
        return best

# Main function to interact with the user
def main():
    # Take user input for values (for a tree of 8 leaves)
    values = []
    print("Enter values for the leaf nodes:")
    for i in range(8):
        value = int(input(f"Enter value for node {i}: "))
        values.append(value)

    # Print the user-input values
    print("\nUser-input values:", values)

    # Call the minimax function with the user-input values
    result = minimax(0, 0, True, values, MIN, MAX)
    print("\nThe optimal value is:", result)

# Directly call the main function
main()

'''Enter values for the leaf nodes:
Enter value for node 0:  6
Enter value for node 1:  4
Enter value for node 2:  3
Enter value for node 3:  1
Enter value for node 4:  0
Enter value for node 5:  2
Enter value for node 6:  7
Enter value for node 7:  9

User-input values: [6, 4, 3, 1, 0, 2, 7, 9]

The optimal value is: 3'''