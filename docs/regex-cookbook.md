# Regular Expression Cookbook

A quick reference for nine common regular-expression patterns. The patterns
below are illustrative starting points rather than authoritative or tested
specifications, and they are not guaranteed to be exhaustive, safe, or
production-grade. They are also written in a generic style: no particular
regular-expression flavour or engine is guaranteed to accept every one of them
unchanged. Treat each pattern as a place to begin, then adapt it to the task
and the tool at hand.

## Email-like address

Matches a simple address made of word, dot, percent, plus, and hyphen
characters, an at sign, a domain, and a dot followed by a short ending.

```
[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
```

Example match: `someone@example.com`

## ISO-style date

Matches four digits, a hyphen, two digits, a hyphen, and two digits, in the
familiar year-month-day shape.

```
\d{4}-\d{2}-\d{2}
```

Example match: `2026-10-31`

## Whitespace runs

Matches one or more whitespace characters in a row, such as spaces, tabs, or
line breaks, wherever they appear.

```
\s+
```

Example match: `"   "` (a run of three spaces)

## Digit runs

Matches one or more decimal digits in a row, with no other characters mixed in.

```
\d+
```

Example match: `12345`

## Repeated characters

Matches any single character that is immediately repeated three or more times,
using a capture group and a backreference to the earlier character.

```
(.)\1{2,}
```

Example match: `zzzz`

## Optional-sign decimal number

Matches a whole number with an optional leading minus sign and an optional
fractional part, so both integers and decimals are accepted.

```
-?\d+(\.\d+)?
```

Example match: `-42.5`

## Hexadecimal colour

Matches a hash sign followed by exactly six hexadecimal digits, as used for a
six-digit colour value.

```
#[0-9A-Fa-f]{6}
```

Example match: `#1A2B3C`

## Whole word

Matches the word "cat" only when it stands alone, because the word-boundary
markers prevent it from matching inside a longer word.

```
\bcat\b
```

Example match: `cat` (but not the "cat" inside "concatenate")

## Quoted string

Matches a double quote, then any run of characters that are not a double
quote, then a closing double quote, capturing the text between the quotes.

```
"[^"]*"
```

Example match: `"hello, world"`
