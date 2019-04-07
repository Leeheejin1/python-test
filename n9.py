val = input('문장을 입력하세요:')
print(val[0:val.find('h')]+val[val.rfind('h')+1::])


