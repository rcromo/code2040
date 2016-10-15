import requests;

api_token = "98167604da0984648f3b69b863562265"
endpoint = "http://challenge.code2040.org/api/reverse"
post_to = "http://challenge.code2040.org/api/reverse/validate"

## Essentially 'string'[::-1]
## Reverse a string
def reverse(string):
	start = end = None
	step = -1
	slice_rev = slice(start, end, step)
	return string[slice_rev]

r_1 = requests.post(endpoint, data = {'token': api_token})
reverse_api = reverse(r_1.text)
r_2 = requests.post(post_to, data = {'token': api_token, 'string': reverse_api})
print(r_2.text)



