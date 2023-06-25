import protobuf_example_pb2  # 导入生成的protobuf模块
from google.protobuf import text_format

p = protobuf_example_pb2.p()
p.name = "John"
p.id = 123
p.email = "john@example.com"

phone_number = p.phones.add()
phone_number.number = "1234567890"
phone_number.type = protobuf_example_pb2.p.MOBILE

address = protobuf_example_pb2.AddressBook()
address.people.extend([p])

with open("address.bin", "wb") as f:
    f.write(address.SerializeToString())

new = protobuf_example_pb2.AddressBook()
with open("address.bin", "rb") as f:
    new.ParseFromString(f.read())

print("Name:", new.people[0].name)
print("ID:", new.people[0].id)
print("Email:", new.people[0].email)
print("Phone Number:", new.people[0].phones[0].number)
print("Phone Type:", new.people[0].phones[0].type)
