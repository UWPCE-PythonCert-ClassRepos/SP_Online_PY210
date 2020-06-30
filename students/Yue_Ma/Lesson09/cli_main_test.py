#.!/usr/bin/env python3
import cli_main
import os
import pytest


def test_send_letters_to_all_donors():
    cli_main.send_letters_to_all_donors()
    assert os.path.isfile('Yue_Ma.txt')
    assert os.path.isfile('Yanan_Ma.txt')
    assert os.path.isfile('Jianqiang_Ma.txt')
    assert os.path.isfile('Chunhong_Liu.txt')
    assert os.path.isfile('Robert_Rowe.txt')


def test_creat_a_report():
    report = cli_main.create_a_report()
    assert report[0] == ' --------------------------------------------------------------------- '
    assert report[1] == '| Donor Name          | Total Given     | Num Gifts  | Average Gift   |'
    assert report[2] == '|---------------------------------------------------------------------|'
    assert report[3] == '| Robert Rowe         | 20000000.00     | 1          | 20000000.00    |'
    assert report[4] == '| Yue Ma              | 1661132.00      | 2          | 830566.00      |'
    assert report[5] == '| Jianqiang Ma        | 1056023.00      | 3          | 352007.67      |'
    assert report[6] == '| Yanan Ma            | 12833.00        | 4          | 3208.25        |'
    assert report[7] == '| Chunhong Liu        | 1100.61         | 2          | 550.31         |'
    assert report[8] == ' --------------------------------------------------------------------- '


def test_send_all():
    send_all = cli_main.send_letters_to_all_donors()
    assert os.path.isfile('Yue_Ma.txt')
    assert os.path.isfile('Robert_Rowe.txt')
    assert os.path.isfile('Jianqiang_Ma.txt')
    assert os.path.isfile('Yanan_Ma.txt')
    assert os.path.isfile('Chunhong_Liu.txt')
