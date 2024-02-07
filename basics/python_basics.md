# Python basics

## List comprehension

```python
doc_sets = [inverted_index[word] for word in words if word in inverted_index]
```

## eval

[385 Mini Parser](https://leetcode.com/problems/mini-parser/description/)

```python
class Solution:
    def deserialize(self, s: str) -> NestedInteger:

        def helper(s):
            if isinstance(s, int):
                return NestedInteger(int(s))
            out = NestedInteger()
            for v in s:
                out.add(helper(v))
            return out
        
        print(type(eval(s)))
        return helper(eval(s))
```