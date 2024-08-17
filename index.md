# Competitive Programmer’s Handbook
## Part I: Basic Techniques
### Chapter 1: Introduction
#### Programming Languages
##### C++ Code Template
```cpp
#include <bits/stdc++.h>
using namespace std;

int main () {
	// solution comes here
}
```
This code can be compiled using:
```shell
g++ -std=c++11 -O2 -Wall test.cpp -o test
```
or simply:
```bash
g++ test.cpp -o test
```
#### Input and Output
[`cin`](https://en.cppreference.com/w/cpp/io/cin) can be used for input.
```cpp
int a, b;
string s;
cin >> a >> b >> s;
```
[`cout`](https://en.cppreference.com/w/cpp/io/cout) can be used for output.
```cpp
int a = 123, b = 456;
string s = "monkey";
cout << a << " " << b << " " << s << "\n";
```
The output of this code is:

```Output
123 456 monkey
```

> ***Note:*** [`\n`](https://en.cppreference.com/w/cpp/language/escape) is used to create a newline and it is faster than [`endl`](https://en.cppreference.com/w/cpp/io/manip/endl). However, `endl` flushes the stream while `\n` does not.

You can use the following commands to make input and output faster:
```cpp
ios::sync_with_stdio(0);
cin.tie(0); cout.tie(0);
```
You can use C functions [`scanf`](https://en.cppreference.com/w/c/io/fscanf) and [`printf`](https://en.cppreference.com/w/c/io/fprintf) as alternatives to `cin` and `cout`.
```cpp
int a, b;
scanf("%d %d", &a, &b);
printf("%d %d", a, b);
```
To read a whole line you can use [`getline`](https://en.cppreference.com/w/cpp/string/basic_string/getline).
```cpp
string s;
getline(cin, s);
```
For unknown amounts of data you can use:
```cpp
while (cin >> x) {
	// code
}
```
Some systems want you to read from a file and write to a file. C++ has [`freopen`](https://en.cppreference.com/w/cpp/io/c/freopen) for this.
```cpp
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
```
After these commands you can use `cin`, `cout` as you normally would.

#### Working with Numbers
##### [Integers](https://en.cppreference.com/w/cpp/language/types)

| Datatype    | Bits | Range                 |
| ----------- | ---- | --------------------- |
| `int`       | 32   | $(-2^{31}, 2^{31}-1)$ |
| `long long` | 64   | $(-2^{63},2^{63}-1)$  |
| `short`     | 16   | $(-2^{15},2^{15}-1)$  |

You can add `unsigned` infront of a datatype to make it unsigned. 

| Datatype             | Bits | Range             |
| -------------------- | ---- | ----------------- |
| `unsigned int`       | 32   | $(0, 2^{32} - 1)$ |
| `unsigned long long` | 64   | $(0, 2^{64} - 1)$ |
| `unsigned short`     | 16   | $(0, 2^{16} - 1)$ |

##### Modular Arithmetic

$$
\begin{array}{rcl}
(a + b) \bmod  m  & = &  (a \bmod m + b \bmod m)  \bmod m \\
(a - b)  \bmod m & = & (a \bmod m-b \bmod m) \bmod m \\
(a \cdot b) \bmod m & = & (a \bmod m \cdot b \bmod m)  \bmod m
\end{array}
$$
You use `%` operator for modulus operation in C++.

##### [Floating Point Numbers](https://en.cppreference.com/w/cpp/language/types)
