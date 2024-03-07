def solution(arr, target):
  hashtable = [0] * (target + 1)

  for num in arr:
    if num <= target:
      hashtable[num] = 1

  for num in arr:
    complement = target - num

    if complement != num and 0 <= complement <= target and hashtable[complement] == 1:
      return True

  return False

answer = solution([1,2,3,4,8] , 6)
print(answer)
