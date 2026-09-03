def analyzecode(code):
    issues = []
    lines = code.splitlines()

    # File length (line-based, more meaningful than char count)
    if len(lines) > 300:
        issues.append({"type": "length", "severity": "low", "message": f"File is long ({len(lines)} lines)"})

    # Long individual lines
    for i, line in enumerate(lines, start=1):
        if len(line) > 100:
            issues.append({"type": "style", "severity": "low", "message": f"Line {i} exceeds 100 characters"})

    # Trailing whitespace
    for i, line in enumerate(lines, start=1):
        if line != line.rstrip():
            issues.append({"type": "style", "severity": "low", "message": f"Line {i} has trailing whitespace"})

    # TODO/FIXME markers
    for i, line in enumerate(lines, start=1):
        if "TODO" in line or "FIXME" in line:
            issues.append({"type": "maintenance", "severity": "low", "message": f"Line {i} contains a TODO/FIXME"})

    # Bare except clauses (bad practice)
    for i, line in enumerate(lines, start=1):
        if line.strip() == "except:":
            issues.append({"type": "bug-risk", "severity": "medium", "message": f"Line {i} uses bare except — should catch specific exceptions"})

    return issues
