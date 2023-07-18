from _ast import Import, ImportFrom
import ast
from typing import Any

filePath="./sampleApp.py"

class InitVisitor(ast.NodeVisitor):
    def __init__(self) :
        self.initModules=[]

    def visit_Import(self, node) -> Any:
        return super().visit_Import(node)
    
    def visit_ImportFrom(self, node) -> Any:
        return super().visit_ImportFrom(node)




with open(filePath, 'r') as r:
    code = r.read()
syntaxTree  = ast.parse(code)
