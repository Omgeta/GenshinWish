from structures.node import PityNode
from typing import List


class PityTree:
    def __init__(self, root: PityNode = PityNode()):
        self.root = root

    def construct_tree(self, depth: int):
        """
        Construct a probability tree from the root PityNode
        by getting next possible nodes until desired depth is reached
        or a branch has reached maximum constellation value of 7
        """
        # initialize at the root node
        current_layer = [self.root]
        next_layer = []
        current_depth = 0

        while current_depth < depth and len(current_layer) > 0:
            for node in current_layer:
                # calculate next possibilities, given the current PityNode
                next_nodes = node.get_next_nodes()
                # add pointers from current node to the next possible nodes
                node.link_left(next_nodes[0])
                node.link_right(next_nodes[1])

                # add the new nodes to the next layer for calculation later
                next_layer.extend([n for n in next_nodes if n is not None])

            # once all the current nodes have been iterated through, move onto the next layer
            current_layer = next_layer
            next_layer = []
            current_depth += 1

    def get_layer(self, layer_depth: int) -> List[PityNode]:
        """
        Get the PityNodes of a given layer depth or earlier if the branch ended early

        Returns:
            List of PityNodes
        """
        # initialize at the root node
        final_nodes = []
        current_layer = [self.root]

        # traverse through nodes for every layer
        for depth in range(layer_depth):
            next_layer = []
            for i in range(len(current_layer)):
                node = current_layer[i]

                # add final node of branch if no more new nodes possible
                if node.left is None:
                    final_nodes.append(node)
                else:  # add the connected nodes to the next layer to be iterated over
                    next_layer.append(node.left)
                    if node.right is not None:
                        next_layer.append(node.right)
            current_layer = next_layer
        final_nodes.extend(current_layer)

        return final_nodes

    @staticmethod
    def calc_total_probability(layer: List[PityNode]) -> List[float]:
        """
        Calculates the total probability of a constellation value occurring in a given layer by summing probabilities

        Returns:
            Array of length 8 with probability of the number of copies of a character at the respective index
        """
        # Create empty array of probabilities for each constellation value
        total_probabilities = [0] * 8

        # add all the probabilities for a constellation value to the respective index
        for node in layer:
            total_probabilities[node.value] += node.probability

        return total_probabilities
