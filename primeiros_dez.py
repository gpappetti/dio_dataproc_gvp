import pandas as pd
dt = pd.read_csv('part-00000', delimiter='\t')
primeiros = dt.head(10)
primeiros.to_csv('resultado.txt')

