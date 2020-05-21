class Item:
    def __init__(self,name="Oreo Biscuits",price=0,category="Food"):
        self.name = name
        self.price = price
        self.category=category
        if self.price <= 0:
            raise ValueError(f'Invalid value for price, got {self.price}')
        
    def __str__(self):
        return f"{self.name}@{self.price}-{self.category}"
        
class Query:
    li = ['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
    def __init__(self,field="name", operation="EQ", value="Oreo Biscuits"):
        self.field = field
        self.operation = operation
        self.value = value
        
        if self.operation not in Query.li:
            raise ValueError(f'Invalid value for operation, got {self.operation}')
        
    def __str__(self):
        return f"{self.field} {self.operation} {self.value}"


class Store:
    def __init__(self):
        self.store_item = []
        
    def __str__(self):
        if self.store_item == []:
            return 'No items'
        return '\n'.join(map(str,self.store_item))
        
    def add_item(self,item):
        self.store_item.append(item)
     
    def count(self):
        return len(self.store_item)
        
    def filter(self,query):
        store_obj = Store()
        
        for item in self.store_item:
            filed_value = getattr(item,query.field)
            #print(filed_value)
            if query.operation == "EQ" and filed_value == query.value:
                store_obj.add_item(item)
            elif query.operation == "IN" and filed_value in query.value:
                store_obj.add_item(item)
            elif query.operation == "GT" and filed_value > query.value:
                store_obj.add_item(item)
            elif query.operation == "GTE" and filed_value >= query.value:
                store_obj.add_item(item)
            elif query.operation == "LT" and filed_value < query.value:
                store_obj.add_item(item)
            elif query.operation == "LTE" and filed_value <= query.value:
                store_obj.add_item(item)
            elif query.operation == "STARTS_WITH" and filed_value.startswith(query.value):
                store_obj.add_item(item)
            elif query.operation == "ENDS_WITH" and filed_value.endswith(query.value):
                store_obj.add_item(item)
            elif query.operation == "CONTAINS" and query.value in filed_value:
                store_obj.add_item(item)
                
                
        return store_obj
        
       
    def exclude(self,query):
        exclude_obj = Store()
        res = self.filter(query)

        for item in self.store_item:
            if item not in res.store_item:
                exclude_obj.add_item(item)
                
        return exclude_obj




'''
class Item:
    
    def __init__(self, name = None, price = 0, category = None): 
        if price <= 0:
            raise ValueError("Invalid value for price, got {}".format(price))
            
        self.name = name
        self.price = price
        self.category = category
        
    def __str__(self):
        return self.name + "@" + str(self.price) + "-" + self.category
        

class Query:
    
    operations = ['IN', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'STARTS_WITH', 'ENDS_WITH', 'CONTAINS']
    def __init__(self, field = None, operation = None, value = None):
        self.field = field
        if  operation not in self.operations:
            raise ValueError("Invalid value for operation, got {}".format(operation))
        self.operation = operation
        self.value = value
     
    def __str__(self):
        return f'{self.field} {self.operation} {self.value}'


class Store:
    def __init__(self):
        self.item_list = []
    
    def add_item(self, item = None):
        self.item_list.append(item)

    def __str__(self):
        if len(self.item_list) > 0:
            return "\n".join(map(str,self.item_list))
        else:
            return "No items"
            
    def count(self):
        return len(self.item_list)
        
    def filter(self, query):
        store_obj = Store()
        if query.operation == 'IN':
            for prod in self.item_list:
                if (prod.name in query.value) or (prod.price in query.value) or (prod.category in query.value):
                    store_obj.add_item(prod)
        
        
        elif query.operation == 'EQ':
            for prod in self.item_list:
                if query.value == prod.name:
                    store_obj.add_item(prod)
                if query.value == prod.price:
                    store_obj.add_item(prod)
                if query.value == prod.category:
                    store_obj.add_item(prod)
            
            
        elif query.operation == 'GT':
            for prod in self.item_list:
                if prod.price > query.value:
                    store_obj.add_item(prod)
            
            
        elif query.operation == 'GTE':
            for prod in self.item_list:
                if prod.price >= query.value:
                    store_obj.add_item(prod)
            
            
        elif query.operation == 'LT':
            for prod in self.item_list:
                if prod.price < query.value:
                     store_obj.add_item(prod)
            
        elif query.operation == 'LTE':
            for prod in self.item_list:
                if prod.price <= query.value:
                    store_obj.add_item(prod)
            
            
        elif query.operation == 'STARTS_WITH':
            for prod in self.item_list:
                if prod.name.startswith(query.value):
                    store_obj.add_item(prod)
                if prod.category.startswith(query.value):
                    store_obj.add_item(prod)
            
            
        
        elif query.operation == 'ENDS_WITH':
            for prod in self.item_list:
                if prod.name.endswith(query.value): 
                    store_obj.add_item(prod)
                if prod.category.endswith(query.value):
                    store_obj.add_item(prod)
        
            
            
        elif query.operation == 'CONTAINS':
            for prod in self.item_list:
                if (query.field == 'name' and prod.name.__contains__(query.value)) or (query.field == 'category' and prod.category.__contains__(query.value)):
                     store_obj.add_item(prod)
            
        return store_obj
            
    def exclude(self, query):
            
        store_obj = Store()
        if query.operation == 'IN':
            for prod in self.item_list:
                if (prod.name not in query.value) and  (prod.price not in query.value) and (prod.category not in query.value):
                    store_obj.add_item(prod)
            
            
        elif query.operation == 'EQ':
            for prod in self.item_list:
                if query.value != prod.name and query.value != prod.price and query.value != prod.category:
                    store_obj.add_item(prod)

            
        
        elif query.operation == 'GT':
            for prod in self.item_list:
                if query.value >= prod.price:
                    store_obj.add_item(prod)

            
        elif query.operation == 'GTE':
            for prod in self.item_list:
                if query.value > prod.price:
                    store_obj.add_item(prod)
                    
        elif query.operation == 'LT':
            for prod in self.item_list:
                if  query.value <= prod.price:
                    store_obj.add_item(prod)

            
        elif query.operation == 'LTE':
            for prod in self.item_list:
                if query.value < prod.price:
                    store_obj.add_item(prod)
                    
                    
        elif query.operation == 'STARTS_WITH':
            for prod in self.item_list:
                if not(prod.name.startswith(query.value) or prod.category.startswith(query.value)):
                    store_obj.add_item(prod)
              
        
        elif query.operation == 'ENDS_WITH':
            for prod in self.item_list:
                if not(prod.name.endswith(query.value) or prod.category.endswith(query.value)): 
                    store_obj.add_item(prod)
            
        elif query.operation == 'CONTAINS':
            if query.field == "name":
                for prod in self.item_list:
                    if not(prod.name.__contains__(query.value)):
                        store_obj.add_item(prod)
                        
            else:
                for prod in self.item_list:
                    if not(prod.category.__contains__(query.value)):
                        store_obj.add_item(prod)
            
        return store_obj   
'''