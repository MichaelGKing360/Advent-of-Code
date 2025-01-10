def main():
  with open("password-philosophy.txt","r") as file:
    rows = file.readlines()

  i = 0
  good_passwords = 0
  for row in rows:
    values = row.split()
    max_and_min = [int(string_int) for string_int in values[0].split('-')]
    min = max_and_min[0]
    max = max_and_min[1]
    # print(f'min: {min}')
    # print(f'max: {max}')

    letter = values[1].replace(":","")
    # print(f'letter: {letter}')

    password = values[2]
    # print(f'password: {password}')
    # count_occurences
    count = password.count(letter)
    # print(f'count of letters: {count}')

    if(min <= count and max >= count):
      good_passwords += 1

    i += 1

  print(f'total good passwords: {good_passwords}')


if __name__ == "__main__":
  main()


