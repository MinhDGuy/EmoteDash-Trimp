import os

file_path = 'source/EmoteTrimp_Origin.txt'

# Kiểm tra xem tệp có tồn tại không
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    n = int(input("Enter emote slot order from 1 to 6: "))
    if n < 1 or n > 6:
        print("Invalid slot position.")
    else:
        content = content.replace('#', str(n))

        new_file_path = 'source/EmoteTrimp.ahk'
        with open(new_file_path, 'w') as file:
            file.write(content)

        print("Done!")
else:
    print("File not identified '{}'".format(file_path))

# Chờ người dùng nhập bất kỳ ký tự nào để đóng chương trình
input("Enter any character to close the program...")
