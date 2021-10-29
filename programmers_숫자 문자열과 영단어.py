def solution(s):
    answer = 0
    num_eng = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
               'five':'5' ,'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}    
    try:
        answer = int(s)
    except:
        for idx, val in enumerate(list(num_eng.keys())):
            if val in s:
                s = s.replace(val, list(num_eng.values())[idx])
        answer = int(s)
    return answer
