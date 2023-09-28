#Returns all custmer from customer table
customers = Customer.objets.all()

#returns first customer in table
firstCustomer = Customer.objects.first()

#returns last custmer in table
lastCustomer = Customer.objects.last()

#retruns single custmer by name
customerByName = Customer.objects.get(name='Peter Piper')

#returns single cuotmer by id
customerById = Customer.objects.get(id=4)

#returns al orders related to customer
firstCustomer.order_set.all()

#retruns the cutomer name attached to the first order
order = Order.objects.first()
parentName = order.customer.name

#returns products from products table with the value of 'Outdoor' in category attribute
products = Product.objects.filter(category="Outdoor")

#Order.Sort Objects by id
leastToGreatest = Product.objects.all().order_bu('id')
greatestToLeast = Product.objects.all().order_bu('-id')

#retruns all products with tag of 'Sports'
productsFilttered = Product.objects.filter(tags_name="Sports")
