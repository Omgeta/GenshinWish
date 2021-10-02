from typing import Tuple


class PityNode:
    """ PityNode class represents and manipulates probability of a specific constellation event occuring """

    def __init__(self, value: int = 0, probability: float = 1, guarantee: bool = False, layer: int = 0):
        """
        Construct PityNode with constellation value, probability of occurence, and guarantee for the next node(s)
        """
        self.value = value
        self.probability = probability
        self.guarantee = guarantee
        self.layer = layer
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return f"Node({self.value}, {self.probability}, {self.guarantee})"

    def get_next_nodes(self) -> Tuple['PityNode']:
        """
        Find the possible nodes that could occur for the next pity,
        given the occurence of the current node.

        If the current node has the same value as the previous node,
        there is a guarantee that the next node will have a higher constellation value and no guarantee.
        Otherwise, there will be a 50/50 chance of either the same value with a guarantee or a higher value with no guarantee.

        Returns:
            Tuple of PityNode(s) for the next pity attempt, given the current PityNode.
        """
        if self.value < 7:  # Check if current constellation value is maximum
            if self.guarantee is True:  # If the next node is guaranteed to be a constellation of the limited character
                return (PityNode(self.value+1, self.probability, False, self.layer+1),
                        None)
            else:  # Else, we return both possibilities for the next pity attempt.
                return (PityNode(self.value+1, self.probability/2, False, self.layer+1),
                        PityNode(self.value, self.probability/2, True, self.layer+1))
        else:  # Return an empty Tuple to signify no more possibilities when maximum constellation is reached
            return (None, None)

    def link_left(self, other: 'PityNode'):
        """
        Link left pointer to the PityNode with a higher constellation value
        """
        if isinstance(other, PityNode) and self.value < other.value:
            self.left = other
            other.parent = self

    def link_right(self, other: 'PityNode'):
        """
        Link right pointer to the PityNode with the same constellation value
        """
        if isinstance(other, PityNode) and self.value == other.value:
            self.right = other
            other.parent = self
