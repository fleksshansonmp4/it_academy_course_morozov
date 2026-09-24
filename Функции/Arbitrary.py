#1
def generate_report(title, *test_names, format="html", **options):
    print(f"Отчет:{title}")
    print(f"Формат:{format}")
    print(f"Тесты:", end = " ")
    for test in test_names:
        print(test, end = " ")
    print("")
    for key, value in options.items():
        print(f"Автор: {value}")

generate_report("Daily Report", "test1", "test2", "test3", format="pdf", author="Tester")