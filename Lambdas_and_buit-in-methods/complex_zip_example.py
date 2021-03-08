midterms = [56,34,76]
finals = [75,23,72]
names = ["Mary","Sussane","Alicia"]

final_grades = [max(pairs) for pairs in zip(midterms,finals)]
final_grades_with_names = {t[0] : max(t[1],t[2]) for t in zip(names,midterms,finals)}
print(final_grades) # [75, 34, 76]
print(final_grades_with_names) #{'Mary': 75, 'Sussane': 34, 'Alicia': 76}