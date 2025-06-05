
equipment_data = {"name": "Dell Desktop", "serial_number": "DT40055", "product_template_id":25}
print("Before ",equipment_data)
equipment_data['template_id'] = equipment_data.pop("product_template_id")
print("After ",equipment_data)


list_of_int = [4,23,5,6,2,3,7,8]
print("Original ",list_of_int)
print("Ascending Order ", sorted(list_of_int))
print("Descending Order ", sorted(list_of_int, reverse=True))
