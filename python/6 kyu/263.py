# https://www.codewars.com/kata/695688e9858d531c29a9d748/train/python

# Passed

from collections import defaultdict

def detect_brute_force(logs):
    brute_force_ips = []
    ip_to_failure_count_dict = defaultdict(int)
    for log in logs:
        ip, status, user = log.split(' ')
        if status == "LOGIN_FAIL":
            ip_to_failure_count_dict[ip] += 1
        else:
            ip_to_failure_count_dict[ip] = 0
        
        if ip_to_failure_count_dict[ip] >= 3 and ip not in brute_force_ips:
            brute_force_ips.append(ip)
            
    brute_force_ips.sort()
    return brute_force_ips

output = detect_brute_force([
            "1.1.1.1 LOGIN_FAIL user=a",
            "2.2.2.2 LOGIN_FAIL user=b",
            "1.1.1.1 LOGIN_FAIL user=a",
            "2.2.2.2 LOGIN_SUCCESS user=b",
            "1.1.1.1 LOGIN_FAIL user=a",
            "2.2.2.2 LOGIN_FAIL user=b"
        ])
print(output)