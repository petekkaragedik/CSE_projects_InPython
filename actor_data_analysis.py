# -*- coding: utf-8 -*-
"""actor_data_analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gwz2oKao1Fg_17xIwxEbH2TIRMdmfDpl
"""

start = int(input("Enter the starting year: "))
end = int(input("Enter the end year: "))
if start > end:
  print("The starting year must be less than or equal to the end year!")
else:
  inFile = open("netflix.txt", "r")
  country = input("Enter the country: ")
  alldatalists = inFile.readlines()
  countrylistss = []
  for row in alldatalists:
    row = row.split("\t")
    cntrs = row[3]
    cntrslist = cntrs.split(", ")
    for c in cntrslist:
      countrylistss.append(c)
  while country not in countrylistss:
    print(country, "does not exist in the database!")
    country = input("Enter the country: ")
    if country in countrylistss:
      break
  inFile.close()

  inFilee = open("netflix.txt", "r")
  lineslistwiththeheader = inFilee.readlines()
  lineslist = lineslistwiththeheader[1:]
  threshold = int(input("Enter the threshold value: "))
  dictionary = {}
  for line in lineslist:
    linee = line.split("\t")
    countrieslist = linee[3]
    countrieslist = countrieslist.split(", ")
    if country in countrieslist:
      year = linee[-1]
      if int(year) >= start and int(year) <= end:
        actors = linee[2]
        actorslist = actors.split(", ")
        for actor in actorslist:
          if actor[0] == " ":
            actor = actor[1:]
          if actor not in dictionary:
            dictionary[actor] = 1
          else:
            dictionary[actor] += 1
  dictionary= dict(sorted(dictionary.items()))
  validactorslist = []
  numberofmovies = []
  for actor in dictionary:
    if int(dictionary[actor]) >= threshold:
      validactorslist.append(actor)
      numberofmovies.append(dictionary[actor])
  count = len(validactorslist)
  counter = 1
  if count == 0:
    print("No actors found!")
  else:
    print("The list of actors (alphabetically ordered) who played in at least", str(threshold), "movies between", str(start), "and", str(end))
    for item in validactorslist:
      print(str(counter) + ") " + validactorslist[counter - 1] + " (" + str(numberofmovies[counter - 1]) + " movies)")
      counter += 1
  inFilee.close()
