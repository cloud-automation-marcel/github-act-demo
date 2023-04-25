from datetime import datetime

file_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.txt')
with open('output_data.txt', 'a') as fd:
    rows = [f"\{file_name.replace('.txt','')}: {i}" 
            for i in range(10)]
    rows = "\n".join(rows) 
    fd.write('\n')
    fd.write(rows)
