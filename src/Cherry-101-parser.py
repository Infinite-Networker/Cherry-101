def split_statements(s):
    return [st.strip() for st in s.split(';') if st.strip()]

def parse_call(s):
    name = s.split('(')[0].strip()
    args = s[s.find('(')+1:s.rfind(')')]
    if not args.strip(): return name, []
    return name, [a.strip() for a in args.split(',')]
