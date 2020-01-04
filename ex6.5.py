text = "X-DSPAM-Confidence:    0.8475";
zeroPosition = text.find('0')
print(float(text[zeroPosition:len(text)]))
