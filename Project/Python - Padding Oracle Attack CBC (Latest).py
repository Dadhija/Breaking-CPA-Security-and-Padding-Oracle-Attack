import requests
import json
import codecs
import sys
from binascii import hexlify

json_data = '{"ciphertext": "d6c88784f890d6a24c5bf2f090c0aec7151c970066589f860ef42acb137f0420638cbb004c563a6617c7b2fb09f17fc7","iv": "26d1634eca6a0222fcff1f6d7bc87ddd"}'
python_obj = json.loads(json_data)
b = json.dumps(python_obj)

string_ct = python_obj["ciphertext"]

#hex_string="d6c88784f890d6a24c5bf2f090c0aec7151c970066589f850df329ca127e031f638cbb004c563a6617c7b2fb09f17fc7"

#an_integer = int(hex_string, 16)
#print(an_integer)
#remove # for testing
#r = requests.post(
# 'https://ineedrandom.com/paddingoracle',
#json={
# "ciphertext":
#string_ct,
#"iv": "26d1634eca6a0222fcff1f6d7bc87ddd"
#})

#print(r.text)
#print("\n")

json_data = '{"ciphertext": "d6c88784f890d6a24c5bf2f090c0aec7151c970066589f860ef42acb137f0420638cbb004c563a6617c7b2fb09f17fc7","iv": "26d1634eca6a0222fcff1f6d7bc87ddd"}'
python_obj2 = json.loads(json_data)
print("\n")

XORchar = ''

mod_str_list = str(python_obj2["ciphertext"])
#print(mod_str_list)
print("\n")
list_ct = list(string_ct)

my_list = [
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e',
  'f'
]

Valid_Padding='Valid'
Invalid_Padding='Invalid'
i = 45 #change starting index accordingly
while (i >= 0):
  
  for j in my_list:
    for p in my_list:
      list_ct[i] = j
      list_ct[i-1]=p
      print(j, end ="")#sending these hex
      print(p, end ="")#values as modified Ciphertext
      temp_ct = "".join(list_ct)
      r = requests.post('https://ineedrandom.com/paddingoracle',
                      json={
                        "ciphertext": temp_ct,
                        "iv": "26d1634eca6a0222fcff1f6d7bc87ddd"
                      })
      #print(temp_ct)
      #above statement prints c1||c2||c3 remove# to activate
      print("\n")
      print(r.text)
    #print("\n")
      if str(r.text) == "\"Valid\"":
        XORchar += j
        print(j)
        sys.exit("Values don't match unfortunately")
        exit()
        
  i = i - 1
  
#listToStr = ' '.join([str(elem) for elem in list_ct])
#print("\n")

#print(listToStr)
#print(python_obj["ciphertext"])
