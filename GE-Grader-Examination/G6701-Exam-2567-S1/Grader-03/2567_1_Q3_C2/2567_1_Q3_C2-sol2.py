# --------------------------------------------------
# File Name : 2567_1_Q3_C2-sol2.py
# Problem   : The Python
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Initialize dictionaries to store nodes and their total values
nodes = {}
total_values = {}


# Define the Node class to represent each node in the tree
class Node:
    # Initialize the node with a name, children, parent, and value
    def __init__(self, name):
        self.name = name
        self.children = set()
        self.parent = None
        self.value = 0

    # Define the integer representation of the node
    def __int__(self):
        return self.value

    # Add a child node to the current node
    def add_child(self, child):
        child.parent = self
        self.children.add(child)

    # Add a parent node to the current node
    def add_parent(self, parent):
        self.parent = parent
        parent.add_child(self)

    # Add a value to the current node
    def add_value(self, value):
        self.value += value

    # Check if the node has any children
    def has_child(self):
        return len(self.children) > 0

    # Check if the node has a parent
    def has_parent(self):
        return self.parent is not None


# Build a tree from n edges
def build_tree(n):
    for _ in range(n):
        # Extract child node, parent node, and child node value from input
        child, parent, value = input().strip().split(",")
        # Initialize child and parent nodes if they do not exist
        if child not in nodes:
            nodes[child] = Node(child)
        if parent not in nodes:
            nodes[parent] = Node(parent)

        # Add the child node to the parent node and set the value
        nodes[child].add_parent(nodes[parent])
        nodes[child].add_value(int(value))

        # Add the child node to the parent's children set
        nodes[parent].add_child(nodes[child])


# Recursively calculate the total values for each node
def get_total_values(node):
    # Check if the total value for this node has already been calculated
    if node.name in total_values:
        return total_values[node.name]

    # Initialize the total value with the node's own value
    total_value = int(node)
    # Recursively add the total values of all child nodes
    for child in node.children:
        total_value += get_total_values(child)
    # Store the total value for this node
    total_values[node.name] = total_value
    # Return the total value
    return total_value


# Display the total values for all root nodes of trees
def display_root_total_values():
    # Find all root nodes and calculate their total values
    root_values = []
    for node in nodes.values():
        # Check if the node is a root (has no parent)
        if not node.has_parent():
            # Store the total value and name of the root node
            total_value = get_total_values(node)
            root_values.append((-total_value, node.name))

    # Output the root values by total value in descending order
    # and name in ascending order
    for total_value, name in sorted(root_values):
        print(f"Boss {name} {-total_value}")


# Main function to read input and build the tree
def main():
    # Build the tree based on the number of edges
    n = int(input())
    build_tree(n)
    # Display the total values for all root nodes
    display_root_total_values()


# Call the main function to execute the program
main()
