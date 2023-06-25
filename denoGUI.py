import tutorial_pb2

p = tutorial_pb2.Person()
p.name = "John"
p.id = 123
p.email = "john@example.com"

phone_number = p.phones.add()
phone_number.number = "1234567890"
phone_number.type = tutorial_pb2.Person.MOBILE

address = tutorial_pb2.AddressBook()
address.people.extend([p])

with open("address.bin", "wb") as f:
    f.write(address.SerializeToString())

new = tutorial_pb2.AddressBook()
with open("address.bin", "rb") as f:
    new.ParseFromString(f.read())

# 使用循环打印所有人员信息
for person in new.people:
    print("Name:", person.name)
    print("ID:", person.id)
    print("Email:", person.email)

    for phone in person.phones:
        print("Phone Number:", phone.number)
        print("Phone Type:", phone.type)
