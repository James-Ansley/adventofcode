import re

with open('../input_files/day19') as f:
    rule_strings, messages = f.read().split('\n\n')

    rule_strings = dict(rule.split(': ') for rule in rule_strings.splitlines())
    messages = messages.splitlines()


def get_expr(n, opt_rules=None):
    if opt_rules and n in opt_rules:
        return opt_rules[n]

    if m := re.match(r'"(\w)"', rule_strings[n]):
        return m.group(1)

    expr = []
    for rule in rule_strings[n].split(' | '):
        values = rule.split()
        expr.append(''.join(get_expr(v, opt_rules) for v in values))
    expr = '|'.join(expr)
    return fr'(?:{expr})'


rule0 = get_expr('0')
total = sum(bool(re.fullmatch(rule0, message)) for message in messages)
print(total)

rule42 = get_expr('42')
rule31 = get_expr('31')
rule8 = fr'(?:{rule42}+)'
rule11 = fr"(?:{'|'.join(f'{rule42}{{{n}}}{rule31}{{{n}}}' for n in range(1, max(map(len, messages)) // 4))})"
opt_rules = {'8': rule8, '11': rule11}

rule0 = get_expr('0', opt_rules)
total = sum(bool(re.fullmatch(rule0, message)) for message in messages)
print(total)
