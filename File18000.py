def chi_square(counts):
    expected = sum(counts)/len(counts)
    chi = 0
    for n in counts:
        chi += ((n-expected)**2)/expected
    return chi

def get_char_counts(text):
    counts = [0] * 127
    for c in text:
        n = ord(c)
        counts[n] += 1
        
    return counts[32:]

def get_file_name(num):
    num_str = hex(num)
    num_str = num_str[2:]
    
    if len(num_str) == 1:
        num_str = "000" + num_str
    elif len(num_str) == 2:
        num_str = "00" + num_str
    elif len(num_str) == 3:
        num_str = "0" + num_str
        
        
    return "file_" + num_str + ".txt"
    

def get_file_content(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    return content

num_files = 18000
threshold = 140

for n in range(num_files):
    file_name = get_file_name(n)
    text = get_file_content("text_files/" + file_name)
    counts = get_char_counts(text)
    x_sq = chi_square(counts)

    if x_sq > threshold:
        print(file_name, x_sq)
