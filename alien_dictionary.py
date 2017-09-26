import collections


class Graph(object):

    def __init__(self):
        self.adjacent_nodes = collections.OrderedDict()
        self.incoming_edges = {}

    def initialize_nodes(self, words):
        for word in words:
            for char in word:
                if char not in self.adjacent_nodes.keys():
                    self.adjacent_nodes[char] = []
                    self.incoming_edges[char] = 0

    def build_graph(self, words):
        self.initialize_nodes(words)

        curr_word = words[0]
        for i in range(1, len(words)):
            next_word = words[i]
            count_char = 0
            while curr_word[count_char] == next_word[count_char]:
                count_char += 1
                if count_char >= len(curr_word) or count_char >= len(next_word):
                    return
            self.adjacent_nodes[curr_word[count_char]] = self.adjacent_nodes[curr_word[count_char]] + [next_word[count_char]]
            curr_word = next_word

            self.calculate_incoming()

    def calculate_incoming(self):
        for key in self.adjacent_nodes.keys():
            for node in self.adjacent_nodes[key]:
                self.incoming_edges[node] += 1

    def get_incoming_edges(self):
        return self.incoming_edges

    def get_adjacent_nodes(self):
        return self.adjacent_nodes

    def get_nodes(self):
        return self.adjacent_nodes.keys()


class Solution(object):

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        gr = Graph()
        gr.build_graph(words)

        incoming_edges = gr.get_incoming_edges()
        adjacent_nodes = gr.get_adjacent_nodes()
        node_set = gr.get_nodes()

        order_list = []
        mystack = []
        for node in node_set:
            if incoming_edges[node] == 0:
                mystack = self.dfs(node, mystack, adjacent_nodes, [])
        while mystack:
            order_list.append(mystack.pop())

        return ''.join(order_list)

    def dfs(self, node, stack, adjacent_nodes, visited):
        if node in visited or node in stack:
            return stack
        else:
            visited = visited + [node]
            neighbors = adjacent_nodes[node]
            if len(neighbors) == 0:
                stack = stack + [node]
            else:
                mystack = self.dfs(neighbors.pop(0), stack, adjacent_nodes, visited)
                stack = mystack + [node]
            return stack


if __name__ == "__main__":
    solution = Solution()
    # orderList = solution.alienOrder([ "wrt", "wrf", "er", "ett", "rftt"])   #--> "wertf"
    # orderList = solution.alienOrder(["bsusz","rhn","gfbrwec","kuw","qvpxbexnhx","gnp","laxutz","qzxccww"])
    # orderList = solution.alienOrder(["ac","ab","b"]) #--> "acb"
    orderList = solution.alienOrder(["zy","zx"])  # --> "yxz"
    # orderList = solution.alienOrder(["a", "b", "ca", "cc"])    #-->"abc"
    # orderList = solution.alienOrder(["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"]) #--> ""
    print(orderList)
