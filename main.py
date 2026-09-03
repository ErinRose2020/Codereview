import sys
from analyze import analyzecode
from ai import analyze_with_ai

def loadcode(file_path):
    with open(file_path, "r") as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    file_path = sys.argv[1]
    loadedcode = loadcode(file_path)

    issues = analyzecode(loadedcode)
    issues += analyze_with_ai(loadedcode)

    if not issues:
        print("No issues found.")
        return

    for issue in issues:
        print(f"[{issue['severity'].upper()}] {issue['type']}: {issue['message']}")

if __name__ == "__main__":
    main()




