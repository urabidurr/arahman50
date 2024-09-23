def string_splosion(str):
  end = ''
  for i in range(len(str)):
    end = end + str[:i+1]
    i += 1
  return end
