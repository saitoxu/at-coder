#!/usr/bin/env python

import argparse
import subprocess
import glob


def main():
    parser = argparse.ArgumentParser(description='問題の実行')
    parser.add_argument('file_path', help='実行するPythonファイル名')

    args = parser.parse_args()
    problem_file_path = args.file_path
    problem_name = problem_file_path.replace('problems/', '').replace('.py', '')

    input_file_paths = sorted(glob.glob('test_cases/{problem_name}_in*.txt'.format(problem_name=problem_name)))
    wrong_cases = []

    if len(input_file_paths) == 0:
        parser.print_help()
        exit(0)

    for input_file_path in input_file_paths:
        command = 'cat {input_file_path} | python {problem_file_path}'.format(
            input_file_path=input_file_path, problem_file_path=problem_file_path)

        result = subprocess.check_output(command, shell=True)
        result_lines = result.decode('utf-8').strip().split("\n")

        output_file_path = input_file_path.replace('_in', '_out')

        answer = subprocess.check_output(
            'cat {output_file_path}'.format(output_file_path=output_file_path), shell=True)
        answer_lines = answer.decode('utf-8').strip().split("\n")

        is_correct = check(input_file_path, output_file_path, result_lines, answer_lines)
        if is_correct:
            print_color('.', pycolor.GREEN, newline=False)
        else:
            wrong_cases.append({
                'input_file_path': input_file_path,
                'results': result_lines,
                'answers': answer_lines
            })
            print_color('F', pycolor.RED, newline=False)

    print('')
    print('')
    if len(wrong_cases) == 0:
        print_color('All test cases are passed.', pycolor.GREEN)
    else:
        print_color('Failures:', pycolor.RED)
        for wc in wrong_cases:
            print_wrong_answer(wc['input_file_path'], wc['results'], wc['answers'])


def check(input_file_path, output_file_path, results, answers):
    """
    正解か判定
    """
    if len(results) != len(answers):
        return False

    for i in range(len(results)):
        if results[i] != answers[i]:
            return False

    return True


def print_wrong_answer(input_file_path, results, answers):
    """
    失敗したテストケースの表示
    """
    print('')
    print_color('  Test case: ' + input_file_path, pycolor.RED)
    print_color('    expected:', pycolor.RED)
    for answer in answers:
        print_color('      ' + answer, pycolor.RED)
    print_color('    got:', pycolor.RED)
    for result in results:
        print_color('      ' + result, pycolor.RED)


def print_color(msg, color, newline = True):
    """
    色付きのprint
    """
    end = '\n' if newline else ''
    print(color + msg + pycolor.END, end=end)


# ref. https://qiita.com/ironguy/items/8fb3ddadb3c4c986496d
class pycolor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'

main()
