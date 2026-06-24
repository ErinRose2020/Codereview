def analyzecode(code):
    issues = []

    if len(code) > 500:
        issues.append("File is very long")

    return issues



