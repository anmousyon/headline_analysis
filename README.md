# headline_analysis
An attempt at finding good news and bad news in Python.

Tell it how many titles you want, and from what subreddit.  It will pass those titles to the api at http://text-processing.com/ which returns the sentiment.

Example use:

```
$ ./reddit_titles.py -n 15 news
neutral  Hot Air Balloon Carrying at Least 16 People Crashes in Texas
pos      Human-Like Speech Seen In Orangutans For The First Time — NOVA Next | PBS
neutral  Obama Signs Bill Mandating GMO Labeling
neutral  3 Walmart employees charged with manslaughter in death of shoplifter
neutral  Oakland police sergeant faced no charges for domestic violence arrest despite video evidence
neutral  Former Miami Dolphins linebacker Antonio Armstrong and his wife were killed at their Houston home on Friday. Police say the couple's 16-year-old son has been charged for the murder.
neutral  Muslim leaders in Normandy have refused to bury one of the church attackers who murdered a priest during morning mass
neutral  Phoenix PD: Parents force 6-year-old to stand outside barefoot causing severe burns
neutral  Stockton mayor's stolen gun used in the murder of 13-year-old boy
neutral  Israel and U.S. are close to a deal on the biggest military aid package ever
neutral  Indianapolis police officer who shot a fellow officer arrested in Cincinnati
neutral  Illinois DNR looking to enlist “river monster” to battle Asian carp in Mississippi and other rivers
neutral  Police: Undocumented immigrant sexually assaulted 7-year-old girl in San Antonio
neutral  Plastic bag use plummets in England since 5p charge
neutral  Witness to William Chapman shooting contradicts police officer's account
```
