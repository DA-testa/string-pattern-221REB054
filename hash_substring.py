# python3
#Marija Tulovska 13.gr 221REB054


def read_input():
    test = input()

    if "I" in test:
        pattern = input()
        text = input()  

    if "F" in test:
        fails = open("./tests/06", "r")
        f = fails.read()
        f = f.split('\n')
        pattern = f[0]
        text = f[1]

    pattern = pattern.strip()
    text = text.strip()


    return (pattern, text)

def print_occurrences(output): 
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 


    n_pattern = len(pattern)
    n_text = len(text)
    pattern_hash = hash(pattern)
    text_hash = hash(text[:n_pattern])
    occurrences = []

    for i in range(n_text - n_pattern + 1): 

        if pattern_hash == text_hash and pattern == text[i:i+n_pattern]:
            occurrences.append(i)

        if i < n_text - n_pattern:  
            text_hash = hash(text[i + 1 : i + n_pattern + 1])
    
    return occurrences




if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

