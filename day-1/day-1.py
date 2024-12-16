def main():
  # Part 1
  with open("list.txt", "r") as file:
    rows = file.readlines()

  col_1 = []
  col_2 = []

  for row in rows:
    values = row.split()
    col_1.append(int(values[0]))
    col_2.append(int(values[1]))

  col_1_sorted = sorted(col_1)
  col_2_sorted = sorted(col_2)

  total_distance = 0

  for i in range(len(col_1_sorted)):
    total_distance += abs(col_1_sorted[i] - col_2_sorted[i])

  print(f"Part 1 - The total distance was: {total_distance}")


  # Part 2
  col_1_distinct = list(set(col_1))

  totals = []
  #short_cut_total = 0
  long_way_total = 0
  # Short cut
  for i in range(len(col_1_distinct)):
    count = 0
    for j in range(len(col_2)):
      if col_1_distinct[i] == col_2[j]:
        #short_cut_total += col_2[j]
        count += 1

    totals.append([col_1_distinct[i], count])

  for i in range(len(totals)):
    long_way_total += totals[i][0] * totals[i][1]


  #print(short_cut_total)
  print(long_way_total)





if __name__ == "__main__":
  main()
