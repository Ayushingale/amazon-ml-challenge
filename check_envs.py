import os
for venv in ['C:\\Users\\Ayush\\venv310\\Scripts\\python.exe',
             'C:\\Users\\Ayush\\venv\\Scripts\\python.exe',
             'C:\\Users\\Ayush\\gpu_env\\Scripts\\python.exe']:
    try:
        import subprocess
        r = subprocess.run([venv, '-c', 'import pandas, numpy, sklearn; print(pandas.__version__, numpy.__version__, sklearn.__version__)'],
                           capture_output=True, text=True, timeout=30)
        print(venv, '->', r.stdout.strip(), r.stderr.strip()[:200])
    except Exception as e:
        print(venv, 'ERROR', e)