import xml.etree.ElementTree as ET

#1
tree = ET.parse("employees.xml")
root = tree.getroot()
print(root.tag)

count_employee = 0
sum_salary = 0
for elem in root.findall('.//salary'):
    sum_salary += int(elem.text)
    count_employee += 1

print(f"Количество сотрудников: {count_employee}")
print(f"Суммарная зарплата: {sum_salary}")

#2
def dummy_test(data):
    if data <= 5:
        return True
    else:
        return False

tests = [
(dummy_test(5), True),
(dummy_test(7), True),
(dummy_test(6), False),
(dummy_test(2), True),
(dummy_test(4), False),
(dummy_test(8), True),
(dummy_test(1), False),
]

fail_tests_counter = 0
count_tests = len(tests)

for result, expected in tests:
    try:
        assert result == expected
    except AssertionError as e:
        print(f"Тест не пройден! Ожидается что пароль результат {expected}, " +
              f"но фактический результат {result}")
        fail_tests_counter += 1
        continue
    print("Тест прошёл!")

print(fail_tests_counter)
data = {
    'tests_count' : count_tests,
    'complete_tests_count': count_tests - fail_tests_counter,
    'fail_tests_count': fail_tests_counter,
    'complete_tests_percent': round((count_tests - fail_tests_counter) / count_tests * 100, 2)
}

root = ET.Element('5.xml')

for key, value in data.items():
    child = ET.SubElement(root, key)
    child.text = str(value)

tree = ET.ElementTree(root)
ET.indent(tree, space="    ")
tree.write("5.xml", encoding="utf-8", xml_declaration=True)