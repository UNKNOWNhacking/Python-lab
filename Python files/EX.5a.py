language1={"C","C++","JAVA"}
language2={"PYTHON","ORACLE","C"}
print(language1)
print(language2)
language1.add("SQL")
print(language1)
language1.remove("SQL")
print(language1)
#Set Methods
print(language1|language2)
print(language2.union(language1))
print(language1&language2)
print(language1.intersection(language2))
print(language1-language2)
print(language2.difference(language1))

language1.pop()
print(language1)
language2.discard("ORACLE")
print(language2)

print("-------------------------")

#Dictionary methods
programming_language={
  "First year": "PYTHON",
  "Second year": "C",
  "Third year": "JAVA"
}
programming_language.update({"Second year": "C++"})
print(programming_language)


"""
{'C', 'JAVA', 'C++'}
{'C', 'PYTHON', 'ORACLE'}
{'C', 'SQL', 'JAVA', 'C++'}
{'C', 'JAVA', 'C++'}
{'C', 'C++', 'JAVA', 'ORACLE', 'PYTHON'}
{'C', 'JAVA', 'ORACLE', 'C++', 'PYTHON'}
{'C'}
{'C'}
{'C++', 'JAVA'}
{'PYTHON', 'ORACLE'}
{'JAVA', 'C++'}
{'C', 'PYTHON'}
-------------------------
{'First year': 'PYTHON', 'Second year': 'C++', 'Third year': 'JAVA'}
"""
