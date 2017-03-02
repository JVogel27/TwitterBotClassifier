== Intro ==
This is the bot/human labeled data used in the following paper currently under submission to ASONAM 2015:
	A New Approach to Bot Detection: The Importance of Recall
	Authors:
		Fred Morstatter (ASU)
		Liang Wu (ASU)
		Tahora Nazer (ASU)
		Mark Karlsrud (ASU)
		Kathleen M. Carley (CMU)
		Huan Liu (ASU)

== Format ==
The data consists of two files:
	libya.txt - Arab Spring activity in Libya.
	honeypot.txt - Bots collected via the Honeypot approach.
The collection and labeling strategies for both are described in detail in the above paper.

Both files share an identical file format. Each file is formatted as follows:
	- Each line describes one user in the dataset.
	- Each line is formatted as follows:
		<label> <user_id> <tweet_id_1> <tweet_id_2> ... <tweet_id_n>
		- The <label> is either "bot", or "human", indicating the label the user received from the corresponding labeling method.
		- The <user_id> is the user's Twitter ID.
		- <tweet_id_1:n> are the ID's of all of the user's tweets included in our study.
