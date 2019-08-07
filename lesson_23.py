def chek(F,idealF):
  for i in range(len(F)):
    if F[i] != idealF[i]:
      return False
  return True

def oneChek(F,idealF):
  cheking = False
  for i in range(len(F)):
    for j in range(i+1,len(F)):
      ch = F
      ch[i],ch[j] = ch[j],ch[i]
      cheking = chek(F,idealF)
      if cheking  == True:
        return cheking
      else:
        ch[i],ch[j] = ch[j],ch[i]
  return cheking

def twoChek(F,idealF):
  cheking = False
  startIndex = 0
  stopIndex = 0
  ch = []
  for i in range(len(F)-1):
    if F[i] < F[i-1] and F[i+1] > F[i]:
      startIndex = F[i]
    elif F[i] < F[i-1] and F[i] < F[i+1]:
      stopIndex = F[i]
    elif startIndex != 0:
      stopIndex = len(F)
  for i in range(len(F)):
    if i < startIndex or i > stopIndex-1:
      ch.append(F[i])
    else:
      F.reverse()
      ch.append(F[i-1])
      F.reverse()
  cheking = chek(ch,idealF)
  return cheking

def Football( F, N):
  idealF = []
  cheking = False
  ch = []
  for i in range(N):
    idealF.append(F[i])
  for i in range(len(idealF)-1):
    for j in range(len(idealF)-i-1):
        if idealF[j] > idealF[j+1]:
            idealF[j], idealF[j+1] = idealF[j+1], idealF[j]
  cheking = oneChek(F,idealF)
  if cheking == False:
    cheking = twoChek(F,idealF)
  return cheking  