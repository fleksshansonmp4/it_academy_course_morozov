#5
def log_message(path, message):
    with open(path, "a") as f:
        f.write(f"<{message}>\n")

log_message("app.log", "Test started")
log_message("app.log", "Test finished")


#6
def read_first_chars(path, n):
    with open(path, "r") as f:
        content = f.read(n)
    return content

print(read_first_chars("app.log",5))


#7
def filter_file(src, dst, keyword):
    with open(src, "r") as r:
        with open (dst, "w") as w:
            content = r.readlines()
            for l in content:
                if "ERROR" in l:
                    w.write(f"{l}")

filter_file("app.log", "errors.log", "ERROR")



#8
def sum_file(path):
    sum = 0
    with open(path, "r") as f:
        for l in f:
            sum += int(l)
    return sum

assert sum_file("numbers.txt") == 1 + 2 + 3 + 4 + 5


#9
def copy_binary(src, copy):
    with open(src, "rb") as r:
        data = r.read()
        with open(copy, "wb") as w:
            w.write(data)

copy_binary("image.png", "image_copy.png")


#10
def read_config(path):
    result = {}
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            key, value = line.split("=", 1)
            result[key.strip()] = value.strip()
    return result

print(read_config("config.txt"))