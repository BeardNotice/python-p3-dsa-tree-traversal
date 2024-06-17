class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]

    while nodes_to_visit:
      elements = nodes_to_visit.pop()
      if elements['id'] == id:
        return elements
      
      nodes_to_visit = nodes_to_visit + elements['children']

    return None
      
