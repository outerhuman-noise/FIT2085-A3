from island import Island
from data_structures.bst import BinarySearchTree, BSTInOrderIterator

class Mode2Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117

    Saving the number of crews and initialising an empty list to add the islands to in __init__,
    islands are added to the list in add_islands to save them.

    In simulate_day, the islands are sorted into a Binary Search Tree (provided they have a non
    zero amount of money) based on the maximum amount of points they can give (negative in order
    to serve the greatest amount of points first). In Order Iterator then returns this most
    efficient island and extracts the greatest amount of points possible before adjusting the
    island attributes to reflect its looted status. If the island is not completely looted then
    it is deleted and reinserted into the 
    """

    def __init__(self, n_pirates: int) -> None:
        """
        Student-TODO: Best/Worst Case
        Best & Worst Case: O(1), only saves input param and creates empty list
        """
        self.pirates = n_pirates
        self.islands_source = []

    def add_islands(self, islands: list[Island]):
        """
        Student-TODO: Best/Worst Case
        Best & Worst Case: O(i) for i length of islands, as it only appends to the list
        """
        for island in islands:
            self.islands_source.append(island)

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        Student-TODO: Best/Worst Case
        Best Case:  O(n + c) for n islands with non zero money and c captains 
                    participating, occurs when islands don't require deletion 
                    and reinsertion (they are completed in one turn)
        Worst Case: O(n + c*log(n)) for the same variables as above, occurs
                    when islands are not completed in one turn (deletion and
                    reinsertion required)
        """
        fights = []

        islands = BinarySearchTree()
        for island in self.islands_source:
            if not (island.money == 0 or island.marines == 0):
                crewlost = min(island.marines, crew)
                points = -(2*(crew - crewlost) + min(crewlost*island.money/island.marines, island.money))

                islands[points] = island

        iterator = BSTInOrderIterator(islands.root)
        node = next(iterator)

        for _ in range(self.pirates):
            if not node == None:
                island = node.item
                crewlost = min(island.marines, crew)

                island.money -= min(crewlost*island.money/island.marines, island.money)
                island.marines -= crewlost

                del islands[node.key]
                
                if not (island.money == 0 or island.marines == 0):
                    newpoints = -(2*(crew - crewlost) + min(crewlost*island.money/island.marines, island.money))
                    islands[newpoints] = island
                    
                    iterator = BSTInOrderIterator(islands.root)
                
                try:
                    node = next(iterator)
                except StopIteration:
                    node = None
            else:
                island = None
                crewlost = 0
            
            fights.append((island, crewlost))
        
        return fights