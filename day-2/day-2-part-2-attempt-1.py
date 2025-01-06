import json


def main():
  with open("input.txt", "r") as file:
    rows = file.readlines()

  print(len(rows))
  # Part 2
  valid_row_count = 0
  for row in rows:
    # get each row as ints
    value_row = [int(string_int) for string_int in row.split()]
    # # sort rows
    # row_asc = sorted(value_row)
    # row_desc = sorted(value_row, reverse=True)

    is_row_valid = get_distance_validity(value_row, 0)

    if(is_row_valid):
      print("Row is valid. Adding to count.")
      valid_row_count += 1
    else:
      print("Row is invalid. Not added to count.")



      #   # Need to eliminate distinct values, to get rid of 0 distance values
      #   checkDistinct(distance_data["value_row"], distance_data["error_count"])

      # range success: no error
      # if(range_data["is_in_range"] == True and range_data["error_count"] < 2):
      #   asc_data = check_asc(range_data)
      #   # asc success: 0-1 errors
      #   if(asc_data["is_asc"] == True and asc_data["error_count"] < 2):
      #     final_list.append(asc_data["value_row"])
      #   else:
      #     desc_data = check_desc(range_data)
      #     # desc success: 0-1 errors
      #     if (desc_data["is_desc"] == True and desc_data["error_count"] < 2):
      #       final_list.append(desc_data["value_row"])

      # # range success: 1 error
      # if(range_data["is_in_range"] == True and range_data["error_count"] == 1):
      #   asc_data = check_asc_has_error(range_data)
      #   # asc success: 1 range error
      #   if (asc_data["is_asc"] == True and asc_data["error_count"] < 2):
      #     final_list.append(asc_data["value_row"])
      #   else:
      #     desc_data = check_desc_has_error(range_data)
      #     # desc success: 1 range error
      #     if (desc_data["is_desc"] == True and desc_data["error_count"] < 2):
      #       final_list.append(asc_data["value_row"])

  print(valid_row_count)




# def check_asc(range_data):
#   is_asc = True
#   asc_value_row = range_data["value_row"]
#   ordered_asc_value_row = sorted(range_data["value_row"])

#   i = 0
#   e = range_data["error_count"]
#   for num in asc_value_row:
#     if(is_asc == True):
#       # check if row is asc
#       if(num != ordered_asc_value_row[i]):
#         # when not asc remove issue level and reprocess
#         e += 1

#         if(e > 1):
#           is_asc = False
#           break
#         asc_value_row.pop(i)
#         # print(asc_value_row)

#         # reorder original list after removal
#         ordered_asc_value_row = sorted(asc_value_row)
#         # print(ordered_asc_value_row)
#         k = 0
#         for num_asc_second_check in asc_value_row:
#           # print(f"Hit secondary loop - position {i}")
#           if(num_asc_second_check != ordered_asc_value_row[k]):
#             # print("Tried to remove to many. Moving to next row.")
#             e += 1
#             is_asc = False
#             break

#           k += 1
#     i += 1
#   # print(is_asc)
#   # print(is_in_range)
#   return {
#       "is_asc": is_asc,
#       "error_count": e,
#       "value_row": asc_value_row
#   }

# def check_desc(range_data):
#   is_desc = True
#   desc_value_row = range_data["value_row"]
#   ordered_desc_value_row = sorted(range_data["value_row"], reverse=True)


#   i = 0
#   e = range_data["error_count"]
#   for num in desc_value_row:
#     if(is_desc == True):
#       # check if row is asc
#       if(num != ordered_desc_value_row[i]):
#         # when not asc remove issue level and reprocess
#         e += 1

#         if(e > 1):
#           is_desc = False
#           break
#         desc_value_row.pop(i)
#         # print(asc_value_row)

#         # reorder original list after removal
#         ordered_desc_value_row = sorted(desc_value_row)
#         # print(ordered_asc_value_row)
#         k = 0
#         for num_desc_second_check in desc_value_row:
#           # print(f"Hit secondary loop - position {i}")
#           if(num_desc_second_check != ordered_desc_value_row[k]):
#             # print("Tried to remove to many. Moving to next row.")
#             e += 1
#             is_desc = False
#             break

#           k += 1
#     i += 1
#   # print(is_asc)
#   # print(is_in_range)
#   return {
#       "is_desc": is_desc,
#       "error_count": e,
#       "value_row": desc_value_row
#   }

def check_distances(distances, value_row, error_count):
  try:
    is_valid = True
    positive_positions = []
    negative_positions = []
    error_count = 0
    i = 0
    for distance in distances:
      # Check if distance is out of allowable range
      if (distance > 3) or (distance < -3):
        error_count += 1
        if(error_count >= 2):
          return False

        # check if positive distance
        if(distance > 0):
          error_count += 1
          # remove bad value
          value_row.pop(i + 1)
          # recheck validity
          get_distance_validity(value_row, error_count)

        # check if negative distance or 0
        if(distance < 0 or distance == 0):
          error_count += 1
          # remove bad value
          value_row.pop(i)
          # recheck validity
          get_distance_validity(value_row, error_count)

      # collect position of positive and negative values
      if(distance > 0):
        # handle positive case=
        positive_positions.append(i)

      if(distance < 0):
        # handle negative case
        negative_positions.append(i)

      # if (+)'s >= 2 and (-)'s >= 2 return false, list is invalid
      if(len(positive_positions) >= 2 and len(negative_positions) >= 2):
        return False

      # when this occurs then pop then negative element and reprocess
      if(len(positive_positions) >= 2 and len(negative_positions) < 2  and len(negative_positions) > 0 and error_count == 0):
        error_count += 1
        if(error_count > 1):
          return False
        # need to pop the negative element and reprocess
        value_row.pop(negative_positions[0])
        get_distance_validity(value_row, error_count)

      # when this occurs then pop then positive element and reprocess
      if(len(negative_positions) >= 2 and len(positive_positions) < 2 and len(positive_positions) > 0 and error_count == 0):
        error_count += 1
        if(error_count > 1):
          return False
        # need to pop the positive element and reprocess
        value_row.pop(positive_positions[0] + 1)
        get_distance_validity(value_row, error_count)

    # More than two errors means list is invalid
    if (error_count < 2):
      return True
    else:
      return False
  except ValueError as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
    print(value_row)

def get_distance_validity(value_row, error_count):
  print(value_row)
  distances = []
  i = 0
  for num in value_row:
    # if logic was added to stop distance check from going out of bounds
    if(i + 1 != len(value_row)):
      # add all distances to an arry
      distances.append(value_row[i+1] - num)
    i += 1

  return check_distances(distances, value_row, error_count)

  # for distance in distances:
  #     if (distance > 3) or (distance < -3):
  #       error_count += 1
  #       # check if positive distance
  #       if(distance > 0):
  #         # handle positive case
  #         value_row.pop(i + 1)


  #       if(distance < 0):
  #         # handle negative case
  #         value_row.pop(i)




  #     counter += 1

  #       if(e > 1):
  #         is_in_range = False
  #         break
  #       value_row.pop(i)
  #       k = 0
  #       for num_second_check in value_row:
  #         if (k != 0):
  #           # get distance
  #           distance = abs(value_row[k-1] - value_row[k])
  #           if (distance == 0 or distance > 3):
  #             is_in_range = False
  #             break
  #         k += 1

  #     i += 1


  # my_obj = {
  #   "is_in_range": is_in_range,
  #   "error_count": e,
  #   "value_row": value_row
  # }

  # print(json.dumps(my_obj, indent=4))
  # return my_obj







if __name__ == "__main__":
  main()

