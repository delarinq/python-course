with open('my_file.txt', 'r', encoding="utf8") as f:
    my_lines = f.readlines()

with open('elif_ym.txt','w', encoding="utf8") as f:
    my_text = ''.join(my_lines)
    my_text = my_text[::-1]
    f.write(my_text)

with open('my_file.txt','r', encoding="utf8") as f:
    print(f.read())

with open('elif_ym.txt','r', encoding="utf8") as f:
    print(f.read())