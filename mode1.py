from island import Island
from data_structures.bst import BinarySearchTree, BSTInOrderIterator

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        Best Case: O(n) for n length of islands, occurs when sorting is not required
        Worst Case: O(n*log(n)) for n length of islands, occurs when sorting is required
        """
        self.islands = BinarySearchTree()
        for island in islands:
            rate = -(island.money/island.marines)
            self.islands[rate] = island
        self.crew = crew

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        Best Case: O(log(n)) for n length of BST, occurs when 
        """
        selection = []
        crew_num = self.crew
        iterator = BSTInOrderIterator(self.islands.root)
        while crew_num > 0:
            try:
                node = next(iterator)
            except StopIteration:
                break
            island = node.item

            crewcost = min(island.marines, crew_num)
            crew_num -= crewcost

            selection.append((island, crewcost))
        
        return selection

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        maxloots = []
        for number in crew_numbers:
            modesim = Mode1Navigator([], number)
            modesim.islands = self.islands
            selection = modesim.select_islands()
            loots = [((x[1]*x[0].money)/x[0].marines) for x in selection]
            maxloots.append(sum(loots))
        
        return maxloots

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        old_rate = -(island.money/island.marines)
        del self.islands[old_rate]

        new_rate = -(new_money/new_marines)
        island.money = new_money
        island.marines = new_marines
        self.islands[new_rate] = island