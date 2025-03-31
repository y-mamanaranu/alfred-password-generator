# Alfred Password Generator
An Alfred workflow to generate passwords arbitrally.

![screen shot](https://github.com/user-attachments/assets/72d8e9b5-d808-4972-8cc0-90b842d69dc6)

# Usage

```
passgen [length: default 18] [character: default A-Za-z0-9]
passgen panc [length: default 18] [character: default A-Za-z0-9!-*]
```

`passgen` generates a password with a specified length and selected character.
length is 18 by default and characters are limited to the alphabet in lower and upper case and digits.

`passgen panc` is almost the same as `passgen` but default characters contain punctuation.

```
passgen split [length: default 18] [by: default 6] [character: default A-Za-z0-9]
passgen panc split [length: default 18] [by: default 6] [character: default A-Za-z0-9]
```

`passgen split` generates a password with a specified length and selected characters separated by some length `by`.
length is 18 and separated by 6 by default and characters are limited to the alphabet in lower and upper case and digits.
`length` must be divisible by `by`.

`passgen panc split` is almost the same as `passgen split` but default characters contain punctuation.

`character` can be list directly as `ABCDEFabcdef012345!@#^&*` or by range `A-Fa-f0-5!-*`.
The punctuation is in order of `!@#^&*`.
