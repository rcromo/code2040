import requests;

api_token = "98167604da0984648f3b69b863562265"
grab = "http://challenge.code2040.org/api/haystack"
post_to = "http://challenge.code2040.org/api/haystack/validate"
 

r_1 = requests.post(grab, data = {'token': api_token})
dictionary  = r_1.json()

needle = dictionary['needle']
haystack = dictionary['haystack']

def find_needle():
	i = 0
	while i < len(haystack):
		if haystack[i] == needle:
			needle_index = i
		i = i + 1
	return needle_index ;

index = find_needle() 



r_2 = requests.post(post_to, data = {'token': api_token, 'needle' : index})
print(r_2.text)


