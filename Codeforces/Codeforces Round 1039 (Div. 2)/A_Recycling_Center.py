for _ in range(int(input())):
  n, c = map(int, input().split())
  a = list(map(int, input().split()))
  a.sort(reverse=True)
  
  num_doublings, coins = 1, 0
  
  for i in range(n):
      if a[i] * num_doublings > c:
        coins += 1
      else:
        num_doublings *= 2
 
  print(coins)