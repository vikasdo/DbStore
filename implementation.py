from pack.abc import db
d=db()

d.create('name','vikas',1220)
d.create('address','Hyderabad',101)
d.create('phone','894546641',1)

d.read('phone')
d.delete('address')
d.read('phone')
d.read('name')
