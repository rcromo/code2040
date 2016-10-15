import requests;


r = requests.post("http://challenge.code2040.org/api/register", data = {'token': "98167604da0984648f3b69b863562265", 'git' : "https://github.com/rcromo/code2040"})

print(r.text)