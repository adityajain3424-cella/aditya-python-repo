marks={"mudrik":50,"aditya":100}
update_marks={}
for key in marks:
  update_marks[key]=marks[key]*2
print(update_marks)
print({i:s*2 for i,s in marks.items()})
