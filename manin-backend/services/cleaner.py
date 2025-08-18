def strip_markdown(code: str) -> str:
    in_code_block = False
    out_lines = []
    for line in code.splitlines():
        stripped = line.strip()
        # Remove markdown code block markers
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        # Omit markdown headings etc. (optional)
        if not in_code_block and (stripped.startswith("#") or stripped == ""):
            continue
        out_lines.append(line)
    return "\n".join(out_lines).strip()
print("Hello")