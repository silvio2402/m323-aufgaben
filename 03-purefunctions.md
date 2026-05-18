# Pure functions

<https://gitlab.com/ch-tbz-it/Stud/m323/m323/-/blob/main/03_PureFunctions/Aufgaben/README.md>

| Exercise | One Return value | Only dependent on parameters | Doesn't change external state | pure/impure |
| -------- | ---------------- | ---------------------------- | ----------------------------- | ----------- |
| 1.1      | Yes              | No                           | No                            | Impure      |
| 1.2      | Yes              | Yes                          | Yes                           | Pure        |
| 1.3      | Yes              | Yes                          | Yes                           | Pure        |
| 1.4      | Yes              | No                           | Yes                           | Impure      |
| 1.5      | No               | Yes                          | Yes                           | Impure      |
| 1.6      | Yes              | Yes                          | No                            | Impure      |

## 1.1

```ts
function addToCart<ItemType>(
  cartItems: ItemType[],
  item: ItemType,
): ItemType[] {
  return [...cartItems, item];
}
```

## 1.4

```ts
function multiplyWithRandom(num: number, randomValue: number): number {
  return num * randomValue;
}
```

## 1.5

```ts
function divideNumbers(dividend: number, divisor: number): number {
  if (divisor === 0) {
    return NaN;
  }
  return dividend / divisor;
}
```

## 1.6

Nicht möglich, in eine pure-function umzuwandeln.

## 3.1

```py
def sumReduce(values: float[]) -> float:
    if len(values) == 0:
        return 0
    return values[0] + sumReduce(values[1:])
```

## 3.2

```py
def avgReduce(values: list[float]) -> float:
    n_values = len(values)
    if n_values == 0:
        return 0
    if n_values == 1:
        return values[0]
    return (values[0] + avgReduce(values[1:]) * (n_values - 1)) / n_values
```

## 3.3

```py
def minStrIndex(l: list[str]) -> int:
    if len(l) == 0:
        return 0
    result = 0
    for i, item in enumerate(l):
        if item < l[result]:
            result = i
    return result

def sortRecursive(l: list[str]) -> list[str]:
    if len(l) == 0:
        return []
    i = minStrIndex(l)
    rest = l[:i] + l[i+1:]
    if len(rest) == 0:
        return [l[i]]
    return [l[i]] + sortRecursive(rest)
```

## 3.4

```py
objs = [
    {"date": "2024-01-01", "priority": 2, "title": "Task 1"},
    {"date": "2024-01-02", "priority": 1, "title": "Task 2"},
    {"date": "2024-01-01", "priority": 1, "title": "Task 3"},
]

def sortObjs(objs: list[dict]) -> list[dict]:
    return sorted(objs, key=lambda obj: (obj["date"], obj["priority"], obj["title"]))
```

## 3.5

```py
tree = {
    "value": 5,
    "children": [
        {"value": 3, "children": []},
        {"value": 8, "children": [
            {"value": 7, "children": []},
            {"value": 10, "children": []}
        ]},
        {"value": 1, "children": []}
    ]
}

def getLeafValues(tree: dict) -> list[int]:
    if not tree["children"]:
        return [tree["value"]]
    values = []
    for child in tree["children"]:
        values.extend(getLeafValues(child))
    return values

```
