#!/usr/bin/python3
import sys
import requests
domain="test.com"
f=open("wordlist2.txt","r").read()



subdomains=f.splitlines()

for i in subdomains:
	url=f'http://{i}.{domain}'
	r=requests.get(url)
	if r.status_code!=404:
		print(f"subdomain {i} found")


