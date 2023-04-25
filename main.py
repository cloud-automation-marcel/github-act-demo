from datetime import datetime

file_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.txt')
with open(file_name, 'w') as fd:
    rows = [f"{file_name.replace('.txt','')}: {i}" 
            for i in range(10)]
    rows = "\n".join(rows)
    fd.write(rows)
