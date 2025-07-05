def repeat(string, exclaim):
    """
    Returns the string 3 times and adds exclamation 
    marks if exclaim is true
    """

    result = string + ' ' + string + ' ' + string

    if exclaim:
        result += '!!!'
    
    return result

def main():
    print(repeat('hey there', False))
    print(repeat('hooya', True))

if __name__=='__main__':
    main()