def solve(sequence1, sequence2):
    # ----------------------------- #    
    cache = {}
    sequence1_length,sequence2_length = len(sequence1),len(sequence2)
    lcs_length_sequence1_sequence2 = longest_common_subsequence(sequence1,sequence2,sequence1_length,sequence2_length,cache)
    lcs_length_sequence12_sequence22 = 0
    length_sequence12_sequence22 = 0
    for i in range(len(sequence1)):
        for j in range(len(sequence2)):
            sequence12 = sequence1[(sequence1_length-i-1):]
            sequence22 = sequence2[(sequence2_length-j-1):]
            if len(sequence12)+len(sequence22) >= lcs_length_sequence1_sequence2:
                cached = {}
                sequence12_length,sequence22_length = len(sequence12),len(sequence22)
                lcs_length_sequence12_sequence22 = longest_common_subsequence(sequence12,sequence22,sequence12_length,sequence22_length,cached)
                if(lcs_length_sequence12_sequence22 == lcs_length_sequence1_sequence2) and ((length_sequence12_sequence22 > sequence12_length + sequence22_length) or length_sequence12_sequence22 == 0):
                    length_sequence12_sequence22 = sequence12_length + sequence22_length
                    break
    # ----------------------------- #       
    return {
        'LCS': lcs_length_sequence1_sequence2, # you should set this field to the LCS length of given sequences.
        'length': length_sequence12_sequence22 # you should set this field to the total length of sequence12 and sequence22.
    }


def longest_common_subsequence(s1, s2, sequence1_length, sequence2_length, cache):
    if sequence1_length == 0 or sequence2_length == 0:
        return 0
    if (sequence1_length, sequence2_length) in cache:
        return cache[(sequence1_length, sequence2_length)]
    if s1[sequence1_length - 1] == s2[sequence2_length - 1]:
        cache[(sequence1_length, sequence2_length)] = 1 + longest_common_subsequence(s1, s2, sequence1_length - 1, sequence2_length - 1, cache)
    else:
        cache[(sequence1_length, sequence2_length)] = max(
            longest_common_subsequence(s1, s2, sequence1_length, sequence2_length - 1, cache), 
            longest_common_subsequence(s1, s2, sequence1_length - 1, sequence2_length, cache)
        )
    return cache[(sequence1_length, sequence2_length)]

def read_input():
    sequence1 = input()
    sequence2 = input()
    return sequence1, sequence2


if __name__ == "__main__":
    sequence1, sequence2 = read_input()
    res = solve(sequence1, sequence2)
    print(res['LCS'])
    print(res['length'])
