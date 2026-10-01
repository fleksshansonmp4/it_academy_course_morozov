#1
class TestCase:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return f"Test '{self.name}' [{self.status}]"

    def __repr__(self):
        return f"TestCase(name= {self.name!r} status= {self.status!r}"

t = TestCase("test_login", "passed")
print(t)
print([t])


#2
class TestSuite:
    def __init__(self, tests):
        self.tests = tests

    def __len__(self):
        return len(self.tests)

    def __bool__(self):
        return len(self.tests) > 0

suite = TestSuite(["test_login", "test_signup"])
print(len(suite))
if suite:
    print("Suite не пустой")


#3
class Results:
    def __init__(self):
        self.data = {}

    def __setitem__(self, test_name, status):
        self.data[test_name] = status

    def __getitem__ (self, test_name):
        return self.data[test_name]


#4
class TestSuite:
    def __init__(self, tests):
        self.tests = tests

    def __len__(self):
        return len(self.tests)

    def __bool__(self):
        return len(self.tests) > 0

    def __iter__(self):
        return iter(self.tests)

suite = TestSuite(["te.st_login", "test_signup"])
for test in suite:
    print(test)


#5
class Duration:
    def __init__(self, seconds):
        self.seconds = seconds

    def __add__(self, other):
        return Duration(self.seconds + other.seconds)

    def __str__(self):
        return f"{self.seconds} sec"

t1 = Duration(1.5)
t2 = Duration(2.3)
print(t1 + t2)


#6
class TestRunner:
    def __init__(self, tests):
        self.tests = tests

    def __call__(self):
        print("Тесты:", end="")
        for i in self.tests:
            print (f"{i}", end=" ")

runner = TestRunner(["test_login", "test_signup"])
runner()


#7
class Version():
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor

    def __eq__(self, other):
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        return (self.major, self.minor) < (other.major, other.minor)

v1 = Version(1, 2)
v2 = Version(1, 3)
print(v1 < v2)
print(v1 == v2)