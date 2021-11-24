import os
import sys
import argparse
from math import log2

def get_list(path: str) -> str:
    return [file for file in os.listdir(path) if os.path.isfile(file)]

def get_contents(path: str) -> list:
    data = []
    with open(path, "rb") as file:
        for i in file.read():
             data.append(i)
    return data

def entropy(data: list) -> float:       
    entropy = 0
    data_length = len(data)
    for i in range(256):
        n = data.count(i) / data_length
        if n > 0:
            entropy += -n * log2(n)
    return entropy

def converting(entropy: float) -> int:
    return round(entropy / 8 * 100)

def get_dictionary(path: str) -> dict:
    dictionary = {}
    for i in get_list(args.dir):
        if os.path.getsize(i) != 0:
            dictionary[i] = converting(entropy(get_contents(os.path.join(path, i))))
    return dictionary

def descending_sort(dictionary: dict) -> dict:
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

def ascending_sort(dictionary: dict) -> dict:
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=False))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Utility that will detect encrypted/compressed files in a specified directory.')
    parser.add_argument("-d", "--dir", type=str, default = os.path.dirname(os.path.abspath(sys.argv[0])),  
        help="• specifies the path to directory where to look for encrypted/compressed files. Default - current directory.")
    parser.add_argument("-c", "--confidence", type=int, default=80,
        help="• specifies the threshold level of confidence (in percents from 0 to 100) to treat a certain file as encrypted/compressed. Default - 80%%.")
    parser.add_argument("-s", "--sorted_descending", action='store_true',
        help="• all files in the program output should be sorted by confidence level descending (from high to low).")
    parser.add_argument("-a", "--sorted_ascending", action='store_true',
        help="• all files in the program output should be sorted by confidence level ascending (from low to high).")
    parser.add_argument("-p", "--print_confidence", action='store_true',
        help="• print the confidence level along with the file name.")
    args = parser.parse_args()
    
    check = False
    if args.print_confidence:
        if args.sorted_descending:
            for (contents, percents) in descending_sort(get_dictionary(args.dir)).items():
                if percents > args.confidence:
                    print(f'{percents}% {contents}')
                    check = True
        elif args.sorted_ascending:
            for (contents, percents) in ascending_sort(get_dictionary(args.dir)).items():
                if percents > args.confidence:
                    print(f'{percents}% {contents}')
                    check = True
        else:
            for (contents, percents) in get_dictionary(args.dir).items():
                if percents > args.confidence:
                    print(f'{percents}% {contents}')
                    check = True 
    else:
        if args.sorted_descending:
            for (contents, percents) in descending_sort(get_dictionary(args.dir)).items():
                if percents > args.confidence:
                    print(contents)
                    check = True
        elif args.sorted_ascending:
            for (contents, percents) in ascending_sort(get_dictionary(args.dir)).items():
                if percents > args.confidence:
                    print(contents)
                    check = True
        else:
            for (contents, percents) in get_dictionary(args.dir).items():
                if percents > args.confidence:
                    print(contents)
                    check = True
    if not check:
        print("directory is empty or incorrectly passed argument")
