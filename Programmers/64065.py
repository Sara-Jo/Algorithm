# ------------------1--------------------
# def solution(s):
#     num_list = []
    
#     for c in s:
#         if c == '{':
#             temp_list = []
#             temp_num = ""
#         elif c == ',':
#             if len(temp_num):
#                 temp_list.append(int(temp_num))
#                 temp_num = ""
#         elif c == '}':
#             if len(temp_num):
#                 temp_list.append(int(temp_num))
#                 temp_num = ""
#             if len(temp_list):
#                 num_list.append(temp_list)
#                 temp_list = []
#         else:
#             temp_num += c      
            
#     num_list = sorted(num_list, key=lambda x: len(x))
    
#     answer = []
#     for l in num_list:
#         for n in l:
#             if n not in answer:
#                 answer.append(n)
        
#     return answer


#------------------2--------------------
def solution(s):
    s = s.lstrip('{').rstrip('}').split('},{')
    
    nums = []
    for n in s:
        nums.append(list(map(int, n.split(','))))
    
    nums.sort(key=len)
    
    answer = []
    for num in nums:
        for n in num:
            if n not in answer:
                answer.append(n)
                
    return answer