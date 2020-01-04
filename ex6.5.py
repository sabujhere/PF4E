text = "X-DSPAM-Confidence:    0.8475"
colonPosition = text.find(':')
print(float(text[colonPosition + 1:].strip()))
