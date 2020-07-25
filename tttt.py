# 测试备用
# 翻译实现
import json
dictPutall = json.load(open('json/dictAllPut.json','r'))
dictpcap = dictPutall['pcap1']
print(dictpcap)
print(type(dictpcap))
i = 0
stringo = ''
stringt = ''
stringolist = []
stringtlist = []


while i < len(dictpcap):
    stringo += str(dictpcap[i])
    for key in dictpcap[i]:

        print(test)
    i += 1

# print(stringolist)
# string = "".join(stringolist)

# for key in dictpcap:
#     string_list.append(key)
#     print(dictpcap[key]['info'])
#     strinfo = '\nInfomation: '+ str(dictpcap[key]['info'][0]) + '\n'
#     string_list.append(strinfo)
#     print(type(dictpcap[key]['trans']))
#     # print(strinfo)
#     if dictpcap[key]['trans'] == '"on":true':
#         strtrans = 'Translation: '+' Turn on the light'+ '\n'
#         string_list.append(strtrans)
#     elif dictpcap[key]['trans'] == '"on":false':
#         strtrans = 'Translation: ' + ' Turn off the light' + '\n'
#         string_list.append(strtrans)
#     elif dictpcap[key]['trans'][0:6] == '"bri":':
#         strtrans = 'Translation: ' + ' Turn the bright to '+dictpcap[key]['trans'][6:9] + '\n'
#         string_list.append(strtrans)
#     string_list.append('\n')
# string = "".join(string_list)
# print(string)