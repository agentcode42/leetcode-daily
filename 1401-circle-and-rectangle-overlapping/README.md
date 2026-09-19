# 1401. Circle and Rectangle Overlapping

## Problem

Given a circle and an axis-aligned rectangle, determine whether the circle and rectangle overlap.

The circle is defined by:

* `radius`
* `(xCenter, yCenter)`

The rectangle is defined by:

* Bottom-left corner `(x1, y1)`
* Top-right corner `(x2, y2)`

Return `True` if the circle and rectangle overlap, otherwise return `False`.

## Approach

The key idea is to find the **minimum squared distance between the circle's center and the rectangle**.

If this distance is less than or equal to `radius`, the circle overlaps the rectangle.

### 1. Distance in the X direction

If the circle's center is already inside the rectangle's horizontal range:

```text
x1 <= xCenter <= x2
```

then the X contribution to the distance is `0`.

Otherwise, the closest point on the rectangle is either `x1` or `x2`.

So we add the squared distance to whichever boundary is closer:

```python
if xCenter < x1 or xCenter > x2:
    dist += min((x1 - xCenter) ** 2, (x2 - xCenter) ** 2)
```

### 2. Distance in the Y direction

We do the same thing vertically.

If:

```text
y1 <= yCenter <= y2
```

the Y contribution is `0`.

Otherwise, we add the squared distance to the closest horizontal boundary:

```python
if yCenter < y1 or yCenter > y2:
    dist += min((y1 - yCenter) ** 2, (y2 - yCenter) ** 2)
```

### 3. Compare with the radius

The squared Euclidean distance from the circle's center to the closest point on the rectangle is:

```text
dx² + dy²
```

There is no need to calculate the actual distance using a square root.

We simply compare:

```text
distance² <= radius²
```

If true, the circle reaches the rectangle.

## Code

```python
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        dist = 0

        if xCenter < x1 or xCenter > x2:
            dist += min((x1 - xCenter) ** 2, (x2 - xCenter) ** 2)

        if yCenter < y1 or yCenter > y2:
            dist += min((y1 - yCenter) ** 2, (y2 - yCenter) ** 2)

        return dist <= radius ** 2
```

## Example

Suppose the rectangle is:

```text
(x1, y1) = (2, 2)
(x2, y2) = (5, 5)
```

and the circle's center is:

```text
(xCenter, yCenter) = (7, 6)
```

The center is outside the rectangle in both directions.

The closest horizontal distance is:

```text
7 - 5 = 2
```

The closest vertical distance is:

```text
6 - 5 = 1
```

Therefore:

```text
distance² = 2² + 1²
          = 5
```

If `radius = 2`:

```text
radius² = 4
```

Since:

```text
5 > 4
```

the circle does not overlap the rectangle.

## Important Observation

The center does **not** have to be inside the rectangle for the shapes to overlap.

The circle can overlap the rectangle from outside.

That is why we calculate the distance from the center to the **closest point of the rectangle**, rather than simply checking whether the center lies inside the rectangle.

Also, when the center is inside the rectangle along one axis, that axis contributes `0` to the distance.

## Complexity Analysis

* **Time:** `O(1)`
* **Space:** `O(1)`

Only a constant number of arithmetic and comparison operations are performed.
