Project goal:  
Create a dictionary with words and frequencies that can be passed to the `generate_from_frequencies` function of the WordCloud class.

```py
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
cloud.to_file("myfile.jpg")
```

**Notes**

- Remove all punctuation marks. `isalpha(method)`.
- Check if words are part of the "uninteresting" set of words ('a', 'the', 'to', 'if')
  - Make this set a parameter to the function.

Input file -> File that contains text only.
eg. from [Project Gutenberg](https://www.gutenberg.org/)

`pip install wordcloud`
