# Intro

## Exercise 1

```java
public static int calculateScore(String word) {
    int score = 0;
    for (char c : word.toCharArray()) {
        if (c == 'a') continue;
        score++;
    }
    return score;
}
```

```java
public static int wordScore(String word) {
    return word.chars().filter(c -> c != 'a').count();
}
```
