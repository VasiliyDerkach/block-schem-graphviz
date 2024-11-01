from graphviz import Digraph

dot = Digraph()

dot.node('A', 'Start')
dot.node('B', 'Enqueue node')
dot.node('C', 'Dequeue node')
dot.node('D', 'Visit node')
dot.node('E', 'Enqueue adjacent nodes')
dot.node('F', 'End')

dot.edges(['AB', 'BC', 'CD', 'DE', 'EB', 'CF'])
dot.edge('E','F',label='New')

dot.render('bfs_algorithm', view=True)