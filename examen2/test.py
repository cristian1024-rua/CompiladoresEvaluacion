from antlr4 import *
from WhileLangLexer import WhileLangLexer
from WhileLangParser import WhileLangParser
from antlr4.tree.Tree import TerminalNode

# === Entrada de prueba ===
input_text = """
i = 0;
while (i < 10) {
  if (i == 5) {
    break;
  }
  i = i + 1;
  continue;
}
"""

# Crear flujo de entrada
input_stream = InputStream(input_text)

# === Fase léxica ===
lexer = WhileLangLexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("## 🔤 TOKENS")
for token in token_stream.tokens:
    if token.type != Token.EOF:
        # Evitar IndexError
        token_name = (
            lexer.symbolicNames[token.type]
            if 0 <= token.type < len(lexer.symbolicNames)
            else str(token.type)
        )
        print(f"  - {token_name} ('{token.text}') @line {token.line}:{token.column}")

# === Fase sintáctica ===
parser = WhileLangParser(token_stream)
tree = parser.program()

print("\n## 🌳 ÁRBOL SINTÁCTICO (toStringTree)")
print(tree.toStringTree(recog=parser))

# === Representación indentada ===
def pretty_tree(node, rule_names, level=0):
    if isinstance(node, TerminalNode):
        return "  " * level + f"TOKEN({node.getText()})"
    else:
        rule_name = rule_names[node.getRuleIndex()]
        result = "  " * level + rule_name
        for child in node.children or []:
            result += "\n" + pretty_tree(child, rule_names, level + 1)
        return result

print("\n## 🌲 ÁRBOL SINTÁCTICO (Indentado)")
print(pretty_tree(tree, parser.ruleNames))
