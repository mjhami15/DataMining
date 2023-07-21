import pandas as pd
import numpy as np
from scipy.stats import pearsonr
lines = []
with open("data.online.scores.txt") as f:
    lines = f.readlines()


final_scores = []
mid_scores = []
final_scores_normalized = []
for line in lines:
    tokens = line.split("\t")
    cut = tokens[2].split("\n")
    tokens[2] = cut[0]
    mid_scores.append(int(tokens[1]))
    final_scores.append(int(tokens[2]))
    final_scores_normalized.append((int(tokens[2]) - 87.084)/10.914)


mean_x = sum(mid_scores) / len(mid_scores)
mean_y = sum(final_scores) / len(final_scores)

print(sum((a - mean_x) * (b - mean_y) for (a,b) in zip(mid_scores,final_scores)) / len(mid_scores))
#sd print((sum2/len(lines)) ** 0.5), sum2 += (score-(sum/len(lines))) ** 2
#mean print(sum/len(lines))
#print(np.quantile(final_scores, 0.25))
#print(np.quantile(final_scores, 0.5))
#print(np.quantile(final_scores, 0.75))
#mode print(max(set(final_scores), key=final_scores.count))
