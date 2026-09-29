import language_tool_python
tool = language_tool_python.LanguageTool("es")

text = "Ayer yo a la tienda y compre unos manzanas."
for match in tool.check(text):
    print(match.message)
    print("Suggestions:", match.replacements[:3])
    print()

tool.close()