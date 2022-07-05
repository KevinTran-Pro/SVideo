with open('list.m3u8', 'r') as file:
    output = []
    m3u8 = file.read().split('\n')

for line in m3u8:
    if line.endswith('.ts'):
        output.append('https://github.com/KevinTran-Pro/SVideo/blob/main/' + line + '?raw=true')
    else:
        output.append(line)

with open('ts.m3u8', 'w') as file:
    file.write('\n'.join(output))
