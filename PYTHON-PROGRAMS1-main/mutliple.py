class father:
    def father_method():
        return"this is father method"
    
class mother:
    def mother_method():
        return "this is mother method"
    
class child(father,mother):
    def child_method():
        return "this is child method derived from father & mother method"
    
obj1=father
obj2=mother
obj3=child

print(obj1.father_method())
print(obj2.mother_method())
print(obj3.child_method())