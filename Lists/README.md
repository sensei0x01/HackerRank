# **[List](https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true)**

  <input type="hidden" id="naderly" name="Writen by: Ahmed Nader" value="https://github.com/naderly">

Consider a list (list = []). You can perform the following commands:

> - `insert` _`i`_ _`e`_ : Insert integer _`e`_ at position _`i`_ . <br>
> - `print` : Print the list. <br>
> - `remove` _`e`_ : Delete the first occurrence of integer _`e`_ . <br>
> - `append` _`e`_ : Insert integer _`e`_ at the end of the list. <br>
> - `sort` : Sort the list. <br>
> - `pop` : Pop the last element from the list. <br>
> - `reverse` : Reverse the list.<br>

> Initialize your list and read in the value of _`n`_ followed by _`n`_ lines of commands where each command will be of the `7` types listed above. Iterate through each command in order and perform the corresponding operation on your list.

## Example

`N = 4` <br>
`append 1` <br>
`append 2` <br>
`insert 3 1` <br>
`print`

> append 1 : Append 1 to the list, arr=[1]. <br>
> append 2 : Append 2 to the list, arr=[1,2]. <br>
> insert 3 1 : Insert 3 at index 1, arr=[1,3,2].<br>
> print: Print the array.

### Output

```sh
[1, 3, 2]
```

## Input Format

> The first line contains an integer, _`n`_ , denoting the number of commands. <br>
> Each line _`i`_ of the _`n`_ subsequent lines contains one of the commands described above.

## Constraints

> The elements added to the list must be integers.

## Output Format

> For each command of type print, print the list on a new line.

## Sample Input 0

```sh
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
```

## Sample Output 0

```sh
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

```
