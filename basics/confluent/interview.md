# Confluent

[Leetcode Confluent](https://leetcode.com/discuss/interview-question?currentPage=1&orderBy=most_relevant&query=Confluent)

## 1

First round was technical - Windowed Average problem (you would need to implement a cache where each item has an expiration time, you would also need to return the average of the valid elements in the cache at any given point time.)

Design round 1(API design) - Spotify like system. Design APIs to retrieve X podcast channels at a time, X audio clips per podcast channel, Database design and high level component design [pagination, skip tokens, limit/offset, api versioning, back of the napkin calculation for number of users to number of podcast channels, podcast channel to number of audio clips per channel, corner cases[users subscribed to a lot of channels, channels with a lot of videos, etc.,]]

Coding round: Given a filled sudoku board, validate if the board is solved or not [optimize the number of traversals through the board - attempt at solving in 1 traversal] - Add test cases and make sure it runs and passes.
As an extension, given an unsolved board how do you solve it (backtracking with recursion - did not have to implement this)

Design round: TinyUrl (Constraints: optimize only for high volume of reads - a simple singleton service with a sharded database(range based sharding on short url would suffice. You can add more read replicas with additional caching at the edge if needed). Do not make it complex

Behavior - Talk about a project you are most proud of, understand the technical details, the business use case. Talk about the challenges, conflicts that came about, etc.,

Coding - Given a list of documents [Pair of id and content], return the list of documentIds for a given search phrase. Dictionary of documentId to dictionary of string and their index - Use this to then check for a given search phrase.

Had major miscommunication and hiccups with scheduling and HR, most interviewers were nice and kind - No offer

