import sys

print("Python interpreter path:", sys.executable)
print("\nPython module search paths:")
for path in sys.path:
    print(path)

print("\nLoaded modules:")
for module_name, module in sys.modules.items():
    print(module_name, "->", module)
