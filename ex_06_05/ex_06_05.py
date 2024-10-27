text = "X-DSPAM-Confidence:    0.8475"
x = text.find(':')
nstr = text[x+1:].strip()
n = float(nstr)
print(n)
