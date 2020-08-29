import hashlib
import argparse

parser = argparse.ArgumentParser(description="hash_cracker")
parser.add_argument('-md5', '--md5', dest='md_5')
parser.add_argument('-w', '--wordlist', dest='word_list',required=True)
parser_args = parser.parse_args()

def main():
    hash_crack = ''
    with open(parser_args.word_list) as file:
        for words in file:
            str1 = words.strip()
            hash_value = hashlib.md5(bytes(str1, encoding='utf-8')).hexdigest()
            if hash_value == parser_args.md_5:
                hash_crack = words
                print('The value of {} is : {}'.format(parser_args.md_5, words))
        if hash_crack=='':
            print('No match found for these hash, Try another dictionary')

if __name__ == '__main__':
    main()