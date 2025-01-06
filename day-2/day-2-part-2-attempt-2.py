import json


def main():
  with open("input.txt", "r") as file:
    rows = file.readlines()

  print(len(rows))
  # Part 2
  valid_row_count = 0
  i = 0
  for row in rows:
    # if i < 100:
    print()
    print()
    print(f'Starting new row: {row}')
    # get each row as ints
    value_row = [int(string_int) for string_int in row.split()]
    validation_value_row = value_row.copy()
    # check row validity
    is_row_valid = get_row_validity(value_row, validation_value_row, 1, 0)

    if(is_row_valid):
      print("Row is valid. Adding to count.")
      valid_row_count += 1
    else:
      print("Row is invalid. Not added to count.")
  i += 1

  print(valid_row_count)


def check_distances(distances, value_row, validation_value_row, attempt_num, error_count):
  original_value_row = value_row.copy()
  try:
    positive_positions = []
    negative_positions = []
    zero_positions = []
    i = 0
    for distance in distances:
      # Check if distance is out of allowable range
      if (distance > 3) or (distance < -3):
        error_count += 1
        print(f'distance[i] was out of allowable range: {distance}. Adding error!')
        if(error_count > 1 and attempt_num == 1):
          print("attempt 1 error count is greater than 1")
          attempt_num = 2
          error_count = 0
          negative_positions = []
          positive_positions = []
          return get_row_validity(validation_value_row, validation_value_row, attempt_num, error_count)

        if(error_count > 1 and attempt_num == 2):
          print("More than 1 error: Returning false!")
          return False

        # check if positive distance
        if(distance > 0 and attempt_num == 1):
          print("hit positive attempt 1")
          # remove bad value
          value_row.pop(i)
          # recheck validity
          negative_positions = []
          positive_positions = []
          return get_row_validity(value_row, validation_value_row, attempt_num, error_count)

        # check if negative distance or 0
        if(distance < 0 and attempt_num == 1):
          print("hit negative attempt 1")
          # remove bad value
          value_row.pop(i + 1)
          # recheck validity
          negative_positions = []
          positive_positions = []
          return get_row_validity(value_row, validation_value_row, attempt_num, error_count)

                # check if positive distance
        if(distance > 0 and attempt_num == 2):
          print("hit positive attempt 2")
          # remove bad value
          value_row.pop(i + 1)
          # recheck validity
          negative_positions = []
          positive_positions = []
          return get_row_validity(value_row, validation_value_row, attempt_num, error_count)

        # check if negative distance or 0
        if(distance < 0 and attempt_num == 2):
          print("hit negative attempt 2")
          # remove bad value
          value_row.pop(i)
          # recheck validity
          negative_positions = []
          positive_positions = []
          return get_row_validity(value_row, validation_value_row, attempt_num, error_count)

      if(distance == 0 and attempt_num == 1):
        print('distance was equal to zero. Attempt 1:  Adding error!')
        error_count += 1
        if(error_count > 1):
          attempt_num = 2
          error_count = 0
          print('errors are greater than one: beginning attempt 2')
          negative_positions = []
          positive_positions = []
          return get_row_validity(validation_value_row, validation_value_row, attempt_num, error_count)

        value_row.pop(i)

      if(distance == 0 and attempt_num == 2):
        print('distance was equal to zero. Adding error!')
        error_count += 1
        if(error_count > 1):
          print("More than 1 error 2nd attempt: Returning false!")
          return False

        value_row.pop(i)

      # collect position of positive and negative values
      if(distance > 0):
        # handle positive case
        positive_positions.append(i)

      if(distance < 0):
        # handle negative case
        negative_positions.append(i)

      # if (+)'s >= 2 and (-)'s >= 2 return false, list is invalid
      if(len(positive_positions) >= 2 and len(negative_positions) >= 2):
        print(f'2 positive and 2 negative distances: Returning false!')
        return False

      # when this occurs then pop then negative element and reprocess
      if(len(positive_positions) >= 2 and len(negative_positions) < 2  and len(negative_positions) > 0 and attempt_num == 1):
        print("entering +2 positives and less than 2 negatives: attempt 1")
        error_count += 1
        if(error_count > 1):
          print("more than one error: beginning attempt 2")
          error_count = 0
          attempt_num = 2
          negative_positions = []
          positive_positions = []
          return get_row_validity(validation_value_row, validation_value_row, 2, error_count)

        # need to pop the negative element and reprocess
        print(f'negative_position: {negative_positions[0]}')
        print(f'value row[i]: {value_row[negative_positions[0]]}')
        print(f'popping negative element: {distance}')
        value_row.pop(negative_positions[0])
        negative_positions = []
        positive_positions = []
        return get_row_validity(value_row, validation_value_row, 1, error_count)

      # when this occurs then pop then positive element and reprocess
      if(len(negative_positions) >= 2 and len(positive_positions) < 2 and len(positive_positions) > 0 and attempt_num == 1):
        error_count += 1
        if(error_count > 1):
          error_count = 0
          attempt_num = 2
          negative_positions = []
          positive_positions = []
          return get_row_validity(validation_value_row, validation_value_row, 2, error_count)

        # need to pop the positive element and reprocess
        value_row.pop(positive_positions[0] + 1)
        negative_positions = []
        positive_positions = []
        return get_row_validity(value_row, validation_value_row, 1, error_count)

            # when this occurs then pop then negative element and reprocess
      if(len(positive_positions) >= 2 and len(negative_positions) < 2  and len(negative_positions) > 0 and attempt_num == 2):
        print("entering +2 positives and less than 2 negatives: attempt 2")
        print(f"errors: {error_count}")
        error_count += 1
        if(error_count > 1):
          print("More than 1 error: Returning false!")
          return False
        # need to pop the negative element and reprocess
        print(f'negative_position: {negative_positions[0]}')
        print(f'value row[i]: {value_row[negative_positions[0] + 1]}')
        print(f'popping negative element: {distance}')
        value_row.pop(negative_positions[0] + 1)
        negative_positions = []
        positive_positions = []
        return get_row_validity(value_row, validation_value_row, 2, error_count)

      # when this occurs then pop then positive element and reprocess
      if(len(negative_positions) >= 2 and len(positive_positions) < 2 and len(positive_positions) > 0 and attempt_num == 2):
        error_count += 1
        if(error_count > 1):
          print("More than 1 error: Returning false!")
          return False
        # need to pop the positive element and reprocess
        value_row.pop(positive_positions[0])
        negative_positions = []
        positive_positions = []
        return get_row_validity(value_row, validation_value_row, 2, error_count)

      i += 1
      print(f"iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii = {i}")

    # More than two errors means list is invalid
    if (error_count < 2):
      print(f'error count was less than 2: {error_count} - returning true')
      return True
    else:
      print(f'error count was more than 2: {error_count} - returning false')
      return False

  except ValueError as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
    print(value_row)


def get_row_validity(value_row, validation_value_row, attempt_num, error_count):
  print(f'value_row: {value_row}')
  print(f'error_count: {error_count}')

  distances = []
  i = 0
  for num in value_row:
    # if logic was added to stop distance check from going out of bounds
    if(i + 1 != len(value_row)):
      # add all distances to an arry
      distances.append(value_row[i+1] - num)
    i += 1

  print(f'distances: {distances}')

  return check_distances(distances, value_row, validation_value_row, attempt_num, error_count)



if __name__ == "__main__":
  main()

