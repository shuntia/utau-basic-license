inputs = {}
out = ""
replacing = False
replacingstr = ""
# fmt=input("Enter the output format[md]: ")

with open("ja-basic.md", "r", encoding="utf-8") as f:
    for i in f.read():
        match i:
            case "[":
                replacing = True
            case "]":
                replacing = False
                if replacingstr in inputs.keys():
                    out += inputs[replacingstr]
                else:
                    inputs[replacingstr] = ""
                    print(f"{replacingstr} の置換文字列を入力してください（終了するにはEnterを2回押してください）:", end="")
                    while True:
                        line = input()
                        if line == "":
                            break
                        inputs[replacingstr] += line + "\n"
                inputs[replacingstr] = inputs[replacingstr].rstrip("\n")
                out += inputs[replacingstr]
                replacingstr = ""
            case _:
                if replacing:
                    replacingstr += i
                else:
                    out += i
print(out)
