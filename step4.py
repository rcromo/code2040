import requests;

api_token = "98167604da0984648f3b69b863562265"
grab = "http://challenge.code2040.org/api/prefix"
post_to = "http://challenge.code2040.org/api/prefix/validate"


r_1 = requests.post(grab, data = {'token': api_token})
dictionary = r_1.json()

prefix = dictionary['prefix']
array_of_words = dictionary['array']


not_prefix = []

def not_that_prefix():
	i = 0
	while i < len(array_of_words):
		if array_of_words[i].startswith(prefix) != True:
			not_prefix.append(array_of_words[i])
		i = i + 1
	return not_prefix ;

updated_array = not_that_prefix();

payload = {}
payload['token'] = api_token
payload['array'] = updated_array

 
r_2 = requests.post(post_to, json = payload)
print(r_2.text)
 