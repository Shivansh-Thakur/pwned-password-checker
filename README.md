# pwned-password-checker

Searching by range

In order to protect the value of the source password being searched for, Pwned Passwords implements a k-Anonymity model that allows a password to be searched for by partial hash. This allows the first 5 characters of a SHA-1 password hash (not case-sensitive) to be passed to the API (testable by clicking here):

GET https://api.pwnedpasswords.com/range/{first 5 hash chars}

When a password hash with the same first 5 characters is found in the Pwned Passwords repository, the API will respond with an HTTP 200 and include the suffix of every hash beginning with the specified prefix, followed by a count of how many times it appears in the data set. The API consumer can then search the results of the response for the presence of their source hash and if not found, the password does not exist in the data set. A sample response for the hash prefix "21BD1" would be as follows:

0018A45C4D1DEF81644B54AB7F969B88D65:1

00D4F6E8FA6EECAD2A3AA415EEC418D38EC:2

011053FD0102E94D6AE2F8B83D76FAF94F6:1

012A7CA357541F0AC487871FEEC1891C49C:2

0136E006E24E7D152139815FB0FC6A50B15:2

...

On average, a range search returns 478 hash suffixes, although this number will differ depending on the hash prefix being searched for. The smallest result is 381, the largest 584. There are 1,048,576 different hash prefixes between 00000 and FFFFF (16^5) and every single one will return HTTP 200; there is no circumstance in which the API should return HTTP 404.
Code	Body	Description

200	Hash suffixes   counts	Ok — all password hashes beginning with the searched prefix are returned alongside prevalence counts..
