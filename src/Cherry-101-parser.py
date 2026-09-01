def split_statements(s):
    """Split on newlines and semicolons; skip blank lines and // comments.

    The published example uses newlines, not semicolons. The original
    implementation only split on ';', so the example never executed.
    """
    parts = []
    text = (s or "").replace("\r\n", "\n")
    for line in text.split("\n"):
        line = line.strip()
        if not line or line.startswith("//"):
            continue
        for st in line.split(";"):
            st = st.strip()
            if st and not st.startswith("//"):
                parts.append(st)
    return parts

def parse_call(s):
    name = s.split('(')[0].strip()
    args = s[s.find('(')+1:s.rfind(')')]
    if not args.strip(): return name, []
    return name, [a.strip() for a in args.split(',')]
