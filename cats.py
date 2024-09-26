from peewee import *

db = SqliteDatabase('cats.sqlite')

class Owner(Model):
    name = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}'


class Cat(Model):
    name = CharField()
    color = CharField()
    age = IntegerField()
    owner = ForeignKeyField(Owner, backref='cats')

    class Meta:
        database = db 

    def __str__(self):
        return f' {self.id}:{self.name}, {self.color}, {self.age}, Owner: {self.owner}'
    
db.connect()
db.create_tables([Cat, Owner])
Cat.delete().execute() #clear database table

sam = Owner(name='Sam')
sam.save()
lily = Cat(name='Lily', color='Black', age=1, owner=sam)
lily.save()

print(lily)
print(lily.owner.name)

zoe = Cat(name='Zoe', color='Ginger', age=3)
zoe.save() #make sure save

holly = Cat(name='Holly', color='Tabby', age=5)
holly.save()

fluffy = Cat(name= 'Fluffly', color='Black', age=1)
fluffy.save()

cats = Cat.select()
for cat in cats:
    print(cat)

list_of_cats = list(cats) # regular Python list

"""CRUD operations
Create - insert
Read - select
Update
Delete
"""

fluffy.age = 2
fluffy.save()

print('After Fluffy age changed')
cats = Cat.select()
for cat in cats:
    print(cat)

# can update many rows if needed.
rows_modified = Cat.update(age=6).where(Cat.name=='Holly').execute()
print('After Holly age changed')
cats = Cat.select()
for cat in cats:
    print(cat)

print(rows_modified)

buzz = Cat(name='Buzz', color= 'Gray', age=3)
buzz.save()

cats_who_are_3 = Cat.select().where(Cat.age == 3)
for cat in cats_who_are_3:
    print(cat,'is three')

cat_with_l_in_name = Cat.select().where(Cat.name.contains ('b'))
for cat in cat_with_l_in_name:
    print(cat,'has b in name')

zoe_from_db = Cat.get_or_none(name='socks')
print(zoe_from_db)

cat_100= Cat.get_or_none(Cat.id == 100)
print(cat_100)

# Count,sort,limit
total = Cat.select().count()
print(total)

total_cats_who_are_5 = Cat.select().where(Cat.age ==5).count()
print(total_cats_who_are_5)

cats_by_name = Cat.select().order_by(Cat.name)
print(list(cats_by_name))

cats_by_age = Cat.select().order_by(Cat.age.desc(), Cat.name.desc())
print(list(cats_by_age))

first_3 = Cat.select().order_by(Cat.name).limit(3)
print(list(first_3))

#delete 

rows_delete = Cat.delete().where(Cat.name=='Holly').execute()
print(rows_delete, list(Cat.select()))