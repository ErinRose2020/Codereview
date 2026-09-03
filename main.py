from analyze import analyzecode
from ai import analyze_with_ai

file_path = "test.py"

def loadcode():
    with open(file_path, "r") as f:
        return f.read()

loadedcode = loadcode()

issues = analyzecode(loadedcode)
issues += analyze_with_ai(loadedcode)

for issue in issues:
    print(f"[{issue['severity'].upper()}] {issue['type']}: {issue['message']}")




