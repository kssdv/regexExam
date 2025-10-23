import re

text = "070-1234-5678"

pattern = r"\d{3}-\d{3,4}-\d{3,4}"

match_object = re.search(pattern, text)

if match_object:
    start_index = match_object.start()
    print(f"パターンを探しました。スタートindex：{start_index}")
    print(f"探した文字列：{match_object.group()}")
else:
    print("文字列からパターンが見つかりませんでした")