import re

# {1,3}
# match_content = re.match("^\D{1,3}afcgx\D$", "fdfafcgxd")
# if match_content:
#     print(match_content.group())
# else:
#     print("匹配失败")

match_content = re.match("^\Safcgx\D$", "hafcgxd")
# if match_content:
#     print(match_content.group())
# else:
#     print("匹配失败")

match_content = re.match(".*(gx).*", "dsadafwfewgxasjjdja")
# if match_content:
#     print(match_content.group())
# else:
#     print("匹配失败")

match_content = re.match("[a-zA-Z1-9][a-zA-Z0-9]{3,19}@(qq|168|126)\.com", "world@168.com")
if match_content:
    print(match_content.group())
else:
    print("匹配失败")
