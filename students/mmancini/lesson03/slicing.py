#!/usr/bin/env python3


####################################


def slice_lab(in_lst):
    result_lst = in_lst.copy()
    print(f"slice lab, original list ", result_lst)

    endix = len(in_lst) - 1
    # print(f"endix =  ", str(endix))

    lsta = in_lst.copy()
    lsta = lsta[-1:] + lsta[1:-1] + lsta[:1]
    print(f"slice lab, swap first and last, ==> ", lsta)

    return result_lst




def slice_test(in_lst):

    # ***MMM slice syntax notes [begix:endix:step]

    result_lst = in_lst.copy()
    print(f"slice_test, original list ", result_lst)

    lsta = in_lst.copy()
    lsta = lsta[-1:]
    print(f"aaa ", lsta)
    lstb = in_lst.copy()
    lstb = lstb[0:-2]
    print(f"bbb ", lstb)
    lstc = in_lst.copy()
    lstc = lstc[:1]
    print(f"ccc ", lstc)
    # return (seq[-1:]+seq[1:-1]+seq[:1])

    print("")

    return result_lst

###################################


# main, test funcs

if __name__ == "__main__":
    # run some tests
    data_lst = ["abc", "def", "hij", "klm", "nop", "qrs"]

    # slice_test(data_lst)

    result_lst1 = slice_lab(data_lst)


