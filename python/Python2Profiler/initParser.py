from _ast import Import, ImportFrom
import ast
from typing import Any

filePath="./sampleApp.py"

class InitVisitor(ast.NodeVisitor):
    def __init__(self) :
        self.initModules=[]

    def visit_Import(self, node) -> Any:
        # now we have the location of the import package
    
    def visit_ImportFrom(self, node) -> Any:
        # we have the path to the directory which have init file in which we have the 




with open(filePath, 'r') as r:
    code = r.read()
syntaxTree  = ast.parse(code)
``