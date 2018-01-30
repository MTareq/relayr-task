### Requirements
- `pytest`

### Usage

using the spec in the Task description.

```python
   from finder.finder import Finder
   finder=Finder(['asd', 'asdd', 'fre', 'glk', 'lkm', 'ads', 'dsa', 'AdS', 'dSa']);
   found = finder.find('sad')
   print(found)
```
```bash
   ['asd', 'ads', 'dsa']
```
Also i added an ignore case option by setting the second argument to True in the find method

```python
   finder=Finder(['asd', 'asdd', 'fre', 'glk', 'lkm', 'ads', 'dsa', 'AdS', 'dSa']);
   found = finder.find('sad', True)
   print(found)
```

```bash
   ['asd', 'ads', 'dsa', 'AdS', 'dSa']
```

### Testing
in the root directory run `pytest -v`

#### TestsCases
- regular test
- irregular string list tests
- wrong type for input test case
- 1k-100k in legnth initial list
- 100k, 500k, 1M runs of Finder.find that runs on less than 2, 10, 20 seconds respectively


