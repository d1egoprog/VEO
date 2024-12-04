
#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Read an Existing Knowledge Graph and Execute a Query file

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
"""

__author__ = "Diego Rincon-Yanez"
__copyright__ = "MIT"
__date__ = "2024/06/20"
__deprecated__ = False
__status__ = "stable"
__version__ = "0.0.1"

from rdflib import Graph

def load_knowledge_graph(file_path):
    """
    Load the knowledge graph from an RDF file.

    Parameters:
    - file_path: str, path to the RDF file containing the knowledge graph.

    Returns:
    - graph: rdflib.Graph, the loaded knowledge graph.
    """
    graph = Graph()
    graph.parse(file_path, format="ttl")  # Adjust the format if your file is not in Turtle format.
    return graph

def query_knowledge_graph(graph, query):
    """
    Query the knowledge graph using SPARQL.

    Parameters:
    - graph: rdflib.Graph, the loaded knowledge graph.
    - query: str, the SPARQL query string.

    Returns:
    - results: list, query results.
    """
    results = graph.query(query)
    return results

if __name__ == "__main__":
    
    # Path to the knowledge graph file
    kg_file_path = 'knowledge_graph.ttl'

    with open('queries/query1.sparql') as query_file:
        sparql_query = query_file.read()

    # Load the knowledge graph
    kg = load_knowledge_graph(kg_file_path)

    # Query the knowledge graph
    results = query_knowledge_graph(kg, sparql_query)

    # Print the results
    for row in results:
        print(row)
