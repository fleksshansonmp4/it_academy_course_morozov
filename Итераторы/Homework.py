import re

#1
def even_numbers(iterable):
    for i in iterable:
        if i % 2 == 0:
            yield i

print(list(even_numbers([1, 2, 3, 4, 5, 6])))

#2
def read_line(path):
    with open(path, encoding="utf-8") as f:
        for l in f:
            yield l

def filter_lines(path, keyword):
    for line in read_line(path):
        if keyword in line:
            yield line.strip()

for line in filter_lines("log.txt", "ERROR"):
    print(line)

#3
def chain(iter1, iter2):
    for i in iter1:
        yield i

    for i in iter2:
        yield i

print(list(chain([1, 2], [3, 4])))

#4
def counter(start = 0):
    count = start
    while True:
        yield count
        count += 1

c = counter(10)
print(next(c))  # 10
print(next(c))  # 11
print(next(c))  # 12

#5
def take(n, iterable):
    for i in range(0,n):
        yield next(iterable)

c = counter(100)
print(list(take(5, c)))  # [100, 101, 102, 103, 104]

#6
text = "one two three\tfour"

res = re.sub(r'\s+', ',', text)
print(res)

#7
emails = ["a@test.com", "b@mail.ru", "user@sub.example.org"]
domains = []
for mail in emails:
    domains.append(re.findall(r"@.+", mail))

print(domains)

#8
def is_valid_date(date):
    pattern = r"\d{4}-\d{2}-\d{2}"
    return re.match(pattern,date) is not None

assert is_valid_date("2025-12-23")
assert not is_valid_date("25-12-23")

print(f"is_valid_date(2025-12-23) -> {is_valid_date("2025-12-23")}")
print(f"is_valid_date(25-12-23) -> {is_valid_date("25-12-23")}")

#9
log = '127.0.0.1 - - "GET /api/v1/users HTTP/1.1" 200 123 "-"'
print(re.search(r'" (\d{3})', log).group(1))

#10
def is_strong_password(password):
    return (
        len(password) >= 8
        and re.search("[A-Z]", password) is not None
        and re.search("[0-9]", password) is not None
    )

assert is_strong_password("Abcdef12")
assert not is_strong_password("abcdef12")
assert not is_strong_password("Abcdefgh")

#11
string = "<p>Hello <b>world</b>!</p>"

print(re.sub(r"<[^>]*>","", string))

#12
s = "name=John; age=30; city=London;"
result = dict(re.findall(r"(\w+)=(\w+)", s))
print(result)

#13

text = "Мой телефон: +7-999-123-45-67, офис: 8 (812) 555-66-77."

def find_phones(text):
    pat = r"\+7-\d{3}-\d{3}-\d{2}-\d{2}|8 \(\d{3}\) \d{3}-\d{2}-\d{2}"
    return re.findall(pat,text)

print(find_phones(text))

#14
text = "one,two;three four"
pat = r"\w+"
print(re.findall(pat, text))

#15
URL = "/api/v1/users/123/orders/456"
user_id_pat = r"users/(\d+)"
orders_id_pat = r"orders/(\d+)"

user = re.findall(user_id_pat,URL)
order = re.findall(orders_id_pat,URL)

print(user, order)