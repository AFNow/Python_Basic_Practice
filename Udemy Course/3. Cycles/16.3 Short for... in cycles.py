scores = {
    'a' : 10, 
    'b' : 12,
    'c' : 5
    }
n_scores = {}
# Example without short syntax:
for key, value in scores.items():
    n_scores[key] = value * 100


# Example with the short syntax:
n2_scores = {key:value * 100 for key, value in scores.items()}


scores = [10, 12, 5]
n3_scores = {index : value * 100 for index, value in enumerate(scores)} # Enumerate uses item's index to create key 


print (n_scores)
print (n2_scores)
print (n3_scores)