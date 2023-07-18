from _ast import Import, ImportFrom
# from typing import Any
import compiler
from compiler.visitor	import ASTVisitor
# from compiler.ast import NodeVisitor

import ast
import sys
import os
import logging


code="""
from pandas import DataFrame, From_Dict
from common.apps.attribution import Ex1
import numpy


def function1(a1, a2):
	a = a1 + a2
	return a

def function2(name):
	print("function 2")
	def functionIn():
		print("inside functionIn")
	print(name)
	functionIn()
    


a=function1(12,23)
print(a)
function2("Void Simple function")
"""

class Visitor(ast.NodeVisitor):
    imports=[]
    modules={}
    # def __init__(self):
        # super().__init__()
        # self.imports=[]
        # self.modules={}
        
		                
    def visit_Import(self, node):
         for name in node.names:
                self.imports.append(name.name)
        
		# return super().visit_Import(node)
    def visit_ImportFrom(self, node):
        # print(ast.dump(node))
        # print(node.__class__.__name__)
        # print(node.module)
        listOfPackages=[]
        for name in node.names:
            listOfPackages.append(name.name)
        self.modules[node.module]=listOfPackages



# syntaxTree = compiler.parse(code)
def createSyntaxTree(code):
	syntaxTree = ast.parse(code)
	return syntaxTree



def parseSyntaxTree(syntaxTree):
	visitor = Visitor()	
	visitor.visit(syntaxTree)
	for module, names in visitor.modules.items():
		print("module : ",module)
		for name in names:
			print("name is :", name)

	for importModuleName in visitor.imports:
		print(importModuleName)



def main():  
	allPaths = sys.path
	tree = createSyntaxTree(code)
	parseSyntaxTree(tree)
	return
	for path in allPaths:
		try:
			print(os.listdir(path))
			print("*********")
		except OSError:
			logging.exception("not a directory")
	# print(allPaths)
	# sys.exit()




if __name__ == "__main__":
	main()