class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        """
        Returns the node with the matching 'id' using depth-first traversal.
        Returns None if not found.
        """

        def dfs(node):
            if node['id'] == id:
                return node
            for child in node['children']:
                found = dfs(child)
                if found:
                    return found
            return None

        return dfs(self.root) if self.root else None