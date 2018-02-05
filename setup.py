import os

pwd = os.getcwd()
filename = 'build.sh'
filepath = os.path.join(pwd, filename)

script = """#!/bin/bash
echo '{"popo": "kuku"}' | python -m json.tool > config.json
"""

if not os.path.exists(filepath):
	with open(filepath, 'wt') as f:
		f.write(script)
