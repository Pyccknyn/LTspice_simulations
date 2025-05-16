import re

# Read LTspice log file
with open('g_min100_bw_50k_worst_case.log', 'r') as f:
    lines = f.readlines()

sections = {}
current_section = None
for line in lines:
    m = re.match(r"Measurement:\s*(\w+)", line)
    if m:
        current_section = m.group(1)
        sections[current_section] = []
        continue
    if current_section and line.strip():
        if current_section == 'Gmax':
            m_val = re.search(r"\(\s*([0-9.]+)dB", line)
            if m_val:
                sections[current_section].append(float(m_val.group(1)))
        elif current_section == 'F3dB':
            m_val = re.match(r"\s*\d+\s+([0-9.]+)", line)
            if m_val:
                sections[current_section].append(float(m_val.group(1)))

# Calculate and print global min/max
for sec, vals in sections.items():
    if not vals:
        continue
    min_val = min(vals)
    max_val = max(vals)
    unit = 'dB' if sec == 'Gmax' else 'Hz'
    print(f"{sec}: min = {min_val:.4f} {unit}, max = {max_val:.4f} {unit}")
