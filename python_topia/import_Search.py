# モジュールの検索先 参照

import sys

for place in sys.path:
    print(place)

# pip show モジュール名 でモジュール単体のimport先 参照