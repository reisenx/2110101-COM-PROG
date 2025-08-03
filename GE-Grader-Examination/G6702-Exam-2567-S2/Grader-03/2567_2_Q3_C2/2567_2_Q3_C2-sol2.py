# --------------------------------------------------
# File Name : 2567_2_Q3_C2-sol2.py
# Problem   : Grandson
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------


# Define the Node class to represent each node in the tree
class Node:
    # Initialize the node with a name and its children
    def __init__(self, name: str) -> None:
        self.name = name
        self.children = set()

    # Add a child node to the current node
    def add_child(self, child: "Node") -> None:
        child.parent = self
        self.children.add(child)

    # Count the number of grandchildren for the current node
    def count_grandchildren(self) -> int:
        total_grandchildren = 0
        for child in self.children:
            total_grandchildren += len(child.children)
        return total_grandchildren


# Main function
def main():
    # Initialize a dictionary to store nodes
    nodes = {}

    # Input the number of relationships and build the tree
    n = int(input())
    for _ in range(n):
        # Extract parent node and child node from input
        parent, child = input().strip().split()
        # Initialize parent and child nodes if they do not exist
        if parent not in nodes:
            nodes[parent] = Node(parent)
        if child not in nodes:
            nodes[child] = Node(child)
        # Add the child node to the parent node
        nodes[parent].add_child(nodes[child])

    # Input the names of nodes to query
    query_nodes = input().strip().split()
    # Output the number of grandchildren for each queried node
    for node in query_nodes:
        if node in nodes:
            print(nodes[node].count_grandchildren())
        else:
            print(0)


# Run the main function
main()
