def string_bits(str):
  end = ""
  for i in range(len(str)):
    if i % 2 == 0:
      end = end + str[i]
  return end
