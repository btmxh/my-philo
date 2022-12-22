import glob
import os

mds = glob.glob('*.md')
links = ""
for md in mds:
    html = md[:-3] + ".html"
    os.system(f'markmap {md} -o build/{html}')
    links += f'<li><a href="{html}">{md[:-3]}</a></li>'

indexhtml = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>decuongtriethoc</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
</head>
<body>
    <ul>
        {links}
    </ul>
</body>
</html>'''

with open('build/index.html', 'w', encoding='utf-8') as f:
    f.write(indexhtml)
