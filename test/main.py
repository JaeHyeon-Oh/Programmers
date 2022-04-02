import re
#
# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    new_id = "abbcdefghijklmn.p"
    # res = re.sub('[^a-z0-9._-]', '', new_id)
    for i in range(int(len(new_id)/2),0,-1):
        for j in range(0,len(new_id),i):
            print(new_id[j:j+i])

#
#     new_id="abcdefghijklmn.p"
#     answer = ''
#     lo = new_id.lower()
#     res = re.sub('[^-0-9a-z._]', '', lo)
#     a = res[0]
#     for i in range(0, len(res)):
#         if a[-1] != res[i]:
#             a += res[i]
#     print(a)
#     if a[0] == '.':
#         a = a[1:]
#     elif a[-1] == '.':
#         a = a[0:-1]
#     if len(a) == 0:
#         a += 'a'
#     if len(a) >= 16:
#         a = a[:15]
#     if a[-1] == '.':
#         a = a[0:-1]
#     for i in range(0, 3):
#         if len(a) <= 2:
#             a += a[-1]
#     print(a)