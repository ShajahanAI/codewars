# https://www.codewars.com/kata/5b3e1dca3da310a4390000f3/train/python

# Passed

def work_needed(project_minutes, free_lancers):
    calculate_freelancer_time = lambda freelancer: freelancer[0] * 60  + freelancer[1]
    available_freelancers_time = sum([calculate_freelancer_time(freelancer_time) for freelancer_time in free_lancers])
    time_i_need_to_work =  project_minutes - available_freelancers_time
    if time_i_need_to_work > 0:
        hours_i_need_to_work = time_i_need_to_work // 60
        minutes_i_need_to_work = time_i_need_to_work % 60
        return f"I need to work {hours_i_need_to_work} hour(s) and {minutes_i_need_to_work} minute(s)"
    
    return "Easy Money!"

output = work_needed(141, [(1,55), (0,25)])
print(output)