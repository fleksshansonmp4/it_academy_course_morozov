import os.path
import shutil

#1
shutil.copy("settings.ini", "settings_backup.ini")

#2
if not os.path.exists("logs_backup"):
    os.makedirs("logs_backup")

shutil.copy("app.log", "logs_backup")

#3
if os.path.exists("project_backup"):
    shutil.rmtree("project_backup")

shutil.copytree("project", "project_backup")

#4
if os.path.exists("report.txt"):
   shutil.move("report.txt", "report_old.txt")
else:
    print("Файл report.txt не найден")

#5
if "archive" not in os.listdir("logs") :
    os.makedirs("logs/archive")

for name in os.listdir("logs"):
    src = os.path.join("logs", name)
    if os.path.isfile(src):
        dst = os.path.join("logs", "archive", name)
        shutil.move(src, dst)


#6
def clean_build():
    if os.path.exists("build"):
        os.makedirs("build")
    

#7
shutil.make_archive("project_backup", "zip", "project")


#8
if os.path.exists("restored_project"):
    shutil.rmtree("restored_project")

shutil.unpack_archive("project_backup.zip", "restored_project")

#9
total, used, free = shutil.disk_usage(".")
mb = 1024 ** 2

print(f"Всего: {total / mb} MB")
print(f"Занято: {used / mb} MB")
print(f"Свободно: {free / mb} MB")

#10
if shutil.which("python") is not None:
    print(shutil.which("python"))
else:
    print("Не найдено")